import numpy as np
from ..base_indicator import BaseIndicator

      
class RSI(BaseIndicator):
      def __init__(self, period = 14):
            super().__init__("RSI")
            self.period = period

      def calculate(self,data):
            n = self.period

            if len(data.columns) > 1:
                  prices = data['close']
            else:
                  prices = data
                  
            upsum = dnsum = 0.0000000000001
            deltas = np.diff(prices)
            seed = deltas[:n+1]
            up = seed[seed >= 0].sum()/n
            down = -seed[seed < 0].sum()/n
            rsi = np.zeros_like(prices)
            for i in range(n, len(prices)):
                  delta = deltas[i-1]

                  if delta > 0:
                        upsum = ((n-1)*up + delta)/n
                        dnsum *= (n-1)/n

                  else:
                        dnsum = ((n-1)*down-delta)/n
                        upsum *= (n-1)/n

                  rsi[i] = (100 * (upsum/(upsum+dnsum))) - 50 
                  # subtract50 to get the values at 0 in attempt to achieve stationarity
                  if n == 2:
                        rsi[i] = -10.0 * np.log(2.0/(1+0.00999*(2*rsi[i] - 100)) -1 )

            return rsi
