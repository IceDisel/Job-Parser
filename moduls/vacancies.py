class Vacancy:
    def __init__(self, name_vacancy, salary, url, requirement):
        self.__name_vacancy = name_vacancy
        self.__salary = 0 if salary is None else int(salary)
        self.__url = url
        self.__requirement = requirement

    @property
    def name_vacancy(self):
        return self.__name_vacancy

    @property
    def salary(self):
        return self.__salary

    @property
    def url(self):
        return self.__url

    @property
    def requirement(self):
        return self.__requirement

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __str__(self):
        return f"{self.__name_vacancy}, Зарплата: {self.__salary}, Требования: {self.__requirement} {self.__url}"
