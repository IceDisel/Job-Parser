from abc import ABC, abstractmethod

import requests


class AbstractConnector(ABC):
    @abstractmethod
    def __init__(self, search_text):
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self):
        raise NotImplementedError


class HeadHunterAPI(AbstractConnector):
    def __init__(self, search_text):
        self.search_text = search_text

    def get_vacancies(self):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.search_text,
            # 'exclude': exclude_text,
            'search_field': 'name',
            'area': 1,
            'period': 1,
            'only_with_salary': True,
            'per_page': 10,
            'page': 0
        }

        response = requests.get(url, params=params)
        data = response.json()

        return data['items']
