from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

class BaseIndicator(ABC):
    def __init__(self, name):
        self.name = name
        self.result = None

    @abstractmethod
    def calculate(self, data):
        pass

    def plot(self, time_series):
        pass
      #   if self.result is None:
      #       raise ValueError("Calculate the indicator before plotting")
      #   plt.figure(figsize=(10, 6))
      #   plt.plot(time_series, label='Price')
      #   plt.plot(self.result, label=self.name)
      #   plt.legend()
      #   plt.title(f"{self.name} Indicator")
      #   plt.show()