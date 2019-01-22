import matplotlib.pyplot as pyplot
import numpy as np
SPY = pdr.get_data_yahoo("SPY", start = "1950-01-01", end="2019-01-01")
SPY.plot(fontsize = 12)
plt.show()
SPY_Close = SPY['Close']
SPY_Close.plot(fontsize = 10)
plt.show()
def plot_data (SPY, title = "Stock Prices"):
  ax = SPY.plot(fontsize = 12)
  ax.set_xlabel("Date")
  ax.set_ylabel("Price")
  plt.show()
plot_data(SPY["Low"])
plot_data(SPY["Volume"])



def compute_daily_returns(B);
  DR = B.copy()
  DR[1:] = (B[1:]/B[:-1].values)-1
  DR.ix[0, :] = 0
  return DR
daily_returns = compute_daily_returns(OD)