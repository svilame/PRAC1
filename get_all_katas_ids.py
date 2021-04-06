from datetime import datetime, timedelta
from time import sleep

from src.library import Library

if __name__ == '__main__':
    """
    Script principal que obtiene todos los ids de las katas existentes en la plataforma
    """
    page = 0
    total_katas = 0
    html = Library.download_html(f"https://www.codewars.com/kata/latest?page={page}")
    total_katas = Library.get_total_of_katas(html)
    fixed_total_kata = total_katas

    while total_katas > 0:
        initial_time = datetime.now()
        html = Library.download_html(f"https://www.codewars.com/kata/latest?page={page}")
        interval = datetime.now() - initial_time # para sumar el intervalo de tiempo que tarda en descargar la página
        katas = Library.get_all_katas_id_per_page(html)
        Library.append_kata_id_to_txt('katas.txt', katas)
        total_katas -= len(katas)  # actualizamos el numero de katas leídas por página
        print(f"{fixed_total_kata - total_katas} of {fixed_total_kata} katas retrieved")
        page += 1
        sleep((interval + timedelta(seconds=1)).total_seconds())  # dormimos el proceso para no saturar la web
