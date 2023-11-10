#assignment day 1
#1
"""
num= int(input("Enter a number you  want a table of:-"))
print(" the table is:-")
for i in range(1,11):
   print(num,"*",i,"=",num*i)
"""

#2
"""
def vowel_check(c):
    vo_low={'a','e','i','o','u'}
    vo_upp={'A','E','I','O','U'}

    if c in vo_low or c in vo_upp:
        print(c,"is a vowel")
    else:
        print(c,"is not a vowel")

char=input("enter a character:-")
check=vowel_check(char)
"""

#3
"""
i=0
while(i<10):
    i+=1
    print(i)
"""  
#4
"""
i=2
while(i<30):
    i+=1
    if(i==24):
        continue
    print(i)
"""
#5
"""
marks=int(input("Enters the marsk out of 100:-")) 
if(marks>=90):
    print("Distinction")
elif(marks<90 and marks>=70):
    print("First Class")
elif(marks<70 and marks>=60):
    print("Second class")
elif(marks<60 and marks>=40):
    print("Pass")
else:
    print("Fail")
"""
#6
"""
sum=0
for i in range(1,11):
    sum+=i
print("sum of first 10 natural number is:-", sum)
"""
#7
"""
total=0
while True:
    num=int(input("Enter the number(or enter 0 to exit):-"))
    if(num==0):
        break
    total+=num
print("the total of entered number is:-",total)
"""

#8
"""
def char_check(c):
    
    if c.isalpha():
        if c.isupper():
            print("Entered character is a uppercase alphabet")
        else:
             print("Entered character is not an uppercase alphabet")
    else:
        print("Entered character is not an alphabet")
c=input("enter any character you want:-")
char=char_check(c)
"""

########################################################################
#                           Assignment day 2
#1) define 3 functions "add()","modify()" and "delete()" with just a print message.
#now accept input from user as a number. if the number entered is 1, call "add()"
#if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
"""
def add():
    print("add function is called")
def modify():
    print("modify function is called ")
def delete():
    print("delete function is called")

i=int(input("enter your choice (between 1 to 3):"))
match i:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Invalid option choosen")
"""
#2) define a function which accepts a number and return its square.
"""
def square(a):
    c=a*a
    print("square of ",a," is :",c)

i=int(input("enter the number you want the square of:"))
square(i)
"""
#3) define a function which accepts character,int,string and display them.
"""
def display(v1,v2,v3):
    print(v1,v2,v3 )
a=str(input("entet a character:"))
b=str(input("entet a string:"))
c=int(input("entet a Integer:"))
display(a,b,c)
"""

#4) define "myfun1()" with a print statement. now 
#define "myfun2()" which should invoke "myfun1()" function. invoke myfun2()
"""
def myfun1():

    print("this is myfun1 function")
def myfun2(fun):
    fun()

myfun2(myfun1)
"""
#5) define a function to accept a number. This function should return 1 if a number passed is more than 0
#return -1 if a number passed is less than 0 , else it should return 0.
"""
def check_num(num):
    
    if(num>0):
        return 1
    elif(num<0):
        return -1
    else:
        return 0

a=int(input("enter a number:-"))
print(check_num(a))
"""
#6) define a function which accepts a character and return toggle of it.
"""
def char_toggle(ch):
    if (len(ch)==1 and ch.isalpha()):
        return ch.swapcase()
    else:
        return "invalid input"

a=str(input("enter a Alphabet:-"))
print(char_toggle(a))
"""


#7) define a function which accepts a string , toggle and return it.[ hint :  use "swapcase()" function of string ]
"""
def char_toggle(ch):
    if (len(ch)>=2 and ch.isalpha()):
        return ch.swapcase()
    else:
        return "invalid input"

a=str(input("Enter a string:-"))
print(char_toggle(a))
"""

#8) write a function to accept minimum 3 characters and maximum 5 characters. 
# [ use default arguments method ]
"""
def process_string(strs,min=3,max=5):
    if(min<=len(strs)<=max):
        print("Valid String")
    else:
        print("Invalid string")

a=str(input("enter the string:"))
process_string(a)
"""

#9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]
"""
def sumall(*num):
    total=0
    for num in num:
        total+=num
    print("the sum of all elemets is:",total)

elements=[]
while(1):
    ele=int(input("enter the elements to add(put zero to stop):"))
    if(ele==0):
        break
    elements.append(ele)

sumall(*elements)
"""