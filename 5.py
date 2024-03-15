import csv


def generate_hash(string: str) -> int:
    """
    Функция для вычисления хэша строки
    :param string: строка, для которой необходимо вычислить хэш
    :return: возвращает вычисленный хэш
    """

    p = 67
    m = 10 ** 9 + 9

    char_hash = {chr(i): i - 1039 for i in range(1040, 1104)}
    char_hash["ё"] = 65
    char_hash["Ё"] = 66
    char_hash[" "] = 67

    hash_ = 0
    for i in range(len(string)):
        if string[i].isalpha():
            hash_ += (char_hash[string[i]] * p ** i) % m

    return hash_


def main() -> None:
    with open("students.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))

    with open("students_with_hash.csv", mode="w") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(reader[0])

        for row in reader[1:]:
            hash_ = generate_hash(row[1])
            writer.writerow([hash_] + row[1:])


main()
