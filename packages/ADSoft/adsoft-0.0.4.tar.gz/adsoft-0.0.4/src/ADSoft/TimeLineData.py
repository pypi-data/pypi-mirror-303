import pandas as pd
import numpy as np


class TimeLineData:
    def __init__(self):
        self.time_labels = None
        self.x_points = None
        self.y_values = None
        self.time_series = None

    def prep(self, df: pd.DataFrame, time_col: str = None, value_col: str = None) -> \
            (list, np.int64, np.float64, pd.tseries):
        if time_col is not None:
            if time_col == 'index':
                self.time_labels = df.index.strftime('%Y-%m-%d %H:%M:%S').tolist()
            else:
                self.time_labels = df[time_col].values.tolist()
            self.x_points = np.arange(df.shape[0] + 1)
        if value_col is not None:
            self.y_values = df[value_col].values
            self.time_series = df[value_col]
        return self.time_labels, self.x_points, self.y_values, self.time_series
    #
    # def time_labels(self, time_col: str) -> list:
    #
    #     return df.time_col.values.tolist()
    #
    # def x_points(self) -> np.int64:
    #
    #     return np.arrange(df.shape[0]+1)
    #
    # def y_values(self, col_name: str) -> np.float64:
    #
    #     return df[col_name].values
    #
    # def df_series(self, col_name: str) -> pd.tseries:
    #     return df.col_name
