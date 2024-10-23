import numpy as np
import pandas as pd

from finter.backtest.simulator import Simulator as BaseSimulator
from finter.backtest.us_stock.main import USStockBacktestor
from finter.backtest.vietnam.main import VietnamBacktestor
from finter.data.data_handler.main import DataHandler

UNIVERSE_DEFAULTS = {
    "kr_stock": {
        "initial_cash": 100000000,  # 1억원
        "buy_fee_tax": 1.2,
        "sell_fee_tax": 31.2,
        "slippage": 10,
        "default_benchmark": "KOSPI200",
        "adj_dividend": False,
    },
    "us_stock": {
        "initial_cash": 100000,  # 10만 달러
        "buy_fee_tax": 25,
        "sell_fee_tax": 25,
        "slippage": 10,
        "default_benchmark": "S&P500",
        "adj_dividend": False,
    },
    "us_etf": {
        "initial_cash": 100000,  # 10만 달러
        "buy_fee_tax": 25,
        "sell_fee_tax": 25,
        "slippage": 10,
        "default_benchmark": "S&P500",
        "adj_dividend": False,
    },
    "vn_stock": {
        "initial_cash": 1000000000,  # 10억 동
        "buy_fee_tax": 40,
        "sell_fee_tax": 50,
        "slippage": 10,
        "default_benchmark": "HO_CHI_MINH_STOCK_INDEX",
        "adj_dividend": False,
    },
    #########################################################
    "vn_stock_deprecated": {
        "initial_cash": 1000000000,  # 10억 동
        "buy_fee_tax": 40,
        "sell_fee_tax": 50,
        "slippage": 10,
        "default_benchmark": "HO_CHI_MINH_STOCK_INDEX",
        "adj_dividend": False,
    },
    "id_stock": {
        "initial_cash": 1000000000,  # 10억 동
        "buy_fee_tax": 40,
        "sell_fee_tax": 50,
        "slippage": 10,
        "default_benchmark": "HO_CHI_MINH_STOCK_INDEX",
        "adj_dividend": False,
    },
    "crypto_spot_binance": {
        "initial_cash": 100000,  # 10만 달러
        "buy_fee_tax": 10,
        "sell_fee_tax": 10,
        "slippage": 10,
        "default_benchmark": "US_DOLLAR_INDEX",
        "adj_dividend": False,
    },
}


class Simulator:
    def __init__(self, start, end, data_handler: DataHandler = None):
        # Todo change with fill_nan=False
        from datetime import datetime, timedelta

        end_dt = datetime.strptime(str(end), "%Y%m%d") + timedelta(days=30)
        end_dt_int = int(end_dt.strftime("%Y%m%d"))
        self.start_str = datetime.strptime(str(start), "%Y%m%d").strftime("%Y-%m-%d")
        self.end_str = datetime.strptime(str(end), "%Y%m%d").strftime("%Y-%m-%d")

        self.data_handler = data_handler or DataHandler(
            start, end_dt_int, cache_timeout=300
        )

    def run(
        self,
        universe,
        position,
        initial_cash=None,
        buy_fee_tax=None,
        sell_fee_tax=None,
        slippage=None,
        adj_dividend=None,
    ):

        # position = position[position.index >= start_date]
        defaults = UNIVERSE_DEFAULTS.get(universe, {})
        initial_cash = (
            initial_cash if initial_cash is not None else defaults.get("initial_cash")
        )
        buy_fee_tax = (
            buy_fee_tax if buy_fee_tax is not None else defaults.get("buy_fee_tax")
        )
        sell_fee_tax = (
            sell_fee_tax if sell_fee_tax is not None else defaults.get("sell_fee_tax")
        )
        slippage = slippage if slippage is not None else defaults.get("slippage")
        adj_dividend = (
            adj_dividend if adj_dividend is not None else defaults.get("adj_dividend")
        )
        print(
            "initial_cash: ",
            initial_cash,
            "buy_fee_tax: ",
            buy_fee_tax,
            "sell_fee_tax: ",
            sell_fee_tax,
            "slippage: ",
            slippage,
            "adj_dividend: ",
            adj_dividend,
        )

        price = (
            self.data_handler.universe(universe)
            .price(adj_div=adj_dividend)
            .dropna(how="all")
            .loc[self.start_str : self.end_str]
        )  # fill_nan=False

        position = position.loc[price.index[0] : price.index[-1]]
        position = position.reindex(price.index)
        assert position.index.equals(price.index)

        if universe == "kr_stock":
            return self.run_simulation_kr(
                position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
            )
        elif universe in ["us_stock", "us_etf"]:
            return self.run_simulation_us(
                position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
            )
        elif universe in ["vn_stock", "vn_stock_deprecated"]:
            return self.run_simulation_vn(
                position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
            )
        elif universe == "id_stock":
            return self.run_simulation_kr(
                position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
            )
        else:
            raise ValueError(f"Unsupported universe: {universe}")

    def run_simulation_kr(
        self, position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
    ):
        position = position.reindex(columns=price.columns)
        simulator = BaseSimulator(
            position,
            price,
            initial_cash=initial_cash,
            buy_fee_tax=buy_fee_tax,
            sell_fee_tax=sell_fee_tax,
            slippage=slippage,
        )
        simulator.run()
        return simulator

    def run_simulation_us(
        self, position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
    ):
        # TODO: Implement US stock/ETF simulation logic
        # For now, we'll use the same logic as KR stocks
        position = position.reindex(columns=price.columns)
        simulator = BaseSimulator(
            position,
            price.ffill(),
            initial_cash=initial_cash,
            buy_fee_tax=buy_fee_tax,
            sell_fee_tax=sell_fee_tax,
            slippage=slippage,
        )
        simulator.run()
        return simulator

    def run_simulation_vn(
        self, position, price, initial_cash, buy_fee_tax, sell_fee_tax, slippage
    ):
        position = position.reindex(columns=price.columns)
        simulator = VietnamBacktestor(
            position,
            price,
            initial_cash=initial_cash,
            buy_fee_tax=buy_fee_tax,
            sell_fee_tax=sell_fee_tax,
            slippage=slippage,
        )
        simulator.run()
        return simulator


if __name__ == "__main__":
    s = Simulator(20240601, 20240823)

    res = s.run(
        "kr_stock",
        s.data_handler.load("alpha.krx.krx.stock.ldh0127.div_new_1"),
        adj_dividend=True,
    )
    res.summary
