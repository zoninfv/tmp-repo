# TODO импортировать необходимые модули


import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    a=list()
    with open ("input.csv") as f:
        reader = csv.DictReader(f, delimiter  = ",", lineterminator  = "\n")
        for line in reader:  # TODO считать содержимое csv файла
            # a.append (json.dumps(line, indent=4))
            a.append(line)
            json1=json.dumps(a, indent=4)
            #print(','.join(a))
    print(json1, end="")
            # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    #with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        #for line in output_f:
           # print(line, end="")
