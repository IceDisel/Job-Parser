from moduls.api_connector import HeadHunterAPI
from moduls.file_manager import JsonManager
from moduls.vacancies import Vacancy


def search_vacancy(query):
    hh_api = HeadHunterAPI(query)
    data = hh_api.get_vacancies()

    list_vacancies = []
    for item in data:
        list_vacancies.append(
            Vacancy(item['name'], item['salary']['from'], item['alternate_url'], item['snippet']['requirement']))

    return list_vacancies


def load_file(path):
    jsonfile = JsonManager(path)
    data = jsonfile.read()
    list_vacancies = []
    for item in data:
        list_vacancies.append(
            Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))

    return list_vacancies


def write_file(path, data):
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
    print(list_vacancies)
    jsonfile.write(list_vacancies)


def sorted_vacancies(data):
    return sorted(data, reverse=True)


def search_keywords(path, keywords):
    json_file = JsonManager(path)
    matching_vacancies = json_file.get(keywords)
    list_vacancies = []
    for item in matching_vacancies:
        list_vacancies.append(
            Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))

    return list_vacancies
