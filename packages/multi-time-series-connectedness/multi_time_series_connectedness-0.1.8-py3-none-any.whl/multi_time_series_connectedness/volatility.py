import pickle
import pandas as pd
import numpy as np
import os
import glob


class Volatility:
    def __init__(self, n=2):
        self.n = n

    def yang_zhang_volatility(self, data, name):
        """
        :param data: a list with Open, High, Low, Close price
        :param name: the name of the volatility column
        :return: A DataFrame with time and volatility data
        """
        # define required variables
        o_c = (data['Open'] / data['Close'].shift(1)).apply(np.log)
        c_o = (data['Close'] / data['Open']).apply(np.log)
        h_o = (data['High'] / data['Open']).apply(np.log)
        l_o = (data['Low'] / data['Open']).apply(np.log)

        # overnight volatility
        vo = o_c.rolling(window=self.n).apply(np.var, raw=True)

        # today(open to close) volatility
        vt = c_o.rolling(window=self.n).apply(np.var, raw=True)

        # rogers-satchell volatility
        rs_fomula = h_o * (h_o - c_o) + l_o * (l_o - c_o)
        rs = rs_fomula.rolling(window=self.n, center=False).sum() * (1.0 / self.n)

        # super parameter
        k = 0.34 / (1 + (self.n + 1) / (self.n - 1))

        # yang-zhang
        result = (vo + k * vt + (1 - k) * rs).apply(np.sqrt)

        result_df = result.to_frame(name=name)

        return pd.concat([data['time'], result_df], axis=1)

    def price_data_to_volatility(self, datasets):
        volatilities = None
        for key, value in datasets.items():
            volatility = self.yang_zhang_volatility(value, key)
            if volatilities is None:
                volatilities = volatility
            else:
                volatilities = volatilities.merge(volatility, on='time', how='outer')

        return volatilities

    # check this one here, use unix timestamp
    def calculate(self, directory, save_path=None, start_at=None, end_at=None):
        datasets = {}
        for filepath in glob.glob(os.path.join(directory, '*.csv')):
            data = pd.read_csv(filepath)
            if start_at is None:
                start_at = data['time'].iloc[0]
            if end_at is None:
                end_at = data['time'].iloc[-1]
            filtered_data = data[(data['time'] >= start_at) & (data['time'] <= end_at)]
            datasets[os.path.basename(filepath)] = filtered_data
        volatilities = self.price_data_to_volatility(datasets)

        with open(save_path, 'wb') as f:
            pickle.dump(volatilities, f)
