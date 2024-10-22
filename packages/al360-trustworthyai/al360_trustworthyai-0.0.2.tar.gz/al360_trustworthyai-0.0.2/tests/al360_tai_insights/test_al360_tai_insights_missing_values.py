# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

from enum import Enum

import numpy as np
import pandas as pd
import pytest
from ml_wrappers.model.predictions_wrapper import \
    PredictionsModelWrapperClassification
from tests.common_utils import create_iris_data

from al360_tai_test_utils.models.sklearn import (
    create_complex_classification_pipeline, create_sklearn_svm_classifier)
from al360_taiutils.exceptions import UserConfigValidationException
from al360_trustworthyai import AL360_TAIInsights
from al360_trustworthyai._internal.constants import ManagerNames
from al360_trustworthyai.feature_metadata import FeatureMetadata

LABELS = 'labels'


class MISSING_VALUE(Enum):
    NO_MISSING_VALUES = 1
    TRAIN_ONLY_MISSING_VALUES = 2
    TEST_ONLY_MISSING_VALUES = 3
    BOTH_TRAIN_TEST_MISSING_VALUES = 4


class TestRAIInsightsMissingValues(object):

    def test_model_does_not_handle_missing_values(self):
        X_train, X_test, y_train, y_test, feature_names, classes = \
            create_iris_data()

        model = create_sklearn_svm_classifier(X_train, y_train)
        X_train.at[1, 'sepal length'] = np.nan
        X_test.at[1, 'sepal length'] = np.nan
        X_train[LABELS] = y_train
        X_test[LABELS] = y_test

        with pytest.raises(
                UserConfigValidationException,
                match='The passed model cannot be '
                      'used for getting predictions via predict'):
            AL360_TAIInsights(model, X_train, X_test,
                        LABELS, task_type="classification")

    @pytest.mark.parametrize('manager_type', [ManagerNames.CAUSAL,
                                              ManagerNames.ERROR_ANALYSIS,
                                              ManagerNames.EXPLAINER,
                                              ManagerNames.COUNTERFACTUAL])
    @pytest.mark.parametrize('categorical_missing_values', [True, False])
    @pytest.mark.parametrize('missing_value_combination', [
        MISSING_VALUE.NO_MISSING_VALUES,
        MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES,
        MISSING_VALUE.TEST_ONLY_MISSING_VALUES,
        MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES
    ])
    @pytest.mark.parametrize('wrapper', [True, False])
    @pytest.mark.skip(
        reason="Seeing failures with PredictionsModelWrapperClassification")
    def test_model_handles_missing_values(
            self, manager_type, adult_data,
            categorical_missing_values,
            missing_value_combination,
            wrapper):

        data_train, data_test, y_train, y_test, categorical_features, \
            continuous_features, target_name, classes, \
            feature_columns, feature_range_keys = \
            adult_data

        data_train_copy = data_train.copy()
        data_test_copy = data_test.copy()

        if missing_value_combination == \
            MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES or \
            missing_value_combination == \
                MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
            data_train_copy.loc[data_train_copy['age'] > 30, 'age'] = np.nan

        if missing_value_combination == \
            MISSING_VALUE.TEST_ONLY_MISSING_VALUES or \
            missing_value_combination == \
                MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
            data_test_copy.loc[data_test_copy['age'] > 30, 'age'] = np.nan

        if categorical_missing_values:
            if missing_value_combination == \
                MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES or \
                missing_value_combination == \
                    MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
                data_train_copy.loc[
                    data_train_copy[
                        'workclass'] == 'Private', 'workclass'] = np.nan

            if missing_value_combination == \
                MISSING_VALUE.TEST_ONLY_MISSING_VALUES or \
                missing_value_combination == \
                    MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
                data_test_copy.loc[
                    data_test_copy[
                        'workclass'] == 'Private', 'workclass'] = np.nan

        X_train = data_train_copy.drop([target_name], axis=1)
        X_test = data_test_copy.drop([target_name], axis=1)

        model = create_complex_classification_pipeline(
            X_train, y_train, continuous_features,
            categorical_features)

        if wrapper:
            all_data = pd.concat(
                [X_test, X_train])
            model_predict_output = model.predict(all_data)
            model_predict_proba_output = model.predict_proba(all_data)
            model_wrapper = PredictionsModelWrapperClassification(
                all_data,
                model_predict_output,
                model_predict_proba_output,
                should_construct_pandas_query=False)
            model = model_wrapper

        al360_tai_insights = AL360_TAIInsights(
            model, data_train_copy, data_test_copy, target_name,
            task_type="classification",
            feature_metadata=FeatureMetadata(
                categorical_features=categorical_features))

        if manager_type == ManagerNames.EXPLAINER:
            if not categorical_missing_values:
                al360_tai_insights.explainer.add()
                al360_tai_insights.compute()
                assert len(al360_tai_insights.explainer.get()) == 1
            else:
                if missing_value_combination != \
                        MISSING_VALUE.NO_MISSING_VALUES:
                    if missing_value_combination == \
                        MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES or \
                        missing_value_combination == \
                            MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
                        error_message = \
                            "Categorical features workclass cannot have " + \
                            "missing values for computing explanations. " + \
                            "Please check your training data."
                    else:
                        error_message = \
                            "Categorical features workclass cannot have " + \
                            "missing values for computing explanations. " + \
                            "Please check your test data."
                    with pytest.raises(
                            UserConfigValidationException,
                            match=error_message):
                        al360_tai_insights.explainer.add()
                else:
                    al360_tai_insights.explainer.add()
                    al360_tai_insights.compute()
                    assert len(al360_tai_insights.explainer.get()) == 1
        elif manager_type == ManagerNames.ERROR_ANALYSIS:
            al360_tai_insights.error_analysis.add()
            al360_tai_insights.compute()
            assert len(al360_tai_insights.error_analysis.get()) == 1
        elif manager_type == ManagerNames.COUNTERFACTUAL:
            if not wrapper:
                if missing_value_combination != \
                        MISSING_VALUE.NO_MISSING_VALUES:
                    if missing_value_combination == \
                        MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES or \
                        missing_value_combination == \
                            MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
                        error_message = \
                            'Missing values are not allowed in ' + \
                            'the train dataset while computing ' + \
                            'counterfactuals.'
                    else:
                        error_message = \
                            'Missing values are not allowed in ' + \
                            'the test dataset while computing ' + \
                            'counterfactuals.'
                    with pytest.raises(
                            UserConfigValidationException,
                            match=error_message):
                        al360_tai_insights.counterfactual.add(
                            total_CFs=10, desired_class="opposite")
                else:
                    al360_tai_insights.counterfactual.add(
                        total_CFs=10, desired_class="opposite")
                    al360_tai_insights.compute()
                    assert len(al360_tai_insights.counterfactual.get()) == 1
        elif manager_type == ManagerNames.CAUSAL:
            if missing_value_combination != \
                    MISSING_VALUE.NO_MISSING_VALUES:
                if missing_value_combination == \
                    MISSING_VALUE.TRAIN_ONLY_MISSING_VALUES or \
                    missing_value_combination == \
                        MISSING_VALUE.BOTH_TRAIN_TEST_MISSING_VALUES:
                    error_message = \
                        'Missing values are not allowed in the ' + \
                        'train dataset while computing causal effects.'
                else:
                    error_message = \
                        'Missing values are not allowed in the ' + \
                        'test dataset while computing causal effects.'
                with pytest.raises(
                        UserConfigValidationException, match=error_message):
                    al360_tai_insights.causal.add(treatment_features=['age'])
            else:
                al360_tai_insights.causal.add(treatment_features=['age'])
                al360_tai_insights.compute()
                assert len(al360_tai_insights.causal.get()) == 1
