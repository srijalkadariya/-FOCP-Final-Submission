#Modify your greeting program so that if the user does not enter a name (i.e. they just press enter), the program responds "Hello, Stranger!". Otherwise it should print greeting with their name as before.

def user_name():
    name = input("Enter your name: ")
    if name.strip():
        print(f"Hello, {name}!")
    else:
        print(f"Hello, stranger!")

user_name()