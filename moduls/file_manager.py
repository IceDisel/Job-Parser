import json
from abc import ABC, abstractmethod
from typing import Any


class AbstractManager(ABC):
    """
    Абстрактный класс для управления данными в файлах.
    """
    @abstractmethod
    def __init__(self, path: str) -> None:
        """
        Абстрактный метод инициализации менеджера.
        :param path: Путь до файла
        """
        raise NotImplementedError

    @abstractmethod
    def read(self) -> list[dict]:
        """
        Абстрактный метод для чтения данных.
        :return: Список
        """
        raise NotImplementedError

    @abstractmethod
    def write(self, data: list[dict]) -> None:
        """
        Абстрактный метод для записи данных.
        :param data: Список
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, keywords: list[str]) -> list[dict]:
        """
        Абстрактный метод для получения данных по ключевым словам.
        :param keywords: Ключевые слова
        :return: Список
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, keywords_remove: list[str]) -> None:
        """
        Абстрактный метод для удаления данных по ключевым словам.
        :param keywords_remove: Ключевые слова
        :return: None
        """
        raise NotImplementedError


class JsonManager(AbstractManager):
    """
    Класс для управления данными в формате JSON.
    """
    def __init__(self, path: str) -> None:
        """
        Инициализация менеджера JsonManager.
        :param path: Путь до файла
        """
        self.path = path

    def read(self) -> Any:
        """
        Чтение данных из файла JSON.
        :return: Список данных
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Файл {self.path} не найден")
        return data

    def write(self, data: list[dict]) -> None:
        """
        Запись данных в файл JSON.
        :param data: Список данных
        :return: None
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get(self, keywords: list[str]) -> list[dict]:
        """
        Получение данных по ключевым словам из файла JSON.
        :param keywords: Ключевые слова
        :return: Список данных
        """
        data = self.read()
        matching_vacancies = [vacancy for vacancy in data if all(keyword in vacancy['name_vacancy']
                                                                 or (vacancy['requirement']
                                                                     and keyword in vacancy['requirement']) for keyword
                                                                 in keywords)]

        return matching_vacancies

    def delete(self, keywords_remove: list[str]) -> None:
        """
        Удаление данных по ключевым словам из файла JSON.
        :param keywords_remove: Ключевые слова
        :return: None
        """
        data = self.read()
        cleaned_data = [vacancy for vacancy in data if not all(
            keyword in vacancy['name_vacancy'] or keyword in vacancy['requirement'] for keyword in keywords_remove)]
        self.write(cleaned_data)
