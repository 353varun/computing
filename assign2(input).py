#solution of question 1
string=("Python is a case sensitive language")

#a) part
print(len(string))

#b) part
print(string[::-1])

#c) part
string2=string[10:27]
print(string2)

#d) part
print(string.replace("a case sensitive","object oriented"))

#e) part
print(string.index("a"))

#f) part
print(string.replace(" ",""))


#solution of question 2

print(" ")
name="varun sharma"
SID= 21104110
dep="Electrical Engineering"
CGPA=9.9

print("Hey, ",name,"Here!\n""My SID is ",SID ,"\nI am from ",dep," Department and my CGPA is ",CGPA)

#solution of question 3

print(" ")
a=56
b=10
#a part
print(a&b)
#b part
print(a|b)
#c part
print(a^b)
#d part
print(a<<2, b<<2)
#e part
print(a>>2, b>>4)

#solution of question 4

print(" ")
no1=(float(input("enter first no:\n")))
no2=(float(input("enter second no:\n")))
no3=(float(input("enter third no:\n")))

if no1>=no2 and no1>=no3:
    print(no1," is the greatest no.")
elif no2>=no1 and no2>=no3:
    print(no2," is the greatest no.")
else:
    print(no3," is the greatest no.")

#solution of question 5

print(" ")
string=input("enter input string\n")

x=string.find("name")
if x>=0 :
    print("yes")
else:
    print("no")

#solution of question 6

print(" ")
l1=int(input("Enter length of first side\n"))
l2=int(input("Enter length of second side\n"))
l3=int(input("Enter length of third side\n"))

if l1+l2 >l3 and  l2+l3>l1 and l1+l3>l2:
    print("yes")
else:
    print("no")







    

