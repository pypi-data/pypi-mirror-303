#!/usr/bin/env python3
import pandas as pd


class WeightedAverage(object):

    def __init__(self, df: pd.DataFrame, num_obs: int) -> None:
        if len(df.columns) != 4:
            raise ValueError("Expected 4 columns, got {}".format(df.columns))
        self.df: pd.DataFrame = df
        self.column_names: list = df.columns.tolist()
        self.values: pd.Series = df[df.columns[2]]
        self.std_devs: pd.Series = df[df.columns[3]]
        self.num_obs: int = num_obs

    def get_weighted_average(self) -> pd.DataFrame:
        """Return weighted average and standard deviation."""
        experiment_ids: str = self.column_names[0]
        values: str = self.column_names[2]
        std_dev: str = self.column_names[3]
        # Group by experiment IDs to compute the weighted statistics and
        # drop all rows that contain NaNs in the output. The 'include_groups' option doesn't exist
        # in Pandas version prior to 2.0.0.
        if pd.__version__ < '2.0.0':
            grouped_stats = (
                self.df.groupby(experiment_ids)
                .apply(
                    lambda x: pd.Series(
                        self.weighted_stats(x[values], x[std_dev], self.num_obs)
                    )
                )
                .reset_index()
                .dropna()
            )
        else:
            grouped_stats = (
                self.df.groupby(experiment_ids)
                .apply(
                    lambda x: pd.Series(
                        self.weighted_stats(x[values], x[std_dev], self.num_obs)
                    ),
                    include_groups=False
                )
                .reset_index()
                .dropna()
            )
        grouped_stats.columns = [
            experiment_ids,
            "weighted_average_value",
            "weighted_std_dev",
        ]
        return grouped_stats

    @staticmethod
    def weighted_stats(values, std_devs, n):
        """Return weighted average and standard deviation from an average of averages."""
        weights = [n / (std**2) for std in std_devs]
        weighted_avg = sum(
            value * weight for value, weight in zip(values, weights)
        ) / sum(weights)

        # Calculate the weighted variance.
        weighted_variance = sum(
            weight * (value - weighted_avg) ** 2
            for value, weight in zip(values, weights)
        ) / sum(weights)

        # Calculate the weighted standard deviation.
        weighted_std_dev = weighted_variance**0.5

        return weighted_avg, weighted_std_dev

    # def _get_weights(self):
    #     return [self.num_obs / (std ** 2) for std in self.std_devs]
    #
    # def _get_weighted_average(self):
    #     weights = self._get_weights()
    #     return sum(value * weight for value, weight in zip(self.values, weights)) / sum(weights)
    #
    # def _get_weighted_variance(self):
    #     """Calculate the weighted variance."""
    #     weighted_avg = self._get_weights()
    #     weights = self._get_weights()
    #     return sum(weight * (value - weighted_avg) ** 2 for value, weight in zip(self.values, weights)) / sum(weights)
    #
    # def _get_weighted_standard_deviation(self):
    #     weighted_variance = self._get_weighted_variance()
    #     return weighted_variance ** 0.5
