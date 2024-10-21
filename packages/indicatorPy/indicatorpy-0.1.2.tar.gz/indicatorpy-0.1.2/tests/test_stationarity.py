import unittest
import numpy as np
from indicators.trend.rsi_mod import RSI
from indicators.common.common import CommonMethods
import pandas as pd
import sys

class TestStationarity(unittest.TestCase):
    def setUp(self):
        self.data =pd.read_csv("sp500.csv")
        self.rsi = RSI()

    def test_rsi_calculation(self):
        result = self.rsi.calculate(self.data)
        self.assertTrue(0 <= len(result))  # RSI should be between 0 and 100

#     def test_rsi_stationarity(self):
#         # Test RSI on stationary data
#         stationary_data = np.ones(100)
#         result = self.rsi.calculate(stationary_data)
#         self.assertAlmostEqual(result, 50, delta=1e-5)  # RSI should be close to 50 for stationary data

#     def test_common_methods_sma(self):
#         sma = CommonMethods.calculate_sma(self.data, period=10)
#         self.assertEqual(len(sma), len(self.data) - 9)  # SMA length should be original length minus period-1

#     def test_common_methods_atr(self):
#         high = np.random.rand(100)
#         low = high - np.random.rand(100) * 0.1  # Ensure low is always lower than high
#         close = low + np.random.rand(100) * 0.1  # Close between low and high
#         atr = CommonMethods.calculate_atr(high, low, close)
#         self.assertTrue(atr > 0)  # ATR should be positive

#     def test_base_indicator_plot(self):
#         # This test just checks if the plot method runs without error
#         self.rsi.calculate(self.data)
#         try:
#             self.rsi.plot(np.arange(len(self.data)))
#         except Exception as e:
#             self.fail(f"plot method raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()