import pytest

from moduls.api_connector import HeadHunterAPI, SuperJobAPI


@pytest.fixture
def api_hh() -> HeadHunterAPI:
    return HeadHunterAPI("Дворник", 1)


@pytest.fixture
def api_sj() -> SuperJobAPI:
    return SuperJobAPI("Дворник", 4)


def test_init_hh(api_hh: HeadHunterAPI) -> None:
    """
    Тест инициализации экземпляра класса HeadHunterAPI
    и подключение по API
    :param api_hh: Экземпляр класса HeadHunterAPI
    :return: None
    """
    data = api_hh.get_vacancies()
    assert 'name' in data[0].keys()
    assert 'from' in data[0]['salary'].keys()
    assert 'alternate_url' in data[0].keys()
    assert 'requirement' in data[0]['snippet'].keys()


def test_init_sj(api_sj: SuperJobAPI) -> None:
    """
    Тест инициализации экземпляра класса SuperJobAPI
    и подключение по API
    :param api_sj: Экземпляр класса SuperJobAPI
    :return: None
    """
    data = api_sj.get_vacancies()
    assert 'profession' in data[0].keys()
    assert 'payment_from' in data[0].keys()
    assert 'link' in data[0].keys()
    assert 'candidat' in data[0].keys()
