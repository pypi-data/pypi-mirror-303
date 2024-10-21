import numpy as np
import pandas as pd
from typing_extensions import Literal

class PortfolioAnalyzer:
    @staticmethod
    def nav2stats(nav, period: Literal['M', 'Q', 'Y', None] = None):
        if period == None:
            return PortfolioAnalyzer._nav_to_stats(nav)
        else:
            return nav.groupby(pd.Grouper(freq = period)).apply(PortfolioAnalyzer._nav_to_stats).unstack()
        
    @staticmethod
    def _nav_to_stats(returns):
        if len(returns) < 2:
            return pd.Series({
                "Total Return (%)": np.nan,
                "CAGR (%)": np.nan,
                "Volatility (%)": np.nan,
                "Sharpe Ratio": np.nan,
                "Sortino Ratio": np.nan,
                "Max Drawdown (%)": np.nan,
                "Skewness": np.nan,
                "Kurtosis": np.nan,
                "VaR 95% (%)": np.nan,
                "VaR 99% (%)": np.nan,
            })
        
        total_return = (returns.iloc[-1] / returns.iloc[0] - 1) * 100
        trading_days = len(returns)
        returns_pct = returns.pct_change().dropna()

        stats_dict = {
            "Total Return (%)": round(total_return, 3),
            "CAGR (%)": round(((1 + total_return / 100) ** (252 / trading_days) - 1) * 100, 3),
            "Volatility (%)": round(returns_pct.std() * np.sqrt(252) * 100, 3),
            "Sharpe Ratio": round((returns_pct.mean() / returns_pct.std()) * np.sqrt(252), 3),
            "Sortino Ratio": round((returns_pct.mean() / returns_pct[returns_pct < 0].std()) * np.sqrt(252), 3),
            "Max Drawdown (%)": round((returns / returns.cummax() - 1).min() * 100, 3),
            "Skewness": round(PortfolioAnalyzer._calculate_skewness(returns_pct), 3),
            "Kurtosis": round(PortfolioAnalyzer._calculate_kurtosis(returns_pct), 3),
            "VaR 95% (%)": round(np.percentile(returns_pct, 5) * 100, 3),
            "VaR 99% (%)": round(np.percentile(returns_pct, 1) * 100, 3),
        }

        return pd.Series(stats_dict)

    @staticmethod
    def _calculate_kurtosis(pct_pnl):
        pct_pnl = pct_pnl.dropna()
        pnl_mean = pct_pnl.mean()
        
        m2 = ((pct_pnl - pnl_mean) ** 2).sum()
        m4 = ((pct_pnl - pnl_mean) ** 4).sum()

        n = len(pct_pnl)

        numerator = (n + 1) * n * (n - 1) * m4
        denominator = (n - 2) * (n - 3) * (m2 ** 2)
        first_term = numerator / denominator

        second_term = (3 * ((n - 1) ** 2)) / ((n - 2) * (n - 3))
        
        return first_term - second_term 

    @staticmethod
    def _calculate_skewness(pct_pnl):
        pct_pnl = pct_pnl.dropna()
        pnl_mean = pct_pnl.mean()
        n = len(pct_pnl)
        
        m3 = ((pct_pnl - pnl_mean) ** 3).sum() / n
        m2 = ((pct_pnl - pnl_mean) ** 2).sum() / n
        g1 = m3 / (m2 ** 1.5)
        return np.sqrt(n * (n - 1)) / (n - 2) * g1