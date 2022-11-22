import asyncio
import aiohttp
from bs4 import BeautifulSoup
from logs.logger import debug_log, info_log, exception_log
from data_methods.writer_and_reader import writer
from parser.setting_for_parser import head_browser, url_site


def products_finder(soup_data: BeautifulSoup) -> (list, list):
    """The function of finding the name of the product and its price"""

    products_items = soup_data.find_all('div', class_='product-item')
    names = []
    prices = []
    for data in products_items:
        name: str = data.find_next(class_='product-item__name').text
        price: str = data.find_next('span', class_="cur-price").text
        names.append(name)
        prices.append(price)
    return names, prices


def products_cards(names: list, prices: list) -> dict:
    """Function for combining the name and price of the product"""

    assert isinstance(names, list) and isinstance(prices, list), 'Ошибка списков!'
    products = {}
    for name, price in sorted(zip(names, prices), key=lambda x: x[0]):
        if price:
            products[name] = price
        else:
            products[name] = 0
    return products


class Parser:
    def __init__(self):
        info_log('Website Scraping initialized', 'parser.py', 'Parser', '__tasks_manager')

        self.__data_list = list()  # Data sheet to transfer to the writer
        self.__head = head_browser  # information for the site that we are not a bot
        self.__url = url_site  # site link for parsing
        self.__counter = 0  # counter for output to the console
        self.semaphore = asyncio.Semaphore(50)

    def __counter_requests(self, name: str) -> None:
        """Function output data to the terminal"""
        self.__counter += 1
        debug_log(f'Request {self.__counter}. The data of the "{name}" section\n'
                  f'has been written to the list of dictionaries!', 'parser.py', 'Parser', '__counter_requests')

    async def __tasks_executor(self, session: aiohttp.client.ClientSession, url: str, name_section: str) -> None:
        """Async function to find the right data"""
        async with session.get(url=url, headers=self.__head, ssl=False) as response:
            async with self.semaphore:
                response_text = await response.text()
                soup = BeautifulSoup(response_text, 'lxml')
                names, prices = products_finder(soup)
                if names and prices:
                    data: dict = products_cards(names, prices)
                    self.__data_list.append((data, name_section))
                    self.__counter_requests(name_section)
                    debug_log(f'Query {self.__counter} data added to record sheet',
                              'parser.py', 'Parser', '__tasks_executor')
                else:
                    debug_log('Data not found, looping over to find data in subdirectories',
                              'parser.py', 'Parser', '__tasks_executor')
                    links_nest_catalogs = soup.find_all('a', class_="section-item")
                    for link_and_name in links_nest_catalogs:
                        name_section: str = link_and_name.text.strip()
                        link_section = 'https://www.karat-market.ru' + link_and_name['href']
                        await self.__tasks_executor(session, link_section, name_section)

    async def __tasks_manager(self) -> None:
        """Async function to set the request processing queue"""
        async with aiohttp.ClientSession() as session:
            debug_log('Sending a request to the server', 'parser.py', 'Parser', '__tasks_manager')
            debug_log(f'Connecting to {self.__url}\n'
                      f'with header {self.__head}\n', 'parser.py', 'Parser', '__tasks_manager')
            try:
                response = await session.get(url=self.__url, headers=self.__head)
                debug_log(f'Server response received {response.status}', 'parser.py', 'Parser', '__tasks_manager')
            except Exception as exc:
                exception_log(f'Site connection error, response code {response.status}',
                              'parser.py', 'Parser', '__tasks_manager', f'{exc}')
            tasks = []
            soup = BeautifulSoup(await response.text(), 'lxml')
            links_nest_catalogs = soup.find_all('a', class_="section-item")
            for link_and_name in links_nest_catalogs:
                name_section: str = link_and_name.text.strip()
                link_section = 'https://www.karat-market.ru' + link_and_name['href']
                task = asyncio.create_task(self.__tasks_executor(session, link_section, name_section))
                tasks.append(task)
            await asyncio.gather(*tasks)

            info_log('All data collected!', 'parser.py', 'Parser', '__tasks_manager')
            info_log('Data transferred for writing!', 'parser.py', 'Parser', '__tasks_manager')

            writer(self.__data_list)

    def start_collecting(self) -> None:
        debug_log('Parser launched', 'parser.py', 'Parser', 'start_collecting')
        asyncio.run(self.__tasks_manager())
