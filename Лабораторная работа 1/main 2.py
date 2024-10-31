from os.path import split

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players = len(list_players)
print(list_players[(players // 2):])

print(list_players[:(players // 2)])
