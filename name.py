from name_function import get_formatted_name

#training task
print("_"*70)
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
print('Python')
print("\t Rython")
print("_"*70)

#task from page210

print("Enter 'q' at any time to quit.")
while True:

    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
