# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(participants1,participants2, sep = ","):
    list1=participants1.split(sep)
    list2=participants2.split(sep)
    list3= []
    for surname in list1:
        if surname in list2:
            list3.append(surname)
    list3.sort()
    return list3
print (find_common_participants(participants_first_group,participants_second_group,sep = "|"))

# TODO Проверьте работу функции с разделителем отличным от запятой
