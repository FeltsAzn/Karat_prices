from fake_useragent import UserAgent

user = UserAgent()

head_browser = {
    'Accept': '*/*',
    'User-Agent': user.chrome
}
url_site = 'https://www.karat-market.ru/catalog/'
