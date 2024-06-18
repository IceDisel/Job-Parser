import os
from abc import ABC, abstractmethod

import requests

from dotenv import load_dotenv

load_dotenv()


class AbstractConnector(ABC):
    """
    Абстрактный класс для подключения к API вакансий.
    """
    @abstractmethod
    def __init__(self, search_text: str) -> None:
        """
        Абстрактный метод инициализации
        :param search_text:
        """
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """
        Абстрактный метод для получения списка вакансий.
        :return: Список вакансий
        """
        raise NotImplementedError


class HeadHunterAPI(AbstractConnector):
    """
    Класс для работы с API HeadHunter.
    """
    def __init__(self, search_text: str, area: int) -> None:
        """
        Инициализация полей для API.
        :param search_text: Ключевые слова для поиска
        :param area: Код региона
        """
        self.__search_text = search_text
        self.__area = area

    def get_vacancies(self):
        """
        Получение списка вакансий через API HeadHunter.
        :return: Список вакансий
        """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.__search_text,
            'search_field': 'name',
            'area': self.__area,
            'period': 1,
            'only_with_salary': True,
            'per_page': 100,
            'page': 0
        }

        response = requests.get(url, params=params)
        data = response.json()

        return data['items']


class SuperJobAPI(AbstractConnector):
    """
    Класс для работы с API SuperJob.
    """
    def __init__(self, search_text: str, town: int) -> None:
        """
        Инициализация полей для API.
        :param search_text: Ключевые слова для поиска
        :param town: Код региона
        """
        self.sj_token = os.getenv('SJ_TOKEN')
        self.search_text = search_text
        self.town = town

    def get_vacancies(self):
        """
        Получение списка вакансий через API SuperJob.
        :return: Список вакансий
        """
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'X-Api-App-Id': self.sj_token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'page': 0,
            'town': self.town,
            'keyword': self.search_text
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return data['objects']
