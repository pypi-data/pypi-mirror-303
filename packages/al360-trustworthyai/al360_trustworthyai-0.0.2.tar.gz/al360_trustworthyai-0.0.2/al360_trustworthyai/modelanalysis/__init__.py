# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

"""Implementation of Model Analysis API."""

# ModelTask is only imported for backwards compatibility
from al360_taiutils.models import ModelTask
from al360_trustworthyai.modelanalysis.model_analysis import ModelAnalysis

__all__ = ["ModelAnalysis", "ModelTask"]
