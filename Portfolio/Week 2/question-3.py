#a program that prompts for the number of students and group size, and then displays how many groups will be needed and how many will be left over in a smaller group.
num=int(input("How many students? "))
size=int(input("Required group size? "))
count=0
leftover=0
while True:
    if num>=size:
        count+=1
        num-=size
    else:
        leftover=num
        break
if count<2:
    if leftover<2:
        print(f"There will be {count} group and {leftover} student left over.")
    else:
        print(f"There will be {count} group and {leftover} students left over.")
else:
    if leftover<2:
        print(f"There will be {count} groups and {leftover} student left over.")
    else:
        print(f"There will be {count} groups and {leftover} students left over.")
