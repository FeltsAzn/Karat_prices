from fake_useragent import UserAgent
"""User agent generator for website parsing"""

user = UserAgent()

head_browser = {
    'Accept': '*/*',
    'User-Agent': user.chrome
}
# url_site = 'https://www.karat-market.ru/catalog/'  # Full catalog of website
url_site = 'https://www.karat-market.ru/catalog/stroymaterialy/'  # Required sector to get prices
