# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

import json
import random
from unittest import mock

import pytest
from tests.common_utils import (RandomForecastingModel,
                                create_tiny_forecasting_dataset)

from al360_trustworthyai import FeatureMetadata, AL360_TAIInsights

RAI_INSIGHTS_DIR_NAME = "al360_tai_insights_test_served_model"


# create a pytest fixture
@pytest.fixture(scope="session")
def al360_tai_forecasting_insights_for_served_model():
    X_train, X_test, y_train, y_test = create_tiny_forecasting_dataset()
    train = X_train.copy()
    train["target"] = y_train
    test = X_test.copy()
    test["target"] = y_test
    model = RandomForecastingModel()

    # create RAI Insights and save it
    al360_tai_insights = AL360_TAIInsights(
        model=model,
        train=train,
        test=test,
        target_column="target",
        task_type='forecasting',
        feature_metadata=FeatureMetadata(
            datetime_features=['time'],
            time_series_id_features=['id']
        ),
        forecasting_enabled=True)
    al360_tai_insights.save(RAI_INSIGHTS_DIR_NAME)


@mock.patch("requests.post")
@mock.patch.dict("os.environ", {"RAI_MODEL_SERVING_PORT": "5432"})
def test_served_model(
        mock_post,
        al360_tai_forecasting_insights_for_served_model):
    X_train, X_test, _, _ = create_tiny_forecasting_dataset()

    mock_post.return_value = mock.Mock(
        status_code=200,
        content=json.dumps({
            "predictions": [random.random() for _ in range(len(X_train))]
        })
    )

    al360_tai_insights = AL360_TAIInsights.load(RAI_INSIGHTS_DIR_NAME)
    forecasts = al360_tai_insights.model.forecast(X_test)
    assert len(forecasts) == len(X_test)
    assert mock_post.call_count == 1
