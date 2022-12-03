from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
from collections import defaultdict
import random


class PriceCompare:

    def __init__(self, product):

        self.looktable_amzn = None
        self.looktable_flip = None
        self.var = product
        self.key = None

    def find(self):
        product = self.var
        product_arr = product.split()
        n = 1
        self.key = ""

        for word in product_arr:
            if n == 1:
                self.key = self.key + str(word)
                n += 1
            else:
                self.key = self.key + '+' + str(word)

        self.price_flipkart(self.key)
        self.price_amzn(self.key)

    def price_flipkart(self, key):
        url_flip = 'https://www.flipkart.com/search?q=' + str(
            key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
        map = defaultdict(list)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        source_code = requests.get(url_flip, headers=headers)
        soup = BeautifulSoup(source_code.text, "html.parser")
        home = 'https://www.flipkart.com'
        for block in soup.find_all('div', {'class': '_2kHMtA'}):
            title, price, link = None, 'Currently Unavailable', None
            for heading in block.find_all('div', {'class': '_4rR01T'}):
                title = heading.text
            for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
                price = p.text[1:]
            for l in block.find_all('a', {'class': '_1fQZEK'}):
                link = home + l.get('href')
            map[title] = [price, link]

        user_input = self.var
        matches_flip = get_close_matches(user_input, map.keys(), 20, 0.1)
        self.looktable_flip = {}
        for title in matches_flip:
            self.looktable_flip[title] = map[title]

    def price_amzn(self, key):
        url_amzn = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + str(key)

        # Faking the visit from a browser
        headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        map = defaultdict(list)
        home = 'https://www.amazon.in'
        proxies_list = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                        "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                        "134.213.29.202:4444"]
        proxies = {'https': random.choice(proxies_list)}
        source_code = requests.get(url_amzn, headers=headers)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for html in soup.find_all('div', {'class': 'sg-col-inner'}):
            title, link, price, img = None, None, None, None
            for heading in html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}):
                title = heading.text
            for p in html.find_all('span', {'class': 'a-price-whole'}):
                price = p.text
            for l in html.find_all('a', {
                'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}):
                link = home + l.get('href')
            # for i in html.find_all('div'):
                # img = i
            if title and link:
                map[title] = [price, link]
        user_input = self.var
        matches_amzn = get_close_matches(user_input, list(map.keys()), 20, 0.01)
        self.looktable_amzn = {}
        for title in matches_amzn:
            self.looktable_amzn[title] = map[title]


def get_price(product: str):
    c = PriceCompare(product)
    c.find()
    return c.looktable_flip, c.looktable_amzn
