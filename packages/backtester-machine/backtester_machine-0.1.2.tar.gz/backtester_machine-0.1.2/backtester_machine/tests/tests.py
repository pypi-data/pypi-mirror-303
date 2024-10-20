import unittest
import pandas as pd
import numpy as np
from unittest.mock import patch
from strategy import compute_max_drawdown, compute_win_rate, setup_global_var, run_final_backtest, plot_strategy_results
# Combine FIRST, SECOND, THIRD into strategy

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

def compute_max_drawdown(equity_curve):
    """Compute the maximum drawdown of the equity curve."""
    drawdown = equity_curve / equity_curve.cummax() - 1
    return drawdown.min()


def compute_win_rate(results):
    """Compute win rate from strategy results."""
    wins = results[results['PnL'] > 0].shape[0]
    total_trades = results.shape[0]
    win_rate = wins / total_trades if total_trades > 0 else 0
    return win_rate


class TestStrategyFunctions(unittest.TestCase):

    def setUp(self):
        # Sample equity curve for testing max drawdown
        self.equity_curve = pd.Series([100, 110, 90, 95, 120, 80, 130])
        # Sample results for testing win rate
        self.results = pd.DataFrame({
            'PnL': [10, -5, 15, -10, 20, -5]
        })

    def test_compute_max_drawdown(self):
        """Test the max drawdown calculation."""
        result = compute_max_drawdown(self.equity_curve)
        expected = -0.3846153846153846  # The maximum drawdown from the sample equity curve
        self.assertAlmostEqual(result, expected, places=5)

    def test_compute_win_rate(self):
        """Test the win rate calculation."""
        result = compute_win_rate(self.results)
        expected = 0.5  # 3 wins out of 6 trades
        self.assertAlmostEqual(result, expected)

    def test_setup_global_var(self):
        """Test the setup of global variables."""

        class Vars:
            future_periods = 10
            feature_selection_criteria = 'some_criteria'
            time_zone = 'UTC'
            tz = 'Europe/Copenhagen'
            LT_timeframes = ['1D', '1W']
            data_source = 'Yahoo'
            start_time = '2020-01-01'
            end_time = '2024-01-01'
            ticker_type = 'stock'
            ticker_results_path = '/path/to/results'
            direction = 'bullish'
            stop_loss_type = 'percentage'
            stop_loss_amt = 0.02

        setup_global_var(Vars)
        self.assertEqual(future_periods, 10)
        self.assertEqual(feature_selection_criteria, 'some_criteria')

    @patch('matplotlib.pyplot.show')  # Mock the plotting to avoid showing the plot during tests
    def test_run_final_backtest(self):
        """Test the final backtest execution."""
        best_strategies_ratio = [('EMA Crossover_50_200', 1.5)]
        initial_train_data = pd.DataFrame({'Date': pd.date_range(start='2020-01-01', periods=100), 'Close': np.random.random(100)})
        validation_data = pd.DataFrame({'Date': pd.date_range(start='2020-04-10', periods=50), 'Close': np.random.random(50)})
        final_test_data = pd.DataFrame({'Date': pd.date_range(start='2020-06-01', periods=50), 'Close': np.random.random(50)})

        # Mock the strategies and backtesting function
        global strategies
        strategies = {
            'EMA Crossover': (lambda x, a, b: pd.DataFrame({'equity_curve': np.random.random(100)}), None, 'long', 'percentage', 0.02, None, None, None, None)
        }

        results, metrics = run_final_backtest(best_strategies_ratio, initial_train_data, validation_data, final_test_data)

        self.assertIn('EMA Crossover_50_200', results)

    @patch('matplotlib.pyplot.show')
    def test_plot_strategy_results(self):
        """Test the plotting of strategy results."""
        best_strategy_results = {
            'EMA Crossover_50_200': (1.5, pd.DataFrame({'equity_curve': np.random.random(100)}))
        }

        # Check if plotting function executes without error
        plot_strategy_results(best_strategy_results)


if __name__ == '__main__':
    unittest.main()
