# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

"""Implementation of Model Analysis API."""

# ModelTask is only imported for backwards compatibility.
from al360_taiutils.models import ModelTask
from al360_trustworthyai.al360_tai_insights.al360_tai_insights import AL360_TAIInsights

__all__ = ['ModelTask', 'AL360_TAIInsights']
