#question 1

def TowerOfHanoi(n, source, auxiliary, destination):
    if n==0:
        return
    
    TowerOfHanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, source, destination)
    
print(TowerOfHanoi(3, 'A', 'B', 'C'))

print(" ")


#question 2


n=int(input("Enter the number of lines of pascal triangle\n"))
#By recursion
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)  
def pas_tr(x):
    if x>=0:
        print(" "*(x), end="")
        def row(r):
           if r>=0:
               print(factorial(n-1-x)//(factorial(r)*factorial(n-1-x-r)), end=' ')
               row(r-1)
           else:
               print()
        row(n-1-x)
        pas_tr(x-1)
if n>0:
    pas_tr(n-1)   
else:
    print("Invalid input") 
print(" ")

#By loops
if n>0:    
    for i in range(n):
        print(" "*(n-i-1), end="")
        if i==0 :
            print('1', end='')
        elif i>0 :
            for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')
        print()        
else:
    print("Invalid input")

print(" ")
#question 3

first_no=float(input("Enter the first number:\n"))
second_no=float(input("Enter the second number:\n"))

if second_no!=0 :
#a)part
    print("\nFunction is callable.")
    quot,rem=divmod(first_no,second_no)
    print(f"Quotient obtained={quot}\nRemainder obtained={rem:.2f}\n")
#b)part
    if quot==0 :
        if rem==0 :
            print("Both value are zero.")
        else:
            print("Quotient is zero.")
            print("Reminder is non-zero.")
    else:
        
        if rem!=0 :
            print("Values are non-zero")
        else :
            print("Quotient is non-zero")
            print("Reminder is zero.")
#c)part
    lt=(quot, rem)+(4, 5, 6)
    print(lt)
    lt1=[]
    for i in lt:
        if i>4 :
            lt1.append(i)
    print("\nThe values which are greater than 4 are:", lt1)
#d)part
    print("\nConversion to set datatype:", set(lt1))
#e)part
    st=frozenset(lt1)
    print("\nMaking  the set immutable:", st)
#f)part
    print("\nThe maximum value from set is:", max(st))
    print("The hash value for the maximum value:", hash(max(st)))
else:
    print("Function is not callable.")

print(" ")

#question 4

class Student:
    def __init__(self,name, roll_num):
        self.name=name
        self.roll_num=roll_num

stu=Student('varun','45')
print(stu.name)
print(stu.roll_num)

#destroying the object

del stu

print(" ")

#question 5

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def details(self):
        print(f"{self.name}\t{self.salary}")
        
# storing details of employees

emp1=Employee('Mehak', 40000)
emp2=Employee('Ashok', 50000)
emp3=Employee('Viren', 60000)
print("Name\tSalary")
emp1.details()
emp2.details()
emp3.details()

# updating salary

emp1.salary=70000
print("\nThe updated table")
print("Name\tSalary")
emp1.details()
emp2.details()
emp3.details()

#deleting the record of Viren

del emp3
print("Record of Viren is deleted.")
    
print(" ")
#question 6

george_word=input('word uttered by George:\n').lower()
barbie_word=input('word spoken by Barbie:\n').lower()
l1=list(george_word.replace(' ', ''))
l2=list(barbie_word.replace(' ', ''))
if sorted(l1)==sorted(l2):
    print("True friendship.")
else:
    print("Friendship is fake.")


