import json

file_name = 'numbers.json'
with open(file_name) as my2_f:
    numbers = json.load(my2_f)
    print(numbers)