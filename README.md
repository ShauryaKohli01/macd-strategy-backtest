# MACD Strategy Backtest

This project implements a simple backtesting model using the **MACD (Moving Average Convergence Divergence)** indicator to generate buy/sell signals and compares it with a traditional **Buy & Hold** strategy.

<img width="1190" height="594" alt="image" src="https://github.com/user-attachments/assets/5d7340e5-f34e-4d53-bd61-a589463a3b6c" />

<img width="1198" height="596" alt="image" src="https://github.com/user-attachments/assets/81fdc6a7-c90a-412d-b680-fd89d5949e2c" />


# How It Works

The MACD strategy tracks the relationship between two exponential moving averages:

- MACD Line** = 12-day EMA − 26-day EMA  
- Signal Line** = 9-day EMA of MACD Line  

# Strategy Logic:

- Buy Signal**: When MACD Line crosses **above** Signal Line  
- Sell Signal**: When MACD Line crosses **below** Signal Line  

This helps identify **momentum shifts** in price, especially useful in **range-bound or moderately trending markets**.

# Performance Comparison


The script plots the equity curve for:

📘 MACD Strategy (IN BLUE)

🟠 Buy & Hold ( IN ORANGE)

This allows users to evaluate how well the strategy performs under various market conditions (trending, sideways, volatile).

