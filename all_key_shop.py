from external_data_source import ExternalDataSource
from pandas import DataFrame
import pandas as pd
from all_key_shop_scraper import AllKeyShopScraper
from typing import final
from pathlib import Path


@final
class AllKeyShop(ExternalDataSource):
    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    @property
    def prices_data(self) -> DataFrame:
        return self._prices_data

    @property
    def logs_path(self) -> Path:
        return self._logs_path

    def __init__(self, name: str, url: str, save_data_after_init: bool) -> None:
        self._name: str = name
        self._url: str = url
        self._prices_data: DataFrame | None = self.__retrieve_prices_data()
        self._logs_path: Path = Path('price_logs') / f'{self.name}.csv'

        if save_data_after_init and self.prices_data is not None:
            ExternalDataSource.save_prices_data(self.prices_data, path=self.logs_path)

    def __retrieve_prices_data(self) -> DataFrame | None:
        scraper: AllKeyShopScraper = AllKeyShopScraper()
        scraped_data: DataFrame | None = scraper.scrape()

        if scraped_data is None:
            return None

        self.preprocess_data(scraped_data)

        return scraped_data

    @staticmethod
    def preprocess_data(data: DataFrame) -> None:
        data.columns = ['Price (€)']
        data['Price (€)'] = data['Price (€)'].apply(lambda price: price[:-1])
        data['Price (€)'] = data['Price (€)'].astype(dtype=float)
        data.sort_values(by='Price (€)', ascending=False, inplace=True)
