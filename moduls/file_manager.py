import json
from abc import ABC, abstractmethod


class AbstractManager(ABC):
    @abstractmethod
    def __init__(self, path):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, data):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError


class JsonManager(AbstractManager):

    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Файл {self.path} не найден")
        return data

    def write(self, data):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get(self):
        pass

    def delete(self):
        pass
