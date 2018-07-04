"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
"""
while True:
    try:
        firdigit = int(input("1 digit: "))
        secdigit = int(input("2 digit: "))
        result = firdigit + secdigit

    except ValueError:
        print("Loshara!")
    else:
        print(result)

"""
"""
cats = ['tuz', 'sam', 'vas']
dogs = ['gavs', 'docs', 'nush']
task10_file = 'txt_files/cats.txt'
task11_file = 'txt_files/dogs.txt'
task12_file = 'txt_files/gzsh.txt'
with open(task10_file) as f10:
    file10 = f10.read()
    print(file10)
"""
"""
try:
    with open(task11_file) as f11:
        file11 = f11.read()

except FileNotFoundError:
    print("file gde?")
else:
    print(file11)
"""
"""
try:
    with open(task12_file) as f12:
        file12 = f12.read()
        print(file12)
except FileNotFoundError:
    print("File gde, Vasya?")
else:
    print(file12)
"""
"""
try:
    with open(task12_file) as f12:
        file12 = f12.read()
        print(file12)
except FileNotFoundError:
    pass
else:
    print(file12)
"""

filenames = 'txt_files/for_testing.txt'
def count_words(filename, search_word):
    try:
        with open(filename) as f1name:
            context = f1name.read()
    except FileNotFoundError:
        print("Gdeeee?")
    else:
        words = context.split()
        num_words = len(words)
        print(num_words)
        line = context
        count_line = line.count(search_word)
        print(count_line)


count_words(filenames, 'файла')