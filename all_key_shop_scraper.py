from webscraper import Webscraper
from typing import final, Final, Iterable, Any
from pandas import DataFrame
from requests import Response
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas as pd
import requests


@final
class AllKeyShopScraper(Webscraper):
    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def scraped_data(self) -> DataFrame | None:
        return self._scraped_data

    def __init__(self) -> None:
        self._endpoint: Final[str] = 'https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/'
        self._scraped_data = None

    def scrape(self) -> DataFrame | None:
        response: Response = requests.get(self.endpoint)
        if response.status_code != 200:
            return None

        html_doc: str = response.text
        soup: BeautifulSoup = BeautifulSoup(html_doc, "html.parser")

        results: Iterable[Any] = soup.find_all("li", 'search-results-row')
        games: dict[str, str] = {}

        for row in results:
            game_title: Tag | None = row.find('h2', 'search-results-row-game-title')
            price_with_currency: Tag | None = row.find('div', 'search-results-row-price')

            if game_title is not None and price_with_currency is not None:
                games[game_title.text.strip()] = price_with_currency.text.strip()

        games_df: DataFrame = pd.DataFrame.from_dict(games, orient='index')

        return games_df
