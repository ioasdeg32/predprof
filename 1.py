import csv


def main() -> None:
    """
    основная функция программы
    :return: None
    """

    with open("students.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))
        classes = dict()

        for row in reader[1:]:
            score = int(row[4]) if row[4] != "None" else 0

            if "Хадаров Владимир" in row[1]:
                print(f"Ты получил: {score}, за проект {row[2]}")

            if row[3] in classes.keys():
                classes[row[3]] = (classes[row[3]][0] + score, classes[row[3]][1] + 1)
            else:
                classes[row[3]] = (score, 1)

        classes = {i: round(classes[i][0] / classes[i][1], ndigits=3) for i in classes.keys()}

        with open("students_new.csv", mode="w") as output_file:
            writer = csv.writer(output_file, delimiter=",")

            for row in reader:
                if row[4] != "None":
                    writer.writerow(row)
                else:
                    writer.writerow(row[:-1] + [classes[row[3]]])


main()
