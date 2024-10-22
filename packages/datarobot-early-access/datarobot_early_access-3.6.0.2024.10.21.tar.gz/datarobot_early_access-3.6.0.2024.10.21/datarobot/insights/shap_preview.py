#
# Copyright 2024 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from typing import Any, cast, Dict, List, Optional

import trafaret as t
from typing_extensions import Self

from datarobot.enums import INSIGHTS_SOURCES
from datarobot.insights.base import BaseInsight


class ShapPreview(BaseInsight):
    """Class for SHAP Preview calculations. Use the standard methods of BaseInsight to compute and
    retrieve SHAP matrices:
    * compute: submit a request to compute a SHAP preview, and return immediately
    * create: submit a request to compute a SHAP preview, and wait for it to finish
    * list: retrieve all ShapPreview results for a model, possibly on multiple datasets or data slices.
    """

    SHAP_PREVIEW_VALUE = t.Dict(
        {
            t.Key("feature_rank"): t.Int(),
            t.Key("feature_name"): t.String(),
            t.Key("feature_value"): t.String(),
            t.Key("shap_value"): t.Float(),
        }
    ).ignore_extra("*")

    SHAP_PREVIEW_ROW = t.Dict(
        {
            t.Key("row_index"): t.Int(),
            t.Key("total_preview_features"): t.Int(),
            t.Key("prediction_value"): t.Float(),
            t.Key("preview_values"): t.List(SHAP_PREVIEW_VALUE),
        }
    )

    INSIGHT_NAME = "shapPreview"
    INSIGHT_DATA = {
        t.Key("previews_count"): t.Int(),
        t.Key("previews"): t.List(SHAP_PREVIEW_ROW),
    }

    @property
    def previews(self) -> List[Dict[str, Any]]:
        """SHAP preview values

        Returns
        -------
        preview : List[Dict[str, Any]]
            A list of the ShapPreview values for each row
        """
        return cast(List[Dict[str, Any]], self.data["previews"])

    @property
    def previews_count(self) -> int:
        """Number of shap preview rows

        Returns
        -------
        int
        """
        return cast(int, self.data["previews_count"])

    @classmethod
    def get(
        cls,
        entity_id: str,
        source: str = INSIGHTS_SOURCES.VALIDATION,
        prediction_filter_row_count: Optional[int] = None,
        prediction_filter_percentiles: Optional[int] = None,
        prediction_filter_operand_first: Optional[float] = None,
        prediction_filter_operand_second: Optional[float] = None,
        prediction_filter_operator: Optional[str] = None,
        feature_filter_count: Optional[int] = None,
        feature_filter_name: Optional[str] = None,
        quick_compute: Optional[bool] = None,
        **kwargs: Any,
    ) -> Self:
        """Return the first matching insight based on the entity id and kwargs.

        Parameters
        ----------
        entity_id: str
            ID of the entity to retrieve generated insights.
        source: str
            Source type to use when retrieving the insight.
        prediction_filter_row_count: int, optional
            The maximum number of preview rows to return.
        prediction_filter_percentiles: int, optional
            The number of percentile intervals to select from the total number of rows.
            This field will supersede predictionFilterRowCount if both are present.
        prediction_filter_operand_first: float, optional
            The first operand to apply to filtered predictions.
        prediction_filter_operand_second: float, optional
            The second operand to apply to filtered predictions.
        prediction_filter_operator: str, optional
            The operator to apply to filtered predictions.
        feature_filter_count: int, optional
            The maximum number of features to return for each preview.
        feature_filter_name: str, optional
            The names of specific features to return for each preview.
        quick_compute: bool, optional
            When enabled, limits the rows used from the selected source subset by default.
            When disabled, all rows are used.

        Returns
        -------
        List[Any]
            List of newly or already computed insights.
        """
        query_params = {**kwargs}
        if prediction_filter_row_count is not None:
            query_params["predictionFilterRowCount"] = prediction_filter_row_count
        if prediction_filter_percentiles is not None:
            query_params["predictionFilterPercentiles"] = prediction_filter_percentiles
        if prediction_filter_operand_first is not None:
            query_params["predictionFilterOperandFirst"] = prediction_filter_operand_first
        if prediction_filter_operand_second is not None:
            query_params["predictionFilterOperandSecond"] = prediction_filter_operand_second
        if prediction_filter_operator is not None:
            query_params["predictionFilterOperator"] = prediction_filter_operator
        if feature_filter_count is not None:
            query_params["featureFilterCount"] = feature_filter_count
        if feature_filter_name is not None:
            query_params["featureFilterName"] = feature_filter_name
        if quick_compute is not None:
            query_params["quickCompute"] = quick_compute

        return super().get(entity_id=entity_id, source=source, **query_params)
