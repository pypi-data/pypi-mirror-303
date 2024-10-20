# Backtester Machine

**A framework for backtesting financial strategies.**

## Table of Contents

- [Installation](#installation)
- [Examples](#examples)
- [Features](#features)
- [Contributing](#contributing)


## Installation

To install `backtester_machine`, clone the repository and install the package using pip:

```bash
git clone https://github.com/yourusername/backtester_machine.git
cd backtester_machine
pip install .   
```

Or install directly from PyPI (if available):

```bash
pip install backtester_machine
```

For development purposes, install the extra dependencies:

```bash
pip install backtester_machine[dev]
```

## Examples

### Example 1: Simple Backtest

```python
from backtester_machine import Backtester, Strategy

# Define a simple strategy
class SimpleStrategy(Strategy):
    def generate_signals(self, data):
        return data['price'].rolling(3).mean() > data['price']

# Create backtester instance
bt = Backtester(SimpleStrategy())

# Run backtest on data
results = bt.run(data)
print(results)
```

### Example 2: Advanced Backtest

```python
from backtester_machine import Backtester, Strategy

# Define more advanced strategy
class AdvancedStrategy(Strategy):
    def generate_signals(self, data):
        return data['price'].rolling(5).mean() < data['price']

# Run with different parameters
bt = Backtester(AdvancedStrategy(), start_cash=10000, commission=0.001)
results = bt.run(data, from_date='2020-01-01', to_date='2023-01-01')
print(results)
```

## Features

- Customizable strategies: Define your own trading strategies with ease.
- Multiple asset support: Backtest on various asset classes like stocks, crypto, etc.
- Performance metrics: Built-in evaluation metrics such as returns, volatility, and drawdowns.
- Modular design: Easily extend or modify the framework to suit your needs.

## Contributions

Contributions are welcome! Please check out the contribution guidelines for more details.



