import json

numbers = [2, 3, 5, 7, 11, 13, 15]

file_name = 'numbers.json'
with open(file_name, 'w') as my_f:
    json.dump(numbers, my_f)