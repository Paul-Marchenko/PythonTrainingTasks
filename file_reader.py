with open('txt_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    #print(contents.rstrip())
    print(contents[:100])
    print(len(contents))

with open('txt_files/pi_digits.txt') as file_pi:
    pi_numbers = file_pi.readlines()
"""
row_pi = ' '
for row in pi_numbers:
    row_pi = row_pi + row.strip()
bithday = input("My birthday, form mmddyy: ")
if bithday in row_pi:
    print("It is: " + bithday)
else:
    print("nifiga")
"""
print("_" *50)

with open('txt_files/learning_python txt') as learn_file:
    """
    for line in learn_file:
        print(line)
    """

    for line in learn_file:
        print(line.replace('Python', 'Java'))

    enter_file = learn_file.read()
    #print(enter_file)
    #enter_file = learn_file.readlines()
    #print(enter_file)
    enter_file.replace('Python', 'Java')
    print(enter_file)
