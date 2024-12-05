# TODO решите задачу
import json
filename = "input.json"

def task() -> float:
    total = 0
    with open(filename, encoding="utf-8") as file:
        json_data = json.load(file)  # TODO считать содержимое JSON файла
    # return max(json_data, key=lambda p: p["score"])
        #print(json_data)
        for scores in json_data:
            total += scores["score"]*scores["weight"]
            #print(total)
    return round(total,3)
print(task())
