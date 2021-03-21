# Práctica1 Tipología

## Descripción

Esta práctica se ha realizado dentro de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web Codewars y generar un dataset.

## Miembros del equipo

La actividad ha sido realizada de manera conjunta por Eleazar Morales Díaz y Susana Vila Melero.

## Código fuente
* `./get_all_katas_ids.py`: Script que obtiene todos los ids de las katas de programación que se encuentran en el servicio web [Codewars](https://www.codewars.com/) y los almacena en el fichero `data/katas.txt`.
* `./get_all_katas_data.py`: Script que lee el fichero `data/katas.txt`, en el cual obtiene los ids con los que extrae la información de estadísticas para cada una de las katas. Cada kata se escribe en un registro del fichero `data/katas.csv` en donde cada columna se separa con la combinación de caracteres `;;`. Esta decisión ha sido necesaria pues tras obtener en un primer intento todas las katas descubrimos que 3 de ellas poseían el caracter `;`, lo cual rompía el sistema de separación de columnas original.
* `src/library.py`: Clase de ayuda con métodos estáticos para realizar el raspado de los ids de las katas de una página en concreto. De cada página podemos extraer 30 ids de katas diferentes.
* `src/codewars_scrapper.py`: Clase de ayuda con métodos estáticos para obtener toda la información de un kata en específico.
* `src/kata_stats.py`: Conjuntos de clases que generan los objetos kata con sus estadísticas. `KataComplexity`, `LanguageCompletions` y `KataStats`.

## Datos
* `data/katas.csv`: dataset con la información a detalle de cada kata.
* `data/katas.txt`: dataset con los ids de todas las katas que existen en la plataforma en el momento del raspado.

## Documentación
* `docs/Practica1.rmd`: reporte final de la práctica en formato RMarkdown.
* `docs/Practica1.pdf`: reporte final de la práctica en formato PDF.

## Recursos

* Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
* Masip, D. (2010). El lenguaje Python. Editorial UOC.
* Tutorial de Github https://guides.github.com/activities/hello-world.
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
