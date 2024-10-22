"""Algorithm to evaluate a model on remote data."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, ClassVar, Optional, Union, cast

from marshmallow import fields
import numpy as np
import pandas as pd

from bitfount.data.datasources.utils import ORIGINAL_FILENAME_METADATA_COLUMN
from bitfount.federated.algorithms.model_algorithms.base import (
    _BaseModelAlgorithmFactory,
    _BaseModellerModelAlgorithm,
    _BaseWorkerModelAlgorithm,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.hub.api import BitfountHub
from bitfount.types import PredictReturnType, _SerializedWeights
from bitfount.utils import delegates

if TYPE_CHECKING:
    from bitfount.types import (
        T_FIELDS_DICT,
        DistributedModelProtocol,
        _DistributedModelTypeOrReference,
    )

logger = _get_federated_logger(__name__)


class _ModellerSide(_BaseModellerModelAlgorithm):
    """Modeller side of the ModelInference algorithm."""

    def run(
        self, results: Mapping[str, Union[list[np.ndarray], pd.DataFrame]]
    ) -> dict[str, Union[list[np.ndarray], pd.DataFrame]]:
        """Simply returns predictions."""
        return dict(results)


class _WorkerSide(_BaseWorkerModelAlgorithm):
    """Worker side of the ModelInference algorithm."""

    def __init__(
        self,
        *,
        model: DistributedModelProtocol,
        class_outputs: Optional[list[str]] = None,
        **kwargs: Any,
    ):
        super().__init__(model=model, **kwargs)
        self.class_outputs = class_outputs

    def run(
        self,
        model_params: Optional[_SerializedWeights] = None,
        return_data_keys: bool = False,
        **kwargs: Any,
    ) -> Union[PredictReturnType, pd.DataFrame]:
        """Runs inference and returns results."""
        if model_params is not None:
            self.update_params(model_params)

        # mypy: as we are in the worker-side of the algorithm, we know that
        # _predict_local() will be the actual underlying call, and that that returns
        # PredictReturnType
        predict_output: PredictReturnType = cast(
            PredictReturnType, self.model.predict(self.datasource)
        )

        # TODO: [BIT-3620] revisit outputs after this ticket is done.
        # At the moment, the pytorch built-in models return the
        # predictions based on the number of frames, which
        # should not be the case. I.e. a file that has 2 frames
        # will return a list of two values adding up to 1 as predictions,
        # whereas a file that has 3 frames returns a list of three values
        # adding up to 1. This is not the desired behaviour, and added
        # to do here as this algo might need updating after we handle that.
        if self.class_outputs:
            df: Optional[pd.DataFrame] = None

            if isinstance(predict_output.preds, pd.DataFrame):
                df = predict_output.preds

                if not set(self.class_outputs).issubset(df.columns):
                    logger.warning(
                        "Class outputs provided do not match"
                        " the model prediction output."
                        f" You provided a list of {len(self.class_outputs)}, and"
                        f" this differs from the output dataframe."
                        " Outputting predictions as-is."
                    )
            else:  # preds is list[np.ndarray]
                # If all the arrays have the same length, we can make a dataframe
                if all(
                    prediction.shape[0] == len(self.class_outputs)
                    for prediction in predict_output.preds
                ):
                    df = pd.DataFrame(
                        data=predict_output.preds, columns=self.class_outputs
                    )

                else:
                    logger.warning(
                        "Class outputs provided do not match"
                        " the model prediction output."
                        f" You provided a list of {len(self.class_outputs)}, and"
                        f" not all the model predictions are of the same shape."
                        " Outputting predictions as a list of numpy arrays."
                    )

            if df is not None:  # i.e. we've created a dataframe
                # If keys are provided and requested, add them to the dataframe as a
                # new column.
                if predict_output.keys is not None and return_data_keys:
                    df[ORIGINAL_FILENAME_METADATA_COLUMN] = predict_output.keys

                return df

        # We will fall back to this if either there aren't self.class_outputs OR if
        # we couldn't create a dataframe as requested above.
        if not return_data_keys:
            # If data keys have not been requested, null out their potential entry
            predict_output.keys = None

        return predict_output


@delegates()
class ModelInference(_BaseModelAlgorithmFactory):
    """Algorithm for running inference on a model and returning the predictions.

    :::danger

    This algorithm could potentially return the data unfiltered so should only be used
    when the other party is trusted.

    :::

    Args:
        model: The model to infer on remote data.
        class_outputs: A list of strings corresponding to prediction outputs.
            If provided, the model will return a dataframe of results with the
            class outputs list elements as columns. Defaults to None.

    Attributes:
        model: The model to infer on remote data.
        class_outputs: A list of strings corresponding to prediction outputs.
            If provided, the model will return a dataframe of results with the
            class outputs list elements as columns. Defaults to None.
    """

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "class_outputs": fields.List(fields.String(), allow_none=True)
    }

    def __init__(
        self,
        *,
        model: _DistributedModelTypeOrReference,
        class_outputs: Optional[list[str]] = None,
        **kwargs: Any,
    ):
        self.class_outputs = class_outputs
        super().__init__(model=model, **kwargs)

    def modeller(self, **kwargs: Any) -> _ModellerSide:
        """Returns the modeller side of the ModelInference algorithm."""
        model = self._get_model_from_reference_and_upload_weights(
            project_id=self.project_id
        )
        return _ModellerSide(model=model, **kwargs)

    def worker(self, hub: BitfountHub, **kwargs: Any) -> _WorkerSide:
        """Returns the worker side of the ModelInference algorithm.

        Args:
            hub: `BitfountHub` object to use for communication with the hub.
            **kwargs: Additional keyword arguments to pass to the worker side.

        Returns:
            Worker side of the ModelInference algorithm.
        """
        model = self._get_model_from_reference_and_download_weights(
            hub=hub, project_id=self.project_id
        )
        return _WorkerSide(model=model, class_outputs=self.class_outputs, **kwargs)
