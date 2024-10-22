# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

import pandas as pd
import pytest

from al360_taiutils.exceptions import SystemErrorException
from al360_trustworthyai.al360_tai_insights import AL360_TAIInsights


class TestRAIInsightsGetFeatureRanges:
    def test_get_feature_range(self):
        data = {'Category': ['A', 'B', 'C', None, 'D'],
                'Numerical': [10, 20, None, 40, 50]}

        df = pd.DataFrame(data)

        feature_ranges = AL360_TAIInsights._get_feature_ranges(
            df, ['Category'], ['Category', 'Numerical'])
        assert len(feature_ranges) == 2
        assert 'Category' == feature_ranges[0]['column_name']
        assert 'Numerical' == feature_ranges[1]['column_name']

    def test_invalid_float_cast_raises_value_error(self):
        data = {'col1': ['A', 'B', 'C', '50']}

        df = pd.DataFrame(data)

        with pytest.raises(SystemErrorException,
                           match='Unable to convert min or max value'):
            AL360_TAIInsights._get_feature_ranges(df, [], ['col1'])
