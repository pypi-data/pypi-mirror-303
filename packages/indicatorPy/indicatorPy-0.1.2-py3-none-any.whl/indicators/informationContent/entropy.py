import numpy as np
def entropy(x): # tested for correctness
      #n - number of datapoints, x = daily close value of datapoints
      x = x[168:]
      n = len(x)
      if n >= 10000:
            nbins = 20
      elif n >= 1000:
            nbins = 10
      elif n >= 100:
            nbins = 5
      else:
            nbins = 3

      counts = [0]*nbins
      for i in range(nbins):
            counts[i] = 0
      
      xmin = min(x)
      xmax = max(x)

      factor = (nbins - 1.e-10)/(xmax - xmin + 1.e-60)

      for i in range(n):
            k = int(factor * (x[i] - xmin))
            counts[k] += 1

      ent_sum = 0.0
      for i in range(nbins):
            if counts[i] > 0:
                  p = float(counts[i]/float(n))
                  ent_sum -= p*np.log(p)

      return ent_sum/np.log(float(nbins))

