'''
The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is 24 students, since this is the number of PCs in a lab. Write a program that calculates how many groups are needed for the following number of students: 113, 175, 12. Display how many full groups there will be, and how many students will be in the smaller "left over" group.
'''
def check(num):
    number=num
    count=0
    leftover=0
    while True:
        if num>24:
            count+=1
            num-=24
        else:
            leftover=num
            break
    print(f"The number of groups for {number} students is {count} and students in left-over group is {leftover}")
check(113)
check(175)
check(12)