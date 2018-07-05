file_name = 'txt_files/programming.txt'
with open(file_name, 'w') as my_file:
    my_file.write("Shaaaloooom.")
"""
files_names = 'txt_files/guest.txt'
guest_name = input("Your name: ")
texts = "waouw"
with open(files_names, 'a') as f2:
    f2.write( guest_name)

while True:
    files_names = 'txt_files/guest.txt'
    real_guest_name = input("Fak-Your name: ")
    print("ooo, shalloom")
    with open(files_names, 'a') as af2:
        af2.write(real_guest_name + "\n ")
    if real_guest_name == 'yes':
        break
"""


cats = ['tuz1', 'sam2', 'vas']
dogs = ['gavs1', 'docs2', 'nush']
task10_file = 'txt_files/cats.txt'
task11_file = 'txt_files/dogs.txt'

with open(task10_file, 'w') as t10_file:
    for cat in cats:
        t10_file.write(cat + "\n")

with open(task11_file, 'w') as t11_file:
    for dog in dogs:
        t11_file.write(dog + "\n")