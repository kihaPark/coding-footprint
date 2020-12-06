import numpy as np
import pandas as pd
import rl_const as ct


class DataMan:
    def __init__(self, start=ct.START_DATE, end=ct.END_DATE):
        self.start = start
        self.end = end
        self.csvD = pd.read_csv('data-files/futuresD.csv')
        self.futuresD = self.add_info()
        self.futuresD = self.futuresD[(self.futuresD['date'] >= start) & \
                                      (self.futuresD['date'] <= end)]

    def add_info(self):
        cD = self.csvD.copy()

        cD['open_lastclose_ratio'] = np.zeros(len(cD))
        cD.loc[1:, 'open_lastclose_ratio'] = \
            (cD['f_open'][1:].values - cD['f_close'][:-1].values) / cD['f_close'][:-1].values

        cD['high_close_ratio'] = \
            (cD['f_high'].values - cD['f_close'].values) / cD['f_close'].values
        cD['low_close_ratio'] = \
            (cD['f_low'].values - cD['f_close'].values) / cD['f_close'].values

        cD['close_lastclose_ratio'] = np.zeros(len(cD))
        cD.loc[1:, 'close_lastclose_ratio'] = \
            (cD['f_close'][1:].values - cD['f_close'][:-1].values) / cD['f_close'][:-1].values

        cD['vol_lastvol_ratio'] = np.zeros(len(cD))
        cD.loc[1:, 'vol_lastvol_ratio'] = \
            (cD['f_vol'][1:].values - cD['f_vol'][:-1].values) / \
             cD['f_vol'][:-1].replace(to_replace=0, method='ffill') \
                .replace(to_replace=0, method='bfill').values

        movings = [5, 10, 20]
        for moving in movings:
            cD[f'f_close_ma{moving}'] = cD['f_close'].rolling(moving).mean()
            cD[f'f_vol_ma{moving}'] = cD['f_vol'].rolling(moving).mean()

        for moving in movings:
            cD[f'close_ma{moving}_ratio'] = \
                (cD['f_close'] - cD[f'f_close_ma{moving}']) / cD[f'f_close_ma{moving}']
            cD[f'vol_ma{moving}_ratio'] = \
                (cD['f_vol'] - cD[f'f_vol_ma{moving}']) / cD[f'f_vol_ma{moving}']

        return cD

    def chart_data(self):
        return self.futuresD[ct.CHART_COLS]

    def train_data(self):
        return self.futuresD[ct.TRAIN_COLS]

    def split_data(self):
        return self.futuresD[ct.CHART_COLS], self.futuresD[ct.TRAIN_COLS]


if __name__ == "__main__":
    dm = DataMan()
    trainD = dm.train_data()
    print(type(trainD), trainD.info())
    print(trainD.head())