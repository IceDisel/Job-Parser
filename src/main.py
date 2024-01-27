from moduls.file_manager import JsonManager
from src.config import PATH_FILE
from src.utils import search_vacancy, load_file, write_file, sorted_vacancies, search_keywords


def user_interaction():
    while True:
        user_choice = input("Начать поиск вакансий или загрузить из файла для анализа?"
                            "'1' - Поиск, '2' - Загрузить, '0' - Выход \n")

        if user_choice == '1':
            query = input("Введи поисковой запрос - ")
            list_vacancies = search_vacancy(query)
            for vacancy in list_vacancies:
                print(f"{vacancy}\n")

            user_choice = input(
                "Записать найденные вакансии в файл? '1' - Да, '2' - Нет, '0' - Выход \n")

            if user_choice == '2' or user_choice == '0':
                break
            else:
                write_file(PATH_FILE, list_vacancies)

        elif user_choice == '2':
            list_vacancies = load_file(PATH_FILE)

            while True:
                user_choice = input("Анализ вакансий, выбери: "
                                    "'1' - Вывести весь список, '2' - Отсортировать по зарплате, "
                                    "'3' - Вывести по ключевым словам, 0' - Выход \n")

                if user_choice == '1':
                    for vacancy in list_vacancies:
                        print(f"{vacancy}\n")

                elif user_choice == '2':
                    sort_vacancies = sorted_vacancies(list_vacancies)
                    for vacancy in sort_vacancies:
                        print(f"{vacancy}\n")

                elif user_choice == '3':
                    keywords_input = input("Введите ключевые слова для поиска: ")
                    keywords = keywords_input.split()
                    matching_vacancies = search_keywords(PATH_FILE, keywords)
                    for vacancy in matching_vacancies:
                        print(f"{vacancy}\n")

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
