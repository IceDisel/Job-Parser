import re


class Vacancy:
    """
    Класс для представления вакансии.
    """
    def __init__(self, name_vacancy: str, salary: str, url: str, requirement: str) -> None:
        """
        Инициализация объекта вакансии.
        :param name_vacancy: Название вакансии
        :param salary: Зарплата
        :param url: URL адрес
        :param requirement: Обязанности
        """
        self.__name_vacancy = name_vacancy
        self.__salary = 0 if salary is None else int(salary)
        self.__url = url

        cleaned_string = re.sub(r'<.*?>', '', str(requirement))
        self.__requirement = cleaned_string.replace('\n', ' ')

    @property
    def name_vacancy(self) -> str:
        """
        Метод получение названия вакансии.
        :return: Название вакансии
        """
        return self.__name_vacancy

    @property
    def salary(self) -> int:
        """
        Метод получение зарплаты.
        :return: Зарплата
        """
        return self.__salary

    @property
    def url(self) -> str:
        """
        Метод получение URL вакансии.
        :return: URL вакансии
        """
        return self.__url

    @property
    def requirement(self) -> str:
        """
        Метод получение требований к вакансии.
        :return: Требования к вакансии
        """
        return self.__requirement

    def __gt__(self, other: 'Vacancy') -> bool:
        return self.__salary > other.__salary

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.__salary < other.__salary

    def __str__(self) -> str:
        """
        Представление объекта в виде строки.
        :return: Строковое представление вакансии.
        """
        return f"{self.__name_vacancy}, Зарплата: {self.__salary}, Требования: {self.__requirement} {self.__url}"
