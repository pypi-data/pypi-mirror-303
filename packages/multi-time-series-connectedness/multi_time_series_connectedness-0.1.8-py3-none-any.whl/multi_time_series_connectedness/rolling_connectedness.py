from multi_time_series_connectedness.connectedness import Connectedness
import pandas as pd
import pickle
import sys
import os


class RollingConnectedness:
    def __init__(self, data, max_lag, data_periods):
        self.data = data
        self.max_lag = max_lag
        self.data_periods = data_periods
        self.name = [col for col in data.columns if col != 'time'] + ['all']

        # save the calculated connectedness
        self.split_data = {}
        self.rolling_connectedness = None
        self.accuracy_list = None

    def divide_timeseries_volatilities(self):
        if (len(self.data) < self.data_periods):
            print("There is not enough data for the first connectedness")
            sys.exit()
        self.data = self.data.reset_index(drop=True)
        num_rows = self.data.shape[0]
        for i in range(num_rows - self.data_periods):
            subset_df = self.data.iloc[i:(i+self.data_periods)]
            self.split_data[int(subset_df.iloc[-1]['time'])] = subset_df

    def calculate(self, store_result_at, callback_after_one_connectedness=None):
        self.divide_timeseries_volatilities()
        restructured_connectedness_timeseries = pd.DataFrame()
        for key, data in self.split_data.items():
            start_date = data["time"].iloc[0]
            end_date = data["time"].iloc[self.data_periods-1]
            period = f"{start_date} ~ {end_date}"
            print("calculate connectedness for period, %s with data between %s"
                  % (end_date, period))

            conn = Connectedness(data)
            conn.calculate_full_connectedness()
            conn.rename_table(self.name)
            conn.flatten_connectedness()

            restructured_connectedness = conn.restructure_connectedness
            restructured_connectedness['period'] = key
            restructured_connectedness.set_index('period', inplace=True)
            if callback_after_one_connectedness:
                callback_after_one_connectedness(restructured_connectedness)
            restructured_connectedness_timeseries = pd.concat(
                [restructured_connectedness_timeseries, restructured_connectedness], 
                ignore_index=False
            )
        restructured_connectedness_timeseries['forecast_at'] = restructured_connectedness_timeseries.index.to_series().shift(-conn.forecast_at_next_period)
        print(restructured_connectedness_timeseries)
        self.rolling_connectedness = restructured_connectedness_timeseries

        directory = os.path.dirname(store_result_at)
        os.makedirs(directory, exist_ok=True)
        with open(store_result_at, 'wb') as f:
            pickle.dump(self.rolling_connectedness, f)

    def plot_rolling():
        pass
