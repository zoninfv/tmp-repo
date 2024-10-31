from os import remove

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0
print (numbers)

total = sum(numbers)
count = len(numbers)
average = total / count
print (average)