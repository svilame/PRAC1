import os
from datetime import datetime
from time import sleep

from src.codewars_scraper import KataScrapper
from src.kata_stats import KataStats

if __name__ == '__main__':
    initial_time = datetime.now()
    with open('data/katas.txt', 'r') as f:
        with open('data/katas.csv', 'w') as csv:
            index = 1
            for id_kata in f.readlines():
                id = id_kata[:-1]
                kata_html = KataScrapper.download_html(f"https://www.codewars.com/kata/{id}")
                author = name = KataScrapper.get_kata_author(kata_html)
                author_html = KataScrapper.download_html(f'https://www.codewars.com/users/{author}')
                kata = KataStats(id=id,
                                 name=KataScrapper.get_kata_name(kata_html),
                                 author=author,
                                 author_profiles=KataScrapper.get_kata_author_profile(author_html),
                                 tags=KataScrapper.get_kata_tags(kata_html),
                                 kata_complexity=KataScrapper.get_kata_complexity(kata_html),
                                 published=KataScrapper.get_kata_published(kata_html),
                                 warriors_trained=KataScrapper.get_kata_warriors_trained(kata_html),
                                 total_skips=KataScrapper.get_kata_total_skips(kata_html),
                                 total_code_submissions=KataScrapper.get_kata_total_code_submissions(kata_html),
                                 total_times_completed=KataScrapper.get_kata_total_times_completed(kata_html),
                                 languages_completions=KataScrapper.get_kata_total_languages_completions(kata_html),
                                 total_stars=KataScrapper.get_kata_total_stars(kata_html),
                                 positive_feedback=KataScrapper.get_kata_positive_feedback(kata_html),
                                 total_very_satisfied_votes=KataScrapper.get_kata_total_very_satisfied_votes(kata_html),
                             total_somewhat_satisfied_votes=KataScrapper.get_kata_total_somewhat_satisfied_votes(
                                     kata_html),
                                 total_not_satisfied_votes=KataScrapper.get_kata_total_not_satisfied_votes(kata_html),
                                 total_rank_assessments=KataScrapper.get_kata_total_rank_assessments(kata_html),
                                 average_assessed_rank=KataScrapper.get_kata_average_assessed_rank(kata_html),
                                 highest_assessed_rank=KataScrapper.get_kata_highest_assessed_rank(kata_html),
                                 lowest_assessed_rank=KataScrapper.get_kata_lowest_assessed_rank(kata_html))
                csv.write(f"{kata.get_csv_row_representation()}{os.linesep}")
                sleep(0.5)
                print(f"{index} katas retrieved in {datetime.now() - initial_time}")
                index += 1
