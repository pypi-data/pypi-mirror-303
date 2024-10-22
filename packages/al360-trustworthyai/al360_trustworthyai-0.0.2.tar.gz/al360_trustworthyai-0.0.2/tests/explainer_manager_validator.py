# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

import pytest

from al360_taiutils.exceptions import UserConfigValidationException
from al360_taiutils.models import ModelTask
from al360_trustworthyai._internal.constants import ListProperties, ManagerNames

LIGHTGBM_METHOD = 'mimic.lightgbm'


def setup_explainer(al360_tai_insights, add_explainer=True):
    if add_explainer:
        if al360_tai_insights.model is None:
            with pytest.raises(
                    UserConfigValidationException,
                    match='Model is required for model explanations'):
                al360_tai_insights.explainer.add()
            return
        else:
            al360_tai_insights.explainer.add()
        # Validate calling add multiple times prints a warning
        with pytest.warns(
            UserWarning,
            match="DUPLICATE-EXPLAINER-CONFIG: Ignoring. "
                  "Explanation has already been added, "
                  "currently limited to one explainer type."):
            al360_tai_insights.explainer.add()
    al360_tai_insights.explainer.compute()


def validate_explainer(al360_tai_insights, X_train, X_test, classes):
    if al360_tai_insights.model is None:
        return
    explanations = al360_tai_insights.explainer.get()
    assert isinstance(explanations, list)
    assert len(explanations) == 1
    explanation = explanations[0]
    if al360_tai_insights._feature_metadata is not None and \
            al360_tai_insights._feature_metadata.dropped_features is not None:
        num_cols = len(X_train.columns) - 1 - len(
            al360_tai_insights._feature_metadata.dropped_features)
    else:
        num_cols = len(X_train.columns) - 1
    if classes is not None:
        assert len(explanation.local_importance_values) == len(classes)
        assert len(explanation.local_importance_values[0]) == len(X_test)
        assert len(explanation.local_importance_values[0][0]) == num_cols
    else:
        assert len(explanation.local_importance_values) == len(X_test)
        assert len(explanation.local_importance_values[0]) == num_cols

    properties = al360_tai_insights.explainer.list()
    assert properties[ListProperties.MANAGER_TYPE] == ManagerNames.EXPLAINER
    assert 'id' in properties
    assert properties['method'] == LIGHTGBM_METHOD
    if classes is not None:
        assert properties['model_task'] == ModelTask.CLASSIFICATION
    else:
        assert properties['model_task'] == ModelTask.REGRESSION
    assert properties['model_type'] is None
    assert properties['is_raw'] is False
    assert properties['is_engineered'] is False

    # Check the internal state of explainer manager
    assert al360_tai_insights.explainer._is_added
    assert al360_tai_insights.explainer._is_run
