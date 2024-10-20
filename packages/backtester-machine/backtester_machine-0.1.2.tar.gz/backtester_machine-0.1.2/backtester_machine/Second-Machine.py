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

def strategy_comparison(strategy_results, sharpe_results, adj_sharpe_results, EV_results):
    """Compare all strategies to find the best and worst strategies through the backtest."""
    print("\nComparing strategies through backtest ...")

    best_strategies_results = {}
    strategies_to_always_compare = ['buyAndHold']

    ranked_strategies_by_criterion = []
    ratio_results = EV_results if classification_criterion == 'EV' else adj_sharpe_results if classification_criterion == 'Adj Sharpe' else sharpe_results

    none_strategies = {key: value for key, value in ratio_results.items() if not value}
    valid_strategies = {key: value for key, value in ratio_results.items() if value}
    ranked_valid_strategies = sorted(valid_strategies.items(), key=lambda x: x[1], reverse=True)
    ranked_strategies_by_criterion = ranked_valid_strategies + list(none_strategies.items())
    ranked_names = [sublist[0] for sublist in ranked_strategies_by_criterion]

    # Plot equity curves for the top and bottom strategies and writing results to file.
    plt.ioff()
    plt.figure(figsize=(10, 6))
    strategy_colors = {}
    no_colors = len(ranked_strategies_by_criterion)
    colors = np.random.rand(no_colors, 3)

    for strat_name, all_attributes in ranked_strategies_by_criterion:
        plt.plot(all_attributes.index, all_attributes['equity_curve'], color=colors[len(strategy_colors)])

    plt.title(f'Equity Curves Comparison by {classification_criterion}')
    plt.xlabel('Date')
    plt.ylabel('Equity ($)')
    plt.grid()
    plt.show()

def compute_max_drawdown(equity_curve):
    """Compute the maximum drawdown of the equity curve."""
    drawdown = equity_curve / equity_curve.cummax() - 1
    max_drawdown = drawdown.min()
    return max_drawdown


def compute_win_rate(results):
    """Compute win rate from strategy results."""
    wins = results[results['PnL'] > 0].shape[0]
    total_trades = results.shape[0]
    win_rate = wins / total_trades if total_trades > 0 else 0
    return win_rate


def strategy_comparison(strategy_results, sharpe_results, adj_sharpe_results, EV_results):
    """Compare all strategies to find the best and worst strategies through the backtest."""
    print("\nComparing strategies through backtest ...")

    # Dictionary to store extra performance metrics
    extra_metrics = {}
    for strat_name, results in strategy_results.items():
        equity_curve = results['equity_curve']
        max_drawdown = compute_max_drawdown(equity_curve)
        win_rate = compute_win_rate(results)
        extra_metrics[strat_name] = {'Max Drawdown': max_drawdown, 'Win Rate': win_rate}

    # Determine the criterion for classification
    ratio_results = (EV_results if classification_criterion == 'EV'
                     else adj_sharpe_results if classification_criterion == 'Adj Sharpe'
    else sharpe_results)

    # Split into valid and None strategies
    none_strategies = {key: value for key, value in ratio_results.items() if not value}
    valid_strategies = {key: value for key, value in ratio_results.items() if value}

    # Rank strategies based on the chosen criterion
    ranked_valid_strategies = sorted(valid_strategies.items(), key=lambda x: x[1], reverse=True)
    ranked_strategies_by_criterion = ranked_valid_strategies + list(none_strategies.items())
    ranked_names = [sublist[0] for sublist in ranked_strategies_by_criterion]

    # Plot equity curves for the top and bottom strategies
    plt.ioff()
    plt.figure(figsize=(12, 7))
    strategy_colors = {}
    no_colors = len(ranked_strategies_by_criterion)
    colors = np.random.rand(no_colors, 3)

    for i, (strat_name, _) in enumerate(ranked_strategies_by_criterion):
        if strat_name in strategy_results:
            plt.plot(strategy_results[strat_name].index, strategy_results[strat_name]['equity_curve'],
                     color=colors[i], label=f'{strat_name}')
            strategy_colors[strat_name] = colors[i]

    plt.title(f'Equity Curves Comparison by {classification_criterion}')
    plt.xlabel('Date')
    plt.ylabel('Equity ($)')
    plt.legend()
    plt.grid()
    plt.show()

    # Print best strategy
    best_strategy = ranked_valid_strategies[0][0] if ranked_valid_strategies else "No valid strategy"
    print(f'Best strategy: {best_strategy}')

    # Print additional metrics for top strategies
    print("\nAdditional Performance Metrics:")
    for strat_name, metrics in extra_metrics.items():
        print(f"{strat_name}: Max Drawdown = {metrics['Max Drawdown']:.2%}, Win Rate = {metrics['Win Rate']:.2%}")

    return ranked_strategies_by_criterion, extra_metrics


# Example usage with hypothetical data
classification_criterion = 'Sharpe'
strategy_results = {
    'Strategy 1': pd.DataFrame({'equity_curve': np.random.random(100)}),
    'Strategy 2': pd.DataFrame({'equity_curve': np.random.random(100)}),
    'Strategy 3': pd.DataFrame({'equity_curve': np.random.random(100)}),
}

sharpe_results = {'Strategy 1': 1.2, 'Strategy 2': 0.8, 'Strategy 3': 1.5}
adj_sharpe_results = {'Strategy 1': 1.1, 'Strategy 2': 0.75, 'Strategy 3': 1.4}
EV_results = {'Strategy 1': 1.3, 'Strategy 2': 0.85, 'Strategy 3': 1.55}

ranked_strategies, extra_metrics = strategy_comparison(strategy_results, sharpe_results, adj_sharpe_results, EV_results)
