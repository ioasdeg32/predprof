import csv
import random
import string


def create_password() -> str:
    """
    Функция для генерации пароля. Алфавит - английские буквы, а также цифры
    :return: возвращает сгенерированный пароль
    """

    alphabet = string.ascii_letters + string.digits
    return "".join([random.choice(alphabet) for _ in range(8)])


def is_valid_password(password: str) -> bool:
    """
    Функция для проверки пароля на соответствие условиям
    :param password: пароль в виде строки
    :return: True, если пароль соответствует условиям, иначе False
    """

    flags = [False, False, False]

    for i in password:
        if i in string.ascii_lowercase:
            flags[0] = True
        elif i in string.ascii_uppercase:
            flags[1] = True
        else:
            flags[2] = True

    return all(flags)


def main() -> None:
    """
    основная функция программы
    :return: None
    """

    with open("students.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))

    with open("students_passwords.csv", mode="w") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(reader[0])

        for row in reader[1:]:
            password = create_password()
            while not is_valid_password(password):
                password = create_password()

            login = row[1].split()
            login = login[0] + "_" + login[1][0] + login[2][0]
            writer.writerow(row + [login, password])


main()
