from pathlib import Path
from typing import Any, Dict

import pandas as pd
import yaml

from finter.data import ContentFactory
from finter.data.data_handler.handler_abstract import AbstractDataHandler
from finter.data.data_handler.registry import DataHandlerRegistry


def load_item_mapping_by_item(item: str) -> Dict[str, str]:
    yaml_path = Path(__file__).parent / "item_mappings.yaml"
    with open(yaml_path, "r") as f:
        mappings = yaml.safe_load(f)

    items = {}
    for key in mappings:
        if item in mappings[key]:
            items[key] = mappings[key][item]
    return items


@DataHandlerRegistry.register_handler("price")
class PriceHandler(AbstractDataHandler):
    def __init__(self):
        self.item_mapping = load_item_mapping_by_item("price")

    def get_data(self, cf: ContentFactory, universe: str, **kwargs) -> Any:
        if universe not in self.item_mapping:
            raise ValueError(f"Unsupported universe: {universe}")
        return cf.get_df(self.item_mapping[universe], **kwargs)  # 수정된 부분


@DataHandlerRegistry.register_handler("volume")
class VolumeHandler(AbstractDataHandler):
    def __init__(self):
        self.item_mapping = load_item_mapping_by_item("volume")

    def get_data(self, cf: ContentFactory, universe: str, **kwargs) -> Any:
        if universe not in self.item_mapping:
            raise ValueError(f"Unsupported universe: {universe}")
        return cf.get_df(self.item_mapping[universe], **kwargs)  # 수정된 부분


@DataHandlerRegistry.register_handler("dividend_factor")
class DividendFactorHandler(AbstractDataHandler):
    def __init__(self):
        self.item_mapping = load_item_mapping_by_item("dividend_factor")

    def get_data(self, cf: ContentFactory, universe: str, **kwargs) -> Any:
        if universe not in self.item_mapping:
            raise ValueError(f"Unsupported universe: {universe}")
        return cf.get_df(self.item_mapping[universe], **kwargs)  # 수정된 부분


@DataHandlerRegistry.register_handler("benchmark")
class BenchmarkHandler(AbstractDataHandler):
    def __init__(self):
        self.item_mapping = load_item_mapping_by_item("benchmark")

    def get_data(self, cf: ContentFactory, universe: str, **kwargs) -> Any:
        if universe not in self.item_mapping:
            raise ValueError(f"Unsupported universe: {universe}")
        if universe == "common":
            return cf.get_df(self.item_mapping["common"], **kwargs)
        else:
            return cf.get_df(self.item_mapping["common"], **kwargs)[
                self.item_mapping[universe]
            ]


@DataHandlerRegistry.register_handler("market_cap")
class MarketCapHandler(AbstractDataHandler):
    def __init__(self):
        self.item_mapping = load_item_mapping_by_item("market_cap")

    def get_data(self, cf: ContentFactory, universe: str, **kwargs) -> Any:
        if universe == "kr_stock":
            return (
                cf.get_df("content.fnguide.ftp.price_volume.mkt_cap.1d", **kwargs)
                / 1e11
            )
        elif universe == "vn_stock":
            price = cf.get_df(
                "content.spglobal.compustat.price_volume.vnm-all-price_close.1d",
                **kwargs,
            )
            shares = cf.get_df(
                "content.spglobal.compustat.price_volume.vnm-all-shares_outstanding.1d",
                **kwargs,
            )
            return price * shares
        elif universe == "id_stock":
            price = cf.get_df(
                "content.spglobal.compustat.price_volume.id-all-price_close.1d",
                **kwargs,
            )
            shares = cf.get_df(
                "content.spglobal.compustat.price_volume.id-all-shares_outstanding.1d",
                **kwargs,
            )
            return price * shares
        elif universe == "us_stock":
            price = cf.get_df(
                "content.spglobal.compustat.price_volume.us-stock-price_close.1d",
                **kwargs,
            )
            shares = cf.get_df(
                "content.spglobal.compustat.price_volume.us-stock-shares_outstanding.1d",
                **kwargs,
            )
            return price * shares
        elif universe == "us_etf":
            price = cf.get_df(
                "content.spglobal.compustat.price_volume.us-etf-price_close.1d",
                **kwargs,
            )
            shares = cf.get_df(
                "content.spglobal.compustat.price_volume.us-etf-shares_outstanding.1d",
                **kwargs,
            )
            return price * shares
        else:
            raise ValueError(
                f"Market cap data for universe {universe} is not implemented."
            )


@DataHandlerRegistry.register_calculated_method("_52week_high")
def calc_52week_high(universe, **kwargs) -> pd.Series:
    price_data = universe.price(**kwargs)
    return price_data.rolling(window=252).max()


@DataHandlerRegistry.register_calculated_method("_52week_low")
def calc_52week_low(universe, **kwargs) -> pd.Series:
    price_data = universe.price(**kwargs)
    return price_data.rolling(window=252).min()
