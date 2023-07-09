import requests
from bs4 import BeautifulSoup
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

BASE_URL = 'https://999.md'
AD_URL = BASE_URL + "/ru/list/transport/cars?applied=1&o_1_21_34=22562&o_1_21_34=78&o_4_151=10&r_6_2_unit=eur&ef=260" \
      "&ef=6&ef=4112&ef=2029&ef=1279&ef=7&ef=4&ef=5&r_6_2_negotiable=yes&r_6_2_to=&r_7_19_from=2011" \
      "&show_all_checked_childrens=no&r_7_19_to=&r_6_2_from=&page=:page "


class Scrapper:
    def __init__(self):
        self._pages_counter: int = 0
        self.image_urls: List[str] = []
        self.ads_list: List[CarItem] = []

    def _get_pages_count(self):
        response = requests.get(AD_URL.replace(':page', '9999'))
        soup = BeautifulSoup(response.content, "html.parser")
        nav = soup.find('nav', class_='paginator cf')
        page_num = nav.find_all('a', href=True)[-1].text
        self._pages_counter = int(page_num)

    def find_images(self):
        self._get_pages_count()
        logging.info(f'Pages to process: {self._pages_counter}')
        for n in range(self._pages_counter):
            response = requests.get(AD_URL.replace(':page', str(n+1)))
            soup = BeautifulSoup(response.content, 'html.parser')
            item_list = soup.find_all('a', class_='js-item-ad')
            for item in item_list:
                if item.has_attr('href') and item.find('img') is not None:
                    self.ads_list.append(CarItem(item.find('img').get('src').replace('320x240', '900x900'),
                                                 BASE_URL + item.get('href')))
            logging.info(f'Page nr.{n+1} has been processed')

# TODO: might be redundant
    # def save_images(self):
    #     timestamp = datetime.now().strftime().strftime("%Y-%m-%d%H-%M-%S")
    #     with open('./data/image_urls.txt' + timestamp, 'a') as f:
    #         for image_url in self.image_urls:
    #             f.write(image_url)


class CarItem:
    def __init__(self, img_url, ad_url):
        self.img_url = img_url
        self.ad_url = ad_url
