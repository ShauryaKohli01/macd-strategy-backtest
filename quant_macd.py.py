import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch stock data
ticker = 'PG'
df = yf.download(ticker, start='2023-07-01', end='2025-07-01')

# Calculate MACD and Signal Line
df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = df['EMA12'] - df['EMA26']
df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

# Generate Trading Signals
df['positions'] = np.where(df['MACD'] > df['Signal'], 1, 0)
df['positions'] = df['positions'].shift(1).fillna(0)

# Strategy Returns
df['returns'] = df['Close'].pct_change()
df['strategy_returns'] = df['returns'] * df['positions']

# Cumulative Performance
df['macd_cum_returns'] = (1 + df['strategy_returns']).cumprod() * 10000
df['buy_hold_cum_returns'] = (1 + df['returns']).cumprod() * 10000

# PLOT 1: Equity Curve

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['macd_cum_returns'], label='MACD Strategy', color='blue')
plt.plot(df.index, df['buy_hold_cum_returns'], label='Buy & Hold', color='orange')
plt.title('Equity Curve vs Buy & Hold')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# PLOT 2: MACD Buy/Sell Signals

buy_signals = df[(df['positions'] == 1) & (df['positions'].shift(1) == 0)]
sell_signals = df[(df['positions'] == 0) & (df['positions'].shift(1) == 1)]

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', color='grey', alpha=0.6)
plt.plot(df['MACD'], label='MACD Line', color='blue')
plt.plot(df['Signal'], label='Signal Line', color='orange')
plt.scatter(buy_signals.index, buy_signals['MACD'], marker='^', color='green', label='Buy Signal', s=100)
plt.scatter(sell_signals.index, sell_signals['MACD'], marker='v', color='red', label='Sell Signal', s=100)
plt.title('MACD Buy & Sell Signals')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
