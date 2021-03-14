from dataclasses import dataclass
from datetime import date
from enum import Enum


@dataclass
class KataComplexity(Enum):
    KYU_8 = 0
    KYU_7 = 1
    KYU_6 = 2
    KYU_5 = 3
    KYU_4 = 4
    KYU_3 = 5
    KYU_2 = 6
    KYU_1 = 7
    DAN_1 = 8
    DAN_2 = 9
    DAN_3 = 10
    DAN_4 = 11


@dataclass
class LanguageCompletions(object):
    programming_language: str
    total_completions: int


@dataclass
class KataStats:
    id: str
    name: str
    author: str
    author_profiles: list[str]
    tags: list[str]
    kata_complexity: KataComplexity
    published: date
    warriors_trained: int
    total_skips: int
    total_code_submissions: int
    total_times_completed: int
    languages_completions: list[LanguageCompletions]
    total_stars: int
    positive_feedback: float
    total_very_satisfied_votes: int
    total_somewhat_satisfied_votes: int
    total_not_satisfied_votes: int
    total_rank_assessments: int
    average_assessed_rank: KataComplexity
    highest_assessed_rank: KataComplexity
    lowest_assessed_rank: KataComplexity
