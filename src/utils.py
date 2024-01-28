from moduls.api_connector import HeadHunterAPI, SuperJobAPI
from moduls.file_manager import JsonManager
from moduls.vacancies import Vacancy
from src.config import AREA, TOWN


def search_vacancy(query: str, mode: int) -> list[Vacancy]:
    """
    Поиск вакансий в соответствии с режимом.
    :param query: Поисковый запрос.
    :param mode: Режим поиска (1 - HeadHunter, 2 - SuperJob, 3 - оба).
    :return: Список найденных вакансий.
    """
    def search_hh(query_hh: str) -> list[Vacancy]:
        hh_api = HeadHunterAPI(query_hh, AREA)
        data_hh = hh_api.get_vacancies()

        list_hh = []

        for item in data_hh:
            list_hh.append(
                Vacancy(item['name'], item['salary']['from'], item['alternate_url'], item['snippet']['requirement']))
        return list_hh

    def search_sj(query_sj: str) -> list[Vacancy]:
        sj_api = SuperJobAPI(query_sj, TOWN)
        data_sj = sj_api.get_vacancies()

        list_sj = []

        for item in data_sj:
            list_sj.append(Vacancy(item['profession'], item['payment_from'], item['link'], item['candidat']))
        return list_sj

    if mode == 1:
        list_vacancies = search_hh(query)
    elif mode == 2:
        list_vacancies = search_sj(query)
    else:
        list_vacancies = search_hh(query) + search_sj(query)

    return list_vacancies


def load_file(path: str) -> list[Vacancy]:
    """
    Загрузка данных о вакансиях из файла.
    :param path: Путь к файлу.
    :return: Список вакансий из файла.
    """
    jsonfile = JsonManager(path)
    data = jsonfile.read()
    list_vacancies = []
    for item in data:
        list_vacancies.append(
            Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))

    return list_vacancies


def write_file(path: str, data: list[Vacancy]) -> None:
    """
    Запись данных о вакансиях в файл.
    :param path: Путь к файлу.
    :param data: Список вакансий для записи.
    :return: None
    """
    jsonfile = JsonManager(path)
    list_vacancies = []
    for item in data:
        dict_vacancy = {
            'name_vacancy': item.name_vacancy,
            'salary': item.salary,
            'url': item.url,
            'requirement': item.requirement
        }
        list_vacancies.append(dict_vacancy)

    jsonfile.write(list_vacancies)


def sorted_vacancies(data: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Сортировка списка вакансий по зарплате.
    :param data: Список вакансий.
    :param top_n: Количество вакансий для вывода.
    :return: Отсортированный список вакансий.
    """
    return sorted(data, reverse=True)[:top_n]


def search_keywords(path: str, keywords: list[str]) -> list[Vacancy]:
    """
    Поиск вакансий по ключевым словам.
    :param path: Путь к файлу.
    :param keywords: Список ключевых слов.
    :return: Список найденных вакансий.
    """
    json_file = JsonManager(path)
    matching_vacancies = json_file.get(keywords)
    list_vacancies = []
    for item in matching_vacancies:
        list_vacancies.append(
            Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))

    return list_vacancies


def delete_vacancies(path: str, keywords_remove: list[str]) -> None:
    """
    Удаление вакансий по ключевым словам.
    :param path: Путь к файлу.
    :param keywords_remove: Список ключевых слов для удаления.
    :return: None
    """
    json_file = JsonManager(path)
    json_file.delete(keywords_remove)
