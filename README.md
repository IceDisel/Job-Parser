## Поиск вакансий

Этот проект ищет вакансии в Москве.
Можно получать информацию о вакансиях с платформ [HH.ru](https://hh.ru/) и [SuperJob.ru](https://superjob.ru/) в России, сохранять ее в файл и позволять удобно работать с ней (сохранять в файл, фильтровать, удалять).

### Как установить
Для того чтобы запустить программу, вам нужно будет получить свой токен 'SuperJob', это можно сделать на сайте [API SuperJob](https://api.superjob.ru), при регистрации приложения от вас потребуют указать сайт, введите любой, они не проверяют. 

После получения токена нужно будет создать файл `.env` или переименовать существующий файл `.env_exemple` в `.env`, в нём сделать переменную и положить в неё токен. 

Пример `.env` файла:
```
SJ_TOKEN=dw13jhfgfdufimcjhbwofghgfhtrfhgay2dsw132ihd34wef #ваш SuperJob token
```

В файле config.py можно указать id городов.

Пример `config.py` файла:
```text
PATH_FILE = "vacancies.json"

AREA = 1  # id города поиска для HeadHunter
TOWN = 4  # id/название города поиска для SuperJob

TOP_N = 5  # вывод топ N вакансий
```

id городов для HeadHunter - [здесь](https://api.hh.ru/areas).

id городов для SuperJob - [здесь](https://api.superjob.ru/2.0/towns).

Рекомендуется использовать POETRY для изоляции проекта.

Python3.10 уже должен быть установлен,
затем используйте poetry для установки зависимостей

### Как запустить 
Для того чтобы запустить код, в консоли нужно прописать `cd` и название папки, в которой находится `main.py`. После этого нужно прописать `python` и через пробел `main.py`.

Пример запуска:
```
python main.py
```

### Цель проекта
Код написан в образовательных целях


## Тестирование проекта
```text
---------- coverage: platform win32, python 3.10.9-final-0 -----------
Name                          Stmts   Miss  Cover                     
-------------------------------------------------                     
moduls\__init__.py                0      0   100%
moduls\api_connector.py          34      2    94%
moduls\file_manager.py           40      7    82%
moduls\vacancies.py              27      0   100%
src\__init__.py                   0      0   100%
src\config.py                     4      0   100%
src\utils.py                     51      0   100%
tests\__init__.py                 0      0   100%
tests\test_api_connector.py      20      0   100%
tests\test_utils.py              47      0   100%
tests\test_vacancies.py          18      0   100%
-------------------------------------------------
TOTAL                           241      9    96%

```