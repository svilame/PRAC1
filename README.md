# PRAC1
Práctica1 Tipología

# 1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique por qué el sitio web elegido proporciona dicha información.

El conjunto de datos recoge información sobre diferentes ejercicos de programación para fomentar o desarrollar habilidades y competencias.

## Utilidades
* Obtener información sobre tracción del lenguaje de programación en el mercado.
* Análisis estadístico descriptivo del sector del desarrollo del software.
* Comparativa entre rendimiento, potencia y evolución de los diferenetes lenguajes de programación.
* Acceso a información valiosa sobre perfiles expertos en los lenguajes de interés para una empresa.

# 2. Definir un título para el dataset. Elegir un título que sea descriptivo.

Katas de programación y sus estadísticas.

# 3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos que se ha extraído (es necesario que esta descripción tenga sentido con el título elegido).

Conjunto de datos que recolecta información sobre las katas de programación recientemente resueltas en la plataforma `CodeWars` en los lenguajes [a rellenar]

# 4. Representación gráfica. Presentar esquema o diagrama que identifique el dataset visualmente y el proyecto elegido.

*undraw* estadisticas + competicion + karate + leaderboard.

# 5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de los datos y cómo se ha recogido.

El dataset incluye una línea para cada kata con los campos que se listan a continuación.

* id_kata
* name
* author
* author_profiles
* tags
* kata_complexity
* published
* warriors_trained
* total_skips
* total_code_submissions
* total_times_completed

* languages_completions

* total_stars
* positive_feedback
* total_very_satisfied_votes
* total_somewhat_satisfied_votes
* total_not_satisfied_votes
* total_rank_assessments
* average_assessed_rank
* highest_assessed_rank
* lowest_assessed_rank

Se debe tener en cuenta que ciertas columnas forman una lista variable de elementos, como puede pasar con las columnas `author_profiles`, `tags` y `languages_completions`. En estos casos se usa la siguiente notación:

```bash
author_profiles = [author_1_uri, author_2_uri]

tags = [tag_1, tag_2]

languages_completions = [(language_1, total_times_completed), (language_2, total_times_completed)]
```

Dado que no es posible obtener información con respecto a la fecha de la subida de soluciones a la kata en cuestión, se ha decidido obtener las `3000` katas más recientes (en cuanto a resolución) de los 8 niveles de dificultad existentes.

# 6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario incluir citas de análisis anteriores o, en caso de no haberlas, justificar esta búsqueda con análisis similares.

Los datos han sido obtenidos de la plataforma Codewars. Se trata de una comunidad web que nace como el esfuerzo colaborativo de usuarios que desinteresadamente aportan katas de entrenamiento, soluciones a las mismas y feedback constructivo. Este servicio ilumina a la comunidad de desarrollades y les ayude a crecer profesionalmente en su campo de conocimiento.

INCLUIR CITAS DE ANALISIS ANTERIORES
https://www.tiobe.com/tiobe-index/

https://www.somostet.com/2020/07/13/top-10-de-las-tecnologias-mas-populares-del-2020-segun-stack-overflow-parte-1/


# 7. Inspiración. Explique por qué es interesante este conjunto de datos y qué preguntas se pretenden responder. Es necesario comparar con los análisis anteriores presentados en el apartado 6.

Los estudios citados en el apartado anterior permiten conocer la evolucion temporal del uso de los lenguajes de programación. El dataset obtenido proporciona además respuesta a las siguientes preguntas:

- ¿Qué lenguajes de programación son los preferidos para competir?
- ¿Cuál es el reparto porcentual de usuarios por lenguaje de programación?
- ¿Cómo se distribuyen los desarrolladores según complejidad de las katas?
- `analisis estadistico descriptivo`
- Soy una empresa de desarrollo de software o un profesional en RRHH ¿Qué perfiles son los más interesantes para la contratación?


# 8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo de su selección:

* Released Under CC0: Public Domain License
* Released Under CC BY-NC-SA 4.0 License
* Released Under CC BY-SA 4.0 License
* Database released under Open Database License individual contents under Database Contents License
* Other (specified above)
* Unknown License

Se ha decidido hacer uso de la licencia **GPLv3** recomendado por la [Free Software Foundation. (FSF)](https://www.gnu.org/licenses/license-recommendations.html). Nos interesa especialmente por las libertades que la misma ofrece a los usuarios. Se permite su distribución, se reconoce el autor de la obra, se permite editar el código fuente, incluso lucrarse economicamente con el mismo. No obstante, no se permite privatizar el software con una licencia que altere las libertades anteriormente expuestas.

# 9. Código. Adjuntar el código con el que se ha generado el dataset, preferiblemente en Python o, alternativamente, en R.

# 10. Dataset. Publicación del dataset en formato CSV en Zenodo (obtención del DOI) con una breve descripción.
