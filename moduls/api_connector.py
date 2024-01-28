import json
import os
from abc import ABC, abstractmethod

import requests

from dotenv import load_dotenv

from src.config import TOWN

load_dotenv()


class AbstractConnector(ABC):
    @abstractmethod
    def __init__(self, search_text):
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self):
        raise NotImplementedError


class HeadHunterAPI(AbstractConnector):
    def __init__(self, search_text, area):
        self.search_text = search_text
        self.area = area

    def get_vacancies(self):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.search_text,
            'search_field': 'name',
            'area': self.area,
            'period': 1,
            'only_with_salary': True,
            'per_page': 100,
            'page': 0
        }

        response = requests.get(url, params=params)
        data = response.json()

        return data['items']


class SuperJobAPI(AbstractConnector):
    def __init__(self, search_text, town):
        self.sj_token = os.getenv('SJ_TOKEN')
        self.search_text = search_text
        self.town = town

    def get_vacancies(self):
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
