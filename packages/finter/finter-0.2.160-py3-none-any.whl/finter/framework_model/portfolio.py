from abc import ABC, abstractmethod
from finter.framework_model import ContentModelLoader
from finter.framework_model.alpha_loader import AlphaPositionLoader

import pandas as pd


class BasePortfolio(ABC):
    __cm_set = set()

    @property
    @abstractmethod
    def alpha_set(self):
        return {}

    def depends(self):
        return set("alpha." + i for i in self.alpha_set) | self.__cm_set

    @classmethod
    def get_cm(cls, key):
        if key.startswith("content."):
            cls.__cm_set.add(key)
        else:
            cls.__cm_set.add("content." + key)
        return ContentModelLoader.load(key)

    def get_alpha_position_loader(
        self, start, end, exchange, universe, instrument_type, freq, position_type
    ):
        return AlphaPositionLoader(
            start,
            end,
            exchange,
            universe,
            instrument_type,
            freq,
            position_type,
            self.alpha_set,
        )

    @abstractmethod
    def get(self, start, end):
        pass

    @staticmethod
    def cleanup_position(position: pd.DataFrame):
        df_cleaned = position.loc[:, ~((position == 0) | (position.isna())).all(axis=0)]
        if df_cleaned.empty:
            df_cleaned = position

        return df_cleaned.fillna(0)
