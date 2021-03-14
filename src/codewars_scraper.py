from datetime import datetime

import requests
from bs4 import BeautifulSoup


class KataScrapper:

    @staticmethod
    def download_html(url) -> str:
        return requests.get(url).content

    @staticmethod
    def get_kata_name(html: str) -> str:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.flex.items-center > h4')[0].text

    @staticmethod
    def get_kata_published(html: str) -> datetime:
        published_date = BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.p-1.text-right')[0].text
        return datetime.strptime(published_date, '%b %d, %Y').date()


if __name__ == '__main__':
    html = KataScrapper.download_html("https://www.codewars.com/kata/5ac616ccbc72620a6a000096")
    print(KataScrapper.get_kata_published(html))
