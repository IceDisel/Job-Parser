from src.config import PATH_FILE, TOP_N
from src.utils import search_vacancy, load_file, write_file, sorted_vacancies, search_keywords, delete_vacancies


def user_interaction() -> None:
    """
    Взаимодействие с пользователем для поиска, анализа и управления вакансиями.
    :return: None
    """
    mode = 0
    while True:
        user_choice = input("Начать поиск вакансий или загрузить из файла для анализа?\n"
                            "'1' - Поиск,\n'2' - Загрузить,\n'0' - Выход\n -> ")

        if user_choice == '1':
            mode_choice = input("Поиск вакансий на:\n'1' - HH.ru,\n"
                                "'2' - SuperJob.ru,\n'3' - HH.ru + SuperJob.ru\n -> ")
            if mode_choice == '1':
                mode = 1
            elif mode_choice == '2':
                mode = 2
            query = input("Введи поисковой запрос: - ") or "уборщица"
            list_vacancies = search_vacancy(query, mode=mode)
            for vacancy in list_vacancies:
                print(f"{vacancy}\n")

            user_choice = input(
                "Записать найденные вакансии в файл?\n'1' - Да,\n'2' - Нет,\n'0' - Выход\n -> ")

            if user_choice == '2' or user_choice == '0':
                break
            else:
                write_file(PATH_FILE, list_vacancies)

        elif user_choice == '2':
            list_vacancies = load_file(PATH_FILE)

            while True:
                user_choice = input(f"Анализ вакансий, выбери:\n"
                                    f"'1' - Вывести весь список,\n'2' - Отсортировать по зарплате топ {TOP_N},\n"
                                    f"'3' - Вывести по ключевым словам,\n'4' - Удалить по ключевым словам,\n"
                                    f"'0' - Выход \n -> ")

                if user_choice == '1':
                    for vacancy in list_vacancies:
                        print(f"{vacancy}\n")

                elif user_choice == '2':
                    sort_vacancies = sorted_vacancies(list_vacancies, TOP_N)
                    for vacancy in sort_vacancies:
                        print(f"{vacancy}\n")

                elif user_choice == '3':
                    keywords_input = input("Введите ключевые слова для поиска: - ")
                    keywords = keywords_input.split()
                    matching_vacancies = search_keywords(PATH_FILE, keywords)
                    for vacancy in matching_vacancies:
                        print(f"{vacancy}\n")

                elif user_choice == '4':
                    keywords_input = input("Введите ключевые слова для удаления вакансий из файла: - ")
                    keywords = keywords_input.split()
                    delete_vacancies(PATH_FILE, keywords)
                    print("Данные удалены")

                elif user_choice == '0':
                    exit()

                else:
                    print("Ты ввел не верное значение, повтори еще")

        elif user_choice == "0":
            break
        else:
            print("Ты ввел не верное значение, повтори еще")
            continue


if __name__ == "__main__":
    user_interaction()
