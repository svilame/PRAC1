import os

import requests
from bs4 import BeautifulSoup


class Library:
    """
    Clase que agrupa los métodos estáticos para obtener información del total de katas que hay en la web y sus ids.
    """
    @staticmethod
    def download_html(url) -> str:
        """
        :param url: dirección de la web de búsqueda de katas
        :return: string con el HTML de la web de búsqueda de katas.
        Por cada página se pueden extraer 30 ids de katas aprox.
        """
        return requests.get(url).content

    @staticmethod
    def get_total_of_katas(html: str) -> int:
        selector = '#shell_content > section > div.w-full.md\:w-9\/12.md\:pl-4.pr-0.space-y-2 > p'
        return int(BeautifulSoup(html, features="html.parser").select(selector)[0].text.split(' Kata Found')[0])

    @staticmethod
    def get_all_katas_id_per_page(html: str) -> list[str]:
        selector = '#shell_content > section > div.w-full.md\:w-9\/12.md\:pl-4.pr-0.space-y-2 > div.list-item.kata'
        return [kata.get('id', None) for kata in BeautifulSoup(html, features="html.parser").select(selector)]

    @staticmethod
    def append_kata_id_to_txt(path: str, katas_ids: list[str]):
        """
        It will write all the ids in a file
        :param path: ruta del archivo de salida
        :param katas_ids: lista con los ids de las katas
        """
        mode = 'a' if os.path.exists(path) else 'w'
        with open(path, mode) as f:
            for kata_id in katas_ids:
                f.write(f'{kata_id}{os.linesep}')
