# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

"""AL360° Trustworthy AI SDK package."""

# ModelTask is only imported for backwards compatibility
from al360_taiutils.models import ModelTask
from al360_trustworthyai.modelanalysis import ModelAnalysis
from al360_trustworthyai.al360_tai_insights import AL360_TAIInsights

from .__version__ import version
from .feature_metadata import FeatureMetadata

__version__ = version

__all__ = ['ModelAnalysis', 'ModelTask', 'AL360_TAIInsights', 'FeatureMetadata']
