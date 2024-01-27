import json

import requests


class HeadHunterAPI:
    def __init__(self):
        pass

    def get_vacancies(self, search_text):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': search_text,
            # 'exclude': exclude_text,
            'search_field': 'name',
            'area': 1,
            'period': 1,
            'only_with_salary': True,
            'per_page': 100,
            'page': 0
        }

        response = requests.get(url, params=params)
        data = response.json()
        with open("work.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(data)
