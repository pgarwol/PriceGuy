from bs4 import BeautifulSoup
from typing import Iterable, Any
from bs4.element import Tag
import requests
from requests import Response
import pandas as pd
from pandas import DataFrame
from all_key_shop import AllKeyShop


def run() -> None:
    all_key_shop: AllKeyShop = AllKeyShop('AllKeyShop.com', 'https://www.allkeyshop.com/', True)
    print(all_key_shop.prices_data)


if __name__ == '__main__':
    run()
