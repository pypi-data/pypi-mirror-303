import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
    This is free and unencumbered software released into the public domain.

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.

    In jurisdictions that recognize copyright laws, the author or authors
    of this software dedicate any and all copyright interest in the
    software to the public domain. We make this dedication for the benefit
    of the public at large and to the detriment of our heirs and
    successors. We intend this dedication to be an overt act of
    relinquishment in perpetuity of all present and future rights to this
    software under copyright law.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

    For more information, please refer to <http://unlicense.org/>
    """

def strategy_backtest():
    sharpe_results, adj_sharpe_results, EV_results = {}, {}, {}
    strategy_results = {}

    validation_data2 = pd.concat([initial_train_data, validation_data], axis=0)
    # Expand the validation data with initial_train_data for computing strategy indicators (not training models).
    for strat_name, (strat_function, time_frames, side, SL_type, SL, SL_spike_out, TP, TS, active_strat) in strategies.items():
        if not active_strat or timeframe not in time_frames:
            continue
        print(f'Backtesting strategy: {strat_name} ...')
        if 'EMA Crossover' in strat_name:
            for span_a, span_b in ema_pairs:
                strategy_info = strat_function(validation_data2.copy(), span_a, span_b).loc[validation_data.index]
                results = backtest_over_periods(split_periods(strategy_info), side, SL_type, SL, SL_spike_out, TP, TS)
                strategy_results[f'{strat_name}_{span_a}_{span_b}'] = results
                sharpe_results[f'{strat_name}_{span_a}_{span_b}'], adj_sharpe_results[f'{strat_name}_{span_a}_{span_b}'], EV_results[f'{strat_name}_{span_a}_{span_b}'] \
                    = (compute_ratios('mean', results, order_return_backtest_run['sharpe_ratio']),
                       compute_ratios('mean', results, order_return_backtest_run['adj_sharpe_ratio'], None_transform=False),
                       compute_ratios('mean', results, order_return_backtest_run['ev_ratio'], None_transform=False))
        elif 'Fibonacci Retracement' in strat_name:
            for fib_direction in fib_directions:
                if fib_direction in direction:
                    for fib_retracement in fib_retracements:
                        strategy_info = strat_function(validation_data2.copy(), fib_retracement, fib_direction).loc[validation_data.index]
                        results = backtest_over_periods(split_periods(strategy_info), side, SL_type, SL, SL_spike_out, TP, TS)
                        strategy_results[f'{strat_name}_{fib_retracement}_{fib_direction}'] = results
                        (sharpe_results[f'{strat_name}_{fib_retracement}_{fib_direction}'],
                         adj_sharpe_results[f'{strat_name}_{fib_retracement}_{fib_direction}'], EV_results[f'{strat_name}_{fib_retracement}_{fib_direction}']) \
                            = (compute_ratios('mean', results, order_return_backtest_run['sharpe_ratio']),
                               compute_ratios('mean', results, order_return_backtest_run['adj_sharpe_ratio'], None_transform=False),
                               compute_ratios('mean', results, order_return_backtest_run['ev_ratio'], None_transform=False))
    return strategy_results, sharpe_results, adj_sharpe_results, EV_results

# Define additional strategies
def rsi_strategy(data, period=14, overbought=70, oversold=30):
    """RSI strategy: Buy when RSI < oversold, Sell when RSI > overbought."""
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    data['RSI'] = rsi
    buy_signals = data['RSI'] < oversold
    sell_signals = data['RSI'] > overbought

    return buy_signals, sell_signals


def bollinger_bands_strategy(data, window=20, std_dev_factor=2):
    """Bollinger Bands strategy: Buy when price is below lower band, Sell when price is above upper band."""
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()

    data['Upper Band'] = rolling_mean + (rolling_std * std_dev_factor)
    data['Lower Band'] = rolling_mean - (rolling_std * std_dev_factor)

    buy_signals = data['Close'] < data['Lower Band']
    sell_signals = data['Close'] > data['Upper Band']

    return buy_signals, sell_signals


# Extended backtest function
def extended_strategy_backtest():
    sharpe_results, adj_sharpe_results, EV_results = {}, {}, {}
    strategy_results = {}

    validation_data2 = pd.concat([initial_train_data, validation_data], axis=0)

    for strat_name, (strat_function, time_frames, side, SL_type, SL, SL_spike_out, TP, TS, active_strat) in strategies.items():
        if not active_strat or timeframe not in time_frames:
            continue
        print(f'Backtesting strategy: {strat_name} ...')

        if strat_name == 'RSI Strategy':
            buy_signals, sell_signals = rsi_strategy(validation_data2.copy())
            # Perform backtesting on RSI signals...

        elif strat_name == 'Bollinger Bands Strategy':
            buy_signals, sell_signals = bollinger_bands_strategy(validation_data2.copy())
            # Perform backtesting on Bollinger Bands signals...

        # Other strategy checks like 'EMA Crossover', 'Fibonacci Retracement' here...

        # Assuming you have similar backtest_over_periods and result computation logic...
        results = backtest_over_periods(validation_data2, side, SL_type, SL, SL_spike_out, TP, TS)
        strategy_results[strat_name] = results
        sharpe_results[strat_name], adj_sharpe_results[strat_name], EV_results[strat_name] = (
            compute_ratios('mean', results, order_return_backtest_run['sharpe_ratio']),
            compute_ratios('mean', results, order_return_backtest_run['adj_sharpe_ratio'], None_transform=False),
            compute_ratios('mean', results, order_return_backtest_run['ev_ratio'], None_transform=False)
        )

    return strategy_results, sharpe_results, adj_sharpe_results, EV_results


# Visualization for strategy results
def plot_strategy_results(strategy_name, results):
    plt.figure(figsize=(12, 6))
    plt.plot(results['Date'], results['Cumulative Returns'], label=f'{strategy_name} Cumulative Returns')
    plt.title(f'{strategy_name} Performance')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.show()


# Call the extended backtest
strategy_results, sharpe_results, adj_sharpe_results, EV_results = extended_strategy_backtest()

# Example plotting for a strategy
plot_strategy_results('RSI Strategy', strategy_results['RSI Strategy'])
