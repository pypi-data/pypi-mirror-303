"""Results Only protocol."""

from __future__ import annotations

from collections.abc import Mapping
import os
import time
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Optional,
    Protocol,
    Union,
    runtime_checkable,
)

from bitfount.federated.aggregators.base import (
    _AggregatorWorkerFactory,
    _BaseAggregatorFactory,
    _BaseModellerAggregator,
    _BaseWorkerAggregator,
    registry as aggregators_registry,
)
from bitfount.federated.aggregators.secure import _InterPodAggregatorWorkerFactory
from bitfount.federated.algorithms.base import registry as algorithms_registry
from bitfount.federated.helper import _create_aggregator
from bitfount.federated.logging import _get_federated_logger
from bitfount.federated.model_reference import BitfountModelReference
from bitfount.federated.protocols.base import (
    BaseCompatibleAlgoFactory,
    BaseCompatibleModellerAlgorithm,
    BaseCompatibleWorkerAlgorithm,
    BaseModellerProtocol,
    BaseProtocolFactory,
    BaseWorkerProtocol,
)
from bitfount.federated.transport.modeller_transport import (
    _ModellerMailbox,
)
from bitfount.federated.transport.worker_transport import (
    _InterPodWorkerMailbox,
    _WorkerMailbox,
)
from bitfount.types import (
    T_NESTED_FIELDS,
    DistributedModelProtocol,
    _StrAnyDict,
)
from bitfount.utils import delegates

if TYPE_CHECKING:
    from bitfount.federated.pod_vitals import _PodVitals
    from bitfount.hub.api import BitfountHub

logger = _get_federated_logger(__name__)


@runtime_checkable
class _ResultsOnlyCompatibleModellerAlgorithm(
    BaseCompatibleModellerAlgorithm, Protocol
):
    """Defines modeller-side algorithm compatibility."""

    def run(self, results: Mapping[str, Any]) -> _StrAnyDict:
        """Runs the modeller-side algorithm."""
        ...


@runtime_checkable
class _ResultsOnlyCompatibleWorkerAlgorithm(BaseCompatibleWorkerAlgorithm, Protocol):
    """Defines worker-side algorithm compatibility."""

    def run(self, *, final_batch: bool = False) -> Any:
        """Runs the worker-side algorithm."""
        ...


class _ModellerSide(BaseModellerProtocol):
    """Modeller side of the ResultsOnly protocol."""

    algorithm: _ResultsOnlyCompatibleModellerAlgorithm
    aggregator: Optional[_BaseModellerAggregator]

    def __init__(
        self,
        *,
        algorithm: _ResultsOnlyCompatibleModellerAlgorithm,
        aggregator: Optional[_BaseModellerAggregator],
        mailbox: _ModellerMailbox,
        **kwargs: Any,
    ):
        super().__init__(algorithm=algorithm, mailbox=mailbox, **kwargs)
        self.aggregator = aggregator

    async def run(
        self,
        iteration: int = 0,
        **kwargs: Any,
    ) -> Union[list[Any], Any]:
        """Runs Modeller side of the protocol."""
        eval_results = await self.mailbox.get_evaluation_results_from_workers()
        logger.info("Results received from Pods.")

        modeller_results = self.algorithm.run(eval_results)

        if self.aggregator:
            return self.aggregator.run(modeller_results)

        return modeller_results


class _WorkerSide(BaseWorkerProtocol):
    """Worker side of the ResultsOnly protocol."""

    algorithm: _ResultsOnlyCompatibleWorkerAlgorithm
    aggregator: Optional[_BaseWorkerAggregator]

    def __init__(
        self,
        *,
        algorithm: _ResultsOnlyCompatibleWorkerAlgorithm,
        aggregator: Optional[_BaseWorkerAggregator],
        mailbox: _WorkerMailbox,
        **kwargs: Any,
    ):
        super().__init__(algorithm=algorithm, mailbox=mailbox, **kwargs)
        self.aggregator = aggregator

    async def run(
        self,
        pod_vitals: Optional[_PodVitals] = None,
        **kwargs: Any,
    ) -> Any:
        """Runs Worker side of the protocol."""
        final_batch: bool = kwargs.get("final_batch", False)
        if pod_vitals:
            pod_vitals.last_task_execution_time = time.time()

        results = self.algorithm.run(final_batch=final_batch)

        if self.aggregator:
            logger.debug("Aggregating results...")
            results = await self.aggregator.run(results)
            logger.debug("Aggregation complete.")

        if hasattr(results, "msgpack_serialize"):
            await self.mailbox.send_evaluation_results(results.msgpack_serialize())
        else:
            await self.mailbox.send_evaluation_results(results)

        return results


@runtime_checkable
class _ResultsOnlyCompatibleAlgoFactory(BaseCompatibleAlgoFactory, Protocol):
    """Defines algo factory compatibility."""

    def modeller(self, **kwargs: Any) -> _ResultsOnlyCompatibleModellerAlgorithm:
        """Create a modeller-side algorithm."""
        ...


@runtime_checkable
class _ResultsOnlyCompatibleAlgoFactory_(_ResultsOnlyCompatibleAlgoFactory, Protocol):
    """Defines algo factory compatibility."""

    def worker(self, **kwargs: Any) -> _ResultsOnlyCompatibleWorkerAlgorithm:
        """Create a worker-side algorithm."""
        ...


@runtime_checkable
class _ResultsOnlyCompatibleModelAlgoFactory(
    _ResultsOnlyCompatibleAlgoFactory, Protocol
):
    """Defines algo factory compatibility."""

    model: Union[DistributedModelProtocol, BitfountModelReference]
    pretrained_file: Optional[Union[str, os.PathLike]] = None

    def worker(
        self, hub: BitfountHub, **kwargs: Any
    ) -> _ResultsOnlyCompatibleWorkerAlgorithm:
        """Create a worker-side algorithm."""
        ...


@delegates()
class ResultsOnly(BaseProtocolFactory):
    """Simply returns the results from the provided algorithm.

    This protocol is the most permissive protocol and only involves one round of
    communication. It simply runs the algorithm on the `Pod`(s) and returns the
    results as a list (one element for every pod) unless an aggregator is specified.

    Args:
        algorithm: The algorithm to run.
        aggregator: The aggregator to use for updating the algorithm results across all
            Pods participating in the task.  This argument takes priority over the
            `secure_aggregation` argument.
        secure_aggregation: Whether to use secure aggregation. This argument is
            overridden by the `aggregator` argument.

    Attributes:
        name: The name of the protocol.
        algorithm: The algorithm to run. This must be compatible with the `ResultsOnly`
            protocol.
        aggregator: The aggregator to use for updating the algorithm results.

    Raises:
        TypeError: If the `algorithm` is not compatible with the protocol.
    """

    # TODO: [BIT-1047] Consider separating this protocol into two separate protocols
    # for each algorithm. The algorithms may not be similar enough to benefit
    # from sharing one protocol.

    algorithm: Union[
        _ResultsOnlyCompatibleAlgoFactory_, _ResultsOnlyCompatibleModelAlgoFactory
    ]
    nested_fields: ClassVar[T_NESTED_FIELDS] = {
        "algorithm": algorithms_registry,
        "aggregator": aggregators_registry,
    }

    def __init__(
        self,
        *,
        algorithm: Union[
            _ResultsOnlyCompatibleAlgoFactory_, _ResultsOnlyCompatibleModelAlgoFactory
        ],
        aggregator: Optional[_BaseAggregatorFactory] = None,
        secure_aggregation: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(algorithm=algorithm, **kwargs)
        self.aggregator: Optional[_BaseAggregatorFactory] = None

        if aggregator:
            self.aggregator = aggregator
        elif secure_aggregation:
            self.aggregator = _create_aggregator(secure_aggregation=secure_aggregation)
        else:
            logger.info("No aggregator specified. Will return a dictionary of results.")

    @classmethod
    def _validate_algorithm(
        cls,
        algorithm: BaseCompatibleAlgoFactory,
    ) -> None:
        """Checks that `algorithm` is compatible with the protocol."""
        if not isinstance(
            algorithm,
            (
                _ResultsOnlyCompatibleAlgoFactory_,
                _ResultsOnlyCompatibleModelAlgoFactory,
            ),
        ):
            raise TypeError(
                f"The {cls.__name__} protocol does not support "
                + f"the {type(algorithm).__name__} algorithm.",
            )

    def modeller(self, mailbox: _ModellerMailbox, **kwargs: Any) -> _ModellerSide:
        """Returns the modeller side of the ResultsOnly protocol."""
        if isinstance(self.algorithm, _ResultsOnlyCompatibleModelAlgoFactory):
            algorithm = self.algorithm.modeller(
                pretrained_file=self.algorithm.pretrained_file
            )
        else:
            algorithm = self.algorithm.modeller()
        return _ModellerSide(
            algorithm=algorithm,
            aggregator=self.aggregator.modeller() if self.aggregator else None,
            mailbox=mailbox,
            **kwargs,
        )

    def worker(
        self, mailbox: _WorkerMailbox, hub: BitfountHub, **kwargs: Any
    ) -> _WorkerSide:
        """Returns the worker side of the ResultsOnly protocol.

        Raises:
            TypeError: If the mailbox is not compatible with the aggregator.
        """
        worker_agg: Optional[_BaseWorkerAggregator] = None
        if self.aggregator is not None:
            if isinstance(self.aggregator, _AggregatorWorkerFactory):
                worker_agg = self.aggregator.worker()
            elif isinstance(self.aggregator, _InterPodAggregatorWorkerFactory):
                if not isinstance(mailbox, _InterPodWorkerMailbox):
                    raise TypeError(
                        "Inter-pod aggregators require an inter-pod worker mailbox."
                    )
                worker_agg = self.aggregator.worker(mailbox=mailbox)
            else:
                raise TypeError(
                    f"Unrecognised aggregator factory ({type(self.aggregator)}); "
                    f"unable to determine how to call .worker() factory method."
                )

        return _WorkerSide(
            algorithm=self.algorithm.worker(hub=hub),
            aggregator=worker_agg,
            mailbox=mailbox,
            **kwargs,
        )
