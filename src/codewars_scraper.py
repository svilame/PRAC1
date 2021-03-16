from datetime import datetime

import requests
from bs4 import BeautifulSoup

from src.kata_stats import LanguageCompletions, KataComplexity

complexity_mapping = {
    "8 kyu": KataComplexity.KYU_8,
    "7 kyu": KataComplexity.KYU_7,
    "6 kyu": KataComplexity.KYU_6,
    "5 kyu": KataComplexity.KYU_5,
    "4 kyu": KataComplexity.KYU_4,
    "3 kyu": KataComplexity.KYU_3,
    "2 kyu": KataComplexity.KYU_2,
    "1 kyu": KataComplexity.KYU_1,
    "1 dan": KataComplexity.DAN_1,
    "2 dan": KataComplexity.DAN_2,
    "3 dan": KataComplexity.DAN_3,
    "4 dan": KataComplexity.DAN_4
}


class KataScrapper:
    @staticmethod
    def download_html(url) -> str:
        return requests.get(url).content

    @staticmethod
    def get_kata_id_kata(html: str) -> str:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.mt-1.mb-3')[0].text

    @staticmethod
    def get_kata_name(html: str) -> str:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.flex.items-center > h4')[0].text

    @staticmethod
    def get_kata_author(html: str) -> str:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.mt-1.mb-3 > a.ml-4.mr-0')[0].text

    @staticmethod
    def get_kata_author_profile(html: list) -> list:
        dom_li = BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-256.max-w-full.mx-auto.my-0.px-0 > section > div > div > div.flex-box > div:nth-child(2) > div:nth-child(3) > ul > li')
        return [li.a.get('href') for li in dom_li]

    @staticmethod
    def get_kata_tags(html: list) -> list:
        keytag = BeautifulSoup(html, features="html.parser").select('div.keyword-tag')
        return [key.text for key in keytag]

    @staticmethod
    def get_kata_complexity(html: str) -> KataComplexity:
        return complexity_mapping.get(BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.px-0.w-full > div > div.w-full.md\:w-5\/12 > div.flex.items-center > div > div > span')[
                                          0].text)

    @staticmethod
    def get_kata_published(html: str) -> datetime:
        published_date = BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.p-1.text-right')[
            0].text
        return datetime.strptime(published_date, '%b %d, %Y').date()

    @staticmethod
    def get_kata_warriors_trained(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_skips(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_code_submissions(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.p-1.value.text-right')[
            0].text

    @staticmethod
    def get_kata_total_times_completed(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(6) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_languages_completions(html: str) -> list[LanguageCompletions]:
        dom_tr = BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr')
        languages_completions = []
        for tr in dom_tr:
            if (value := tr.find(class_='p-1 pl-5')) is not None:
                languages_completions.append(LanguageCompletions(value.text.replace(' Completions', ''),
                                                                 int(tr.find(class_='p-1 text-right').text)))
        return languages_completions

    @staticmethod
    def get_kata_total_stars(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(1) > table > tbody > tr:nth-child(9) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_positive_feedback(html: float) -> float:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.p-1.text-right')[
            0].text.split('%')[0]

    @staticmethod
    def get_kata_total_very_satisfied_votes(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_somewhat_satisfied_votes(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_not_satisfied_votes(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_total_rank_assessments(html: int) -> int:
        return BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.p-1.text-right')[
            0].text

    @staticmethod
    def get_kata_average_assessed_rank(html) -> KataComplexity:
        return complexity_mapping.get(BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.p-1.text-right > div > div > span')[
                                          0].text)

    @staticmethod
    def get_kata_highest_assessed_rank(html) -> KataComplexity:
        return complexity_mapping.get(BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(7) > td.p-1.text-right > div > div > span')[
                                          0].text)

    @staticmethod
    def get_kata_lowest_assessed_rank(html) -> KataComplexity:
        return complexity_mapping.get(BeautifulSoup(html, features="html.parser").select(
            '#shell_content > div.w-full.mt-2 > div:nth-child(6) > div > div:nth-child(2) > table > tbody > tr:nth-child(8) > td.p-1.text-right > div > div > span')[
                                          0].text)


if __name__ == '__main__':
    # html = KataScrapper.download_html("https://www.codewars.com/users/kodejuice")
    html = KataScrapper.download_html("https://www.codewars.com/kata/5ac616ccbc72620a6a000096")
    print(KataScrapper.get_kata_lowest_assessed_rank(html))
