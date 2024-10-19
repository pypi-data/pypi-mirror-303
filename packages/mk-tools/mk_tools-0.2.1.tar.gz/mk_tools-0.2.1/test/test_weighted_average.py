#!/usr/bin/env python3
import pandas as pd
import unittest
from src.weighted_average import WeightedAverage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        data = {
            'experiment_id': [1, 1, 1, 2, 2, 3, 3, 3, 3],
            'repeat_id': [1, 2, 3, 1, 2, 1, 2, 3, 4],
            'value': [10, 15, 10, 20, 25, 30, 35, 40, 45],
            'std_dev': [1.0, 1.5, 1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
        }

        self.df = pd.DataFrame(data)
        self.NUMBER_OF_OBSERVATIONS = 100

        expected = {
            'experiment_id': [1, 2, 3],
            'weighted_average_value': [10.909091, 21.951220, 35.823210],
            'weighted_std_dev': [1.928473, 2.439024, 5.457206]
        }
        self.df_expected = pd.DataFrame(data=expected)

    def tearDown(self):
        del self.df
        del self.NUMBER_OF_OBSERVATIONS

    def test_get_weighted_average(self):
        weighted_avg = WeightedAverage(self.df, self.NUMBER_OF_OBSERVATIONS)
        observed: pd.DataFrame = weighted_avg.get_weighted_average()
        pd.testing.assert_frame_equal(observed, self.df_expected)


if __name__ == '__main__':
    unittest.main()
