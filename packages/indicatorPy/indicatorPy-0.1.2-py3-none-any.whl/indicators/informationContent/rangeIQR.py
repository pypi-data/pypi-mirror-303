import numpy as np
def rangeInterQuartileRangeRatio(x):
      # n - number of cases in x
      # x - indicator values
      #this is just range by IQR, do it later
      x = x[168:]
      mean = np.mean(x)
      q75, q25 = np.percentile(x, [75 ,25])
      iqr = q75 - q25
      return mean/iqr
      
