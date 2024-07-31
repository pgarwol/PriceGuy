from abc import ABC, abstractmethod


class Webscraper(ABC):

    @property
    @abstractmethod
    def endpoint(self):
        ...

    @property
    @abstractmethod
    def scraped_data(self):
        ...

    @abstractmethod
    def scrape(self):
        ...
