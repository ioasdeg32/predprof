import csv


def main() -> None:
    """
    основная функция программы
    :return: None
    """

    with open("students.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))[1:]

        id_proj = input()
        while id_proj != "СТОП":
            flg = True

            for row in reader:
                if row[2] == id_proj:
                    flg = False
                    x = row[1].split()[:2]
                    x = x[1][0] + ". " + x[0]

                    print(f"Проект №{id_proj} делал(а): {x}, он(а) получил(а) оценку - {row[4]}")
            if flg:
                print("Ничего не найдено")
            id_proj = input()


main()
