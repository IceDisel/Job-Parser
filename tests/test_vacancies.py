import pytest

from moduls.vacancies import Vacancy


@pytest.fixture
def vacancy1() -> Vacancy:
    return Vacancy("Дворник", "47850", "https://www.superjob.ru/vakansii/dvornik-46198639.html",
                   "Уборка уличной территории прилегающей к зданию")


@pytest.fixture
def vacancy2() -> Vacancy:
    return Vacancy("Рабочий по благоустройству территории, дворник", "50000",
                   "https://www.superjob.ru/vakansii/rabochij-po-blagoustrojstvu-territorii-45425114.html",
                   "уборка улиц, тротуаров, участков и площадей")


def test_init(vacancy1: Vacancy) -> None:
    """
    Тест инициализации экземпляра класса.
    :param vacancy1: Экземпляр класса Vacancy.
    :return: None
    """
    assert vacancy1.name_vacancy == "Дворник"
    assert vacancy1.salary == 47850
    assert vacancy1.url == "https://www.superjob.ru/vakansii/dvornik-46198639.html"
    assert vacancy1.requirement == "Уборка уличной территории прилегающей к зданию"


def test_gt_lt(vacancy1: Vacancy, vacancy2: Vacancy) -> None:
    """
    Тест сравнения зарплат экземпляров класса.
    :param vacancy1: Экземпляр класса Vacancy.
    :param vacancy2: Экземпляр класса Vacancy.
    :return: None
    """
    assert (vacancy1 < vacancy2) is True
    assert (vacancy1 > vacancy2) is False


def test_str(vacancy1: Vacancy) -> None:
    """
    Тест вывода данных в строковом состоянии экземпляра класса.
    :param vacancy1: Экземпляр класса Vacancy.
    :return: None
    """
    assert str(vacancy1) == ("Дворник, Зарплата: 47850, Требования: Уборка уличной территории прилегающей к зданию "
                             "https://www.superjob.ru/vakansii/dvornik-46198639.html")
