# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

"""Defines the ModelAnalysis class."""

import warnings
from typing import Any, List, Optional

import numpy as np
import pandas as pd

from al360_trustworthyai.feature_metadata import FeatureMetadata
from al360_trustworthyai.managers.causal_manager import CausalManager
from al360_trustworthyai.managers.counterfactual_manager import CounterfactualManager
from al360_trustworthyai.managers.error_analysis_manager import ErrorAnalysisManager
from al360_trustworthyai.managers.explainer_manager import ExplainerManager
from al360_trustworthyai.al360_tai_insights import AL360_TAIInsights


class ModelAnalysis(object):

    """Defines the top-level Model Analysis API.
    Use ModelAnalysis to analyze errors, explain the most important
    features, compute counterfactuals and run causal analysis in a
    single API.
    """

    def __init__(self, model: Any, train: pd.DataFrame, test: pd.DataFrame,
                 target_column: str, task_type: str,
                 categorical_features: Optional[List[str]] = None,
                 train_labels: Optional[np.ndarray] = None,
                 serializer: Optional[Any] = None,
                 maximum_rows_for_test: int = 5000,
                 feature_metadata: Optional[FeatureMetadata] = None):
        """Creates a ModelAnalysis object.

        :param model: The model to compute RAI insights for.
            A model that implements sklearn.predict or sklearn.predict_proba
            or function that accepts a 2d ndarray.
        :type model: object
        :param train: The training dataset including the label column.
        :type train: pandas.DataFrame
        :param test: The test dataset including the label column.
        :type test: pandas.DataFrame
        :param target_column: The name of the label column.
        :type target_column: str
        :param task_type: The task to run, can be `classification` or
            `regression`.
        :type task_type: str
        :param categorical_features: The categorical feature names.
        :type categorical_features: list[str]
        :param train_labels: The class labels in the training dataset
        :type train_labels: numpy.ndarray
        :param serializer: Picklable custom serializer with save and load
            methods defined for model that is not serializable. The save
            method returns a dictionary state and load method returns the
            model.
        :type serializer: object
        :param maximum_rows_for_test: Limit on size of test data
            (for performance reasons)
        :type maximum_rows_for_test: int
        :param feature_metadata: Feature metadata for the train/test
                                 dataset to identify different kinds
                                 of features in the dataset.
        :type feature_metadata: FeatureMetadata
        """
        warnings.warn(
            "MODULE-DEPRECATION-WARNING: ModelAnalysis in al360_trustworthyai "
            "package is deprecated. Please use AL360_TAIInsights instead.",
            DeprecationWarning)
        self.al360_tai_insights = AL360_TAIInsights(
            model,
            train,
            test,
            target_column,
            task_type,
            categorical_features=categorical_features,
            classes=train_labels,
            serializer=serializer,
            maximum_rows_for_test=maximum_rows_for_test,
            feature_metadata=feature_metadata)
        self.model = self.al360_tai_insights.model
        self.train = self.al360_tai_insights.train
        self.test = self.al360_tai_insights.test
        self.target_column = self.al360_tai_insights.target_column
        self.task_type = self.al360_tai_insights.task_type
        self.categorical_features = self.al360_tai_insights.categorical_features
        self._feature_metadata = feature_metadata

    @property
    def causal(self) -> CausalManager:
        """Get the causal manager.
        :return: The causal manager.
        :rtype: CausalManager
        """
        return self.al360_tai_insights.causal

    @property
    def counterfactual(self) -> CounterfactualManager:
        """Get the counterfactual manager.
        :return: The counterfactual manager.
        :rtype: CounterfactualManager
        """
        return self.al360_tai_insights.counterfactual

    @property
    def error_analysis(self) -> ErrorAnalysisManager:
        """Get the error analysis manager.
        :return: The error analysis manager.
        :rtype: ErrorAnalysisManager
        """
        return self.al360_tai_insights.error_analysis

    @property
    def explainer(self) -> ExplainerManager:
        """Get the explainer manager.
        :return: The explainer manager.
        :rtype: ExplainerManager
        """
        return self.al360_tai_insights.explainer

    def compute(self):
        """Calls compute on each of the managers."""
        self.al360_tai_insights.compute()

    def list(self):
        """List information about each of the managers.
        :return: Information about each of the managers.
        :rtype: dict
        """
        return self.al360_tai_insights.list()

    def get(self):
        """List information about each of the managers.

        :return: Information about each of the managers.
        :rtype: dict
        """
        return self.al360_tai_insights.get()

    def get_data(self):
        """Get all data as ModelAnalysisData object

        :return: Model Analysis Data
        :rtype: ModelAnalysisData
        """
        return self.al360_tai_insights.get_data()

    def save(self, path):
        """Save the ModelAnalysis to the given path.
        :param path: The directory path to save the ModelAnalysis to.
        :type path: str
        """
        self.al360_tai_insights.save(path)

    @staticmethod
    def load(path):
        """Load the ModelAnalysis from the given path.
        :param path: The directory path to load the ModelAnalysis from.
        :type path: str
        :return: The ModelAnalysis object after loading.
        :rtype: ModelAnalysis
        """
        # create the ModelAnalysis without any properties using the __new__
        # function, similar to pickle
        inst = ModelAnalysis.__new__(ModelAnalysis)
        inst.al360_tai_insights = AL360_TAIInsights.load(path)
        inst.model = inst.al360_tai_insights.model
        inst.train = inst.al360_tai_insights.train
        inst.test = inst.al360_tai_insights.test
        inst.target_column = inst.al360_tai_insights.target_column
        inst.task_type = inst.al360_tai_insights.task_type
        inst.categorical_features = inst.al360_tai_insights.categorical_features
        inst._feature_metadata = inst.al360_tai_insights._feature_metadata
        return inst
