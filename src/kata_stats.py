"""
Librería con las clases necesarias para representar una kata.
"""
from dataclasses import dataclass
from datetime import date
from enum import Enum


@dataclass
class KataComplexity(Enum):
    """
    Cada Kata posee una complejidad que se mide en niveles KYU y DAN.
    """
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
    """
    Una kata se puede resolver en varios lenguajes.
    Esta clase ayuda a crear instancias por cada lenguaje y las veces que se ha completado la kata
    en dicho lenguaje de programación.
    """
    programming_language: str
    total_completions: int


@dataclass
class KataStats:
    """
    Clase para representar las estadísticas y propiedades de kada Kata.
    """
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

    def get_csv_row_representation(self) -> str:
        """
        Método para obtener la representación de una kata como una fila string en el fichero csv.
        :return: string con la representación de la kata en forma de una fila en el CSV.
        """
        return f"{self.id};;" \
               f"{self.name};;" \
               f"{self.author};;" \
               f"{','.join(self.author_profiles)};;" \
               f"{','.join(self.tags)};;" \
               f"{self.kata_complexity};;" \
               f"{self.published};;" \
               f"{self.warriors_trained};;" \
               f"{self.total_skips};;" \
               f"{self.total_code_submissions};;" \
               f"{self.total_times_completed};;" \
               f"{','.join([f'{lang.programming_language}_{lang.total_completions}' for lang in self.languages_completions])};;" \
               f"{self.total_stars};;" \
               f"{self.positive_feedback};;" \
               f"{self.total_very_satisfied_votes};;" \
               f"{self.total_somewhat_satisfied_votes};;" \
               f"{self.total_not_satisfied_votes};;" \
               f"{self.total_rank_assessments};;" \
               f"{self.average_assessed_rank};;" \
               f"{self.highest_assessed_rank};;" \
               f"{self.lowest_assessed_rank}"
