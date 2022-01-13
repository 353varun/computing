#ans 1
print("soln. of first quest.")
print("  ")


print("enter first no.")
n1=input()
print("enter second no.")
n2=input()
print("enter third no.")
n3=input()
print("average =",(int(n1)+int(n2)+int(n3))/3)
print("  ")

#ques 2
print("soln. of second ques.")
print("  ")

print("enter gross income")
inc=float(input())#inc=gross income

print("enter no. of dependents")
n=int(input())  #n=no. of dependents

sd=10000    #sd=standard deduction
ad=3000    #as=additional deduction

taxable_income=inc-sd-(ad*n)
print("taxable income=",taxable_income)

print("tax=",taxable_income*0.2)
print("  ")

#ques 3
print("soln. of third ques.")
print("  ")

print("SID")
x=int(input())
print("Name")
n=input()
print("Gender\n 'M'for male\n 'F' for female\n 'U' for unknown")
g=input()
print("course name")
c=input()
print("CGPA")
cg=float(input())

student=[x,n,g,c,cg]
print(student)
print("  ")


#ques4(done)
print("soln. of fourth ques.")
print("  ")

print("enter marks of first student")
m1=int(input())
print("enter marks of second student")
m2=int(input())
print("enter marks of third student")
m3=int(input())
print("enter marks of fourth student")
m4=int(input())
print("enter marks of fifth student")
m5=int(input())

marks=[m1,m2,m3,m4,m5]
marks.sort()
print(marks)
print("  ")


#ques 5
print("soln. of fourth ques.")
print("  ")

#a part
print("part a)")


color =["Red","Green","White","Black","Pink","Yellow"]
color.remove("Black")
print(color)


#b part
print("part b)")


color =["Red","Green","White","Black","Pink","Yellow"]
color[3:5] = ['purple']
print(color)










