#  Futu Algo: Algorithmic High-Frequency Trading Framework
#  Copyright (c)  billpwchan - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021

import unittest

import pandas as pd

from strategies.Short_Term_Band import ShortTermBand


class StrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.stock_code = 'HK.09988'
        self.complete_data = pd.read_csv('./test/test_data/test_data.csv', index_col=None)
        self.input_data = self.complete_data.iloc[:100, :]
        self.test_data = self.complete_data.iloc[100:, :]
        self.strategy = ShortTermBand({self.stock_code: self.input_data}, observation=100)

    def test_buy(self):
        for index, row in self.test_data.iterrows():
            latest_data = row.to_frame().transpose()
            latest_data.reset_index(drop=True, inplace=True)
            self.strategy.parse_data(latest_data=latest_data)
            self.strategy.buy(self.stock_code)
        self.assertEqual(True, True)

    def test_sell(self):
        for index, row in self.test_data.iterrows():
            latest_data = row.to_frame().transpose()
            latest_data.reset_index(drop=True, inplace=True)
            self.strategy.parse_data(latest_data=latest_data)
            self.strategy.sell(self.stock_code)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()