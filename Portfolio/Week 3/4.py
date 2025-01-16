#Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
BAD_PASSWORDS = ['password', 'Srijal', 'apple', 'mango', 'hello']
BAD_PASSWORDS = ['password', 'Srijal', 'apple', 'mango', 'hello']
def password():
    pw1=input("Enter a new password: ")
    if pw1 in BAD_PASSWORDS:
        print("Error: Password id too common. Try again")
    if len(pw1)<8 or len(pw1)>12:
        print("Error: Password must be between 8 to 12 characters")
    pw2=input("Please, confirm your password: ")
    if pw1==pw2:
        print("Password set")
    else:
        print("Error: Password doesn't match")

password()