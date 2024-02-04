import json

import pytest


@pytest.fixture
def list_vacancy():
    return [Vacancy("Дворник", "47850", "https://www.superjob.ru/vakansii/dvornik-46198639.html",
                    "Уборка уличной территории прилегающей к зданию"),
            Vacancy("Рабочий по благоустройству территории, дворник", "50000",
                    "https://www.superjob.ru/vakansii/rabochij-po-blagoustrojstvu-territorii-45425114.html",
                    "уборка улиц, тротуаров, участков и площадей")]


from moduls.vacancies import Vacancy
from src.utils import search_hh, search_sj, search_vacancy, load_file, write_file, delete_vacancies, sorted_vacancies, \
    search_keywords


def test_search_hh():
    data = search_hh("дворник")
    assert isinstance(data[0], Vacancy)


def test_search_sj():
    data = search_sj("дворник")
    assert isinstance(data[0], Vacancy)


def test_search_vacancy():
    hh = search_vacancy("дворник", 1)
    assert isinstance(hh[0], Vacancy)

    sj = search_vacancy("дворник", 2)
    assert isinstance(sj[0], Vacancy)

    hh_sj = search_vacancy("дворник", 3)
    assert isinstance(hh_sj[0], Vacancy)


def test_load_file():
    data = load_file("tests/test_vacancies.json")
    assert isinstance(data[0], Vacancy)


def test_write_file(list_vacancy):
    path = "tests/test_write.json"

    write_file(path, list_vacancy)

    with open(path, 'r', encoding='utf-8') as file:
        r_data = json.load(file)

    assert r_data[0]["name_vacancy"] == "Дворник"
    assert r_data[0]["salary"] == 47850
    assert r_data[1]["name_vacancy"] == "Рабочий по благоустройству территории, дворник"
    assert r_data[1]["salary"] == 50000


def test_delete_vacancies(list_vacancy):
    path = "tests/test_delete.json"

    write_file(path, list_vacancy)
    delete_vacancies(path, ["Дворник"])

    with open(path, 'r', encoding='utf-8') as file:
        r_data = json.load(file)

    assert len(r_data) == 1


def test_sorted_vacancies(list_vacancy):
    result = sorted_vacancies(list_vacancy, 2)
    assert result[0].salary == 50000
    assert result[1].salary == 47850


def test_search_keywords(list_vacancy):
    path = "tests/test_write.json"
    search_data = search_keywords(path, ["Дворник"])

    assert search_data[0].name_vacancy == "Дворник"
