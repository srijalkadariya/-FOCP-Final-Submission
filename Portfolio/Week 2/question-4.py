#a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
pupils=int(input("Enter the number of pupils: "))
chocolate=int(input("Enter the number of chocolate: "))
count=0
leftover=0
while True:
    if chocolate>=pupils:
        count+=1
        chocolate-=pupils
    else:
        leftover=chocolate
        break
print(f"Each pupil will recieve {count} chocolate and {leftover} leftover.")