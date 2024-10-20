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

# Visualization function
def plot_strategy_results(best_strategy_results):
    """Plot equity curves for the best strategies from the final backtest."""
    plt.figure(figsize=(12, 7))
    colors = np.random.rand(len(best_strategy_results), 3)

    for i, (strat_name, (avg_ratio, results)) in enumerate(best_strategy_results.items()):
        plt.plot(results.index, results['equity_curve'], color=colors[i], label=f'{strat_name}')

    plt.title('Equity Curves for Best Strategies (Out-Sample)')
    plt.xlabel('Date')
    plt.ylabel('Equity ($)')
    plt.legend()
    plt.grid()
    plt.show()

# Example final backtest execution
best_strategies_ratio = [('EMA Crossover_50_200', 1.5), ('Fibonacci Retracement_0.618_bullish', 1.2)]
initial_train_data = pd.DataFrame({'Date': pd.date_range(start='2020-01-01', periods=100), 'Close': np.random.random(100)})
validation_data = pd.DataFrame({'Date': pd.date_range(start='2020-04-10', periods=50), 'Close': np.random.random(50)})
final_test_data = pd.DataFrame({'Date': pd.date_range(start='2020-06-01', periods=50), 'Close': np.random.random(50)})

best_strategy_results, extra_metrics = run_final_backtest(best_strategies_ratio, initial_train_data, validation_data, final_test_data)

# Plot the results for final backtest
plot_strategy_results(best_strategy_results)

def setup_global_var(var_):
    global future_periods, feature_selection_criteria, time_zone, tz, LT_timeframes, data_source, start_time, end_time, ticker_type, ticker_results_path
    variable_names = ('future_periods', 'feature_selection_criteria', 'time_zone', 'tz', 'LT_timeframes', 'data_source',
                      'start_time', 'end_time', 'ticker_type', 'ticker_results_path', 'direction', 'stop_loss_type', 'stop_loss_amt')
    globals().update({name: getattr(var_, name) for name in variable_names})

def run_final_backtest(best_strategies_ratio, initial_train_data, validation_data, final_test_data):
    print("\nRunning Out-Sample backtest ...")
    best_strategy_results = {}
    final_test_data2 = pd.concat([initial_train_data, validation_data, final_test_data], axis=0)

    for strat_name, avg_ratio in best_strategies_ratio:
        if 'EMA Crossover' in strat_name:
            name = strat_name.split('_')[0]
            span_a = int(strat_name.split('_')[1])
            span_b = int(strat_name.split('_')[2])
            strat_function, _, side, SL_type, SL, SL_spike_out, TP, TS, _ = strategies[name]
            strategy_info = strat_function(final_test_data2.copy(), span_a, span_b)
        elif 'Fibonacci Retracement' in strat_name:
            name = strat_name.split('_')[0]
            fib_retracement = float(strat_name.split('_')[1])
            fib_direction = strat_name.split('_')[2]
            strat_function, _, side, SL_type, SL, SL_spike_out, TP, TS, _ = strategies[name]
            strategy_info = strat_function(final_test_data2.copy(), fib_retracement, fib_direction)
        # Add more strategy conditions if needed
        best_strategy_results[strat_name] = avg_ratio, backtest_over_periods(split_periods(strategy_info), side, SL_type, SL, SL_spike_out, TP, TS)
    return best_strategy_results