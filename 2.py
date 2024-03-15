import csv


def insertion_sort(n: list) -> list:
    """
    Реализация сортировки вставками для упорядочивания входной таблицы
    :param n: Входная таблицы
    :return: Отсортированная по столбцу оценки таблица
    """

    for i in range(1, len(n)):
        j = i - 1
        while j >= 0 and int(n[j][4]) < int(n[j + 1][4]):
            n[j], n[j + 1] = n[j + 1], n[j]
            j -= 1
    return n


def main() -> None:
    """
    основная функция программы
    :return: None
    """

    with open("students.csv") as input_file:
        reader = csv.reader(input_file, delimiter=",")

        next(reader)
        sorted_reader = insertion_sort([i for i in reader if "10" in i[3]])

        print("10 класс:")
        for i in range(3):
            x = sorted_reader[i][1].split()[:2]
            x = x[1][0] + ". " + x[0]
            print(f"{i + 1} место: {x}")


main()
