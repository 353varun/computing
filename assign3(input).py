
#ques 1
inp_str =input("enter a string\n")
l1 =inp_str.split()
s=set()
if len(l1)>1:
    for word in l1:
        s.add(word)
    for word in s:
        print("no of occurences of %s ="%(word), inp_str.count(word))
else:
    for i in inp_str.replace(" ",""):
        s.add(i)
    for i in s:
        print("no. of occurences of %s ="%(i),inp_str.count(i))
print(" ")


#ques 2

day=int(input("enter the respective day of month:"))
month=int(input("enter the respective month:"))
year=int(input("enter the respective year:"))

if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025:
    if month in (1,3,5,7,8,10):
        if 1<=day<=30:
            print("the next date:",day+1,"/",month,"/",year)
        else:
            print("the next date: 1/",month+1,"/",year)
    elif month in (4,6,9,11):
        if 1<=day<=29:
            print("the next date:",day+1,"/",month,"/",year)
        elif day==30:
            print("the next date: 1/",month+1,"/",year)       
        else:
            print("invalid input")
    elif month==12:
        if 1<=day<=30:
            print("the next date:",day+1,"/",month,"/",year)
        else:
            print("the next date: 1/1/",year+1)
            
    else:
        if 1<=day<=27:
            print("the next date:",day+1,"/",month,"/",year)
        elif day==28:
            if year%4==0:
                print("the next date:",day+1,"/",month,"/",year)
            else:
                print("the next date: 1/",month+1,"/",year)
        elif day==29:
            if year%4==0:
                print("the next date: 1/",month+1,"/",year)
            else:
                print("invalid input")
        else:
            print("invalid input")
else:
    print("invalid input")
print(" ")


#ques 3

inp_list=[3,9,10,12,25]
l2=[]
for no in inp_list:
    l2.append((no,no**2))
print(l2)
print(" ")


#ques 4

n=int(input("enter grade points\n"))

dict1={10:{"g":"A+","p":"Outstanding"},
       9:{"g":"A","p":"Excellent"},
       8:{"g":"B","p":"Very Good"},
       7:{"g":"+B","p":"Good"},
       6:{"g":"C","p":"Average"},
       5:{"g":"C+","p":"Below Average"},
       4:{"g":"D","p":"Poor"}}

if n not in range(4,11):
     print("error!!, pls enter suitable grade point")
else:
    print("Your Grade is %s and %s Performance."%(dict1[n]["g"],dict1[n]["p"]))
print(" ")


#ques 5

a=("ABCDEFGHIJK")
n=11
k=0
while (n>0 and k<6):
    print(" "*k,a[0:n])
    n=n-2
    k=k+1
print(" ")
   

#ques 6
dict1={}

while(1):
    n=input("enter name of the student")
    s=int(input("enter SID of the student"))
    dict1[s]=n
    x=input("do you want to continue \nEnter  'Y' for yes \n 'N' for no\n")
    if x.upper()=="Y":
        continue
    else:
        break
#part a)
print(dict1)

#part b)
l1=[]
dict2={}
for sid in dict1:
    l1.append(dict1[sid])
    l1.sort()
for item in l1:
     for sid in dict1:
         if dict1[sid]== item:
             dict2.update({sid:item})
print(dict2)

#part c)
l3=[]
dict3={}
for sid in dict1:
    l3.append(sid)
    l3.sort()
for item in l3:
    dict3.update({item:dict1[item]})
print(dict3)             


#part d)
n=int(input("Enter the SID of the student"))
if n in dict1:
    print("the name of the student with SID=%d is:"%(n),dict1[n])
else:
    print("please enter a valid SID to search from the list!!")
print(" ")



#ques7

n=int(input("enter no. of terms in resultant fibonacci series\n"))
i=0
j=1
k=1
sum_f=0
if n<=0:
    print("enter a valid input")
else:
    while k<=n:
        print(i,end=" ")
        sum_f+=i
        s=i+j
        j=i
        i=s
        k+=1
print("\nsum of the series:",sum_f)
print("average of the series",sum_f/n)
print(" ")



#ques 8

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#part a)
set4=set1^set2
print(set4)

#part b)
set5=(set1|set2|set3)- ((set1&set2)|(set1&set3))
print(set5)

#part c)
set6=(set1|set2|set3)-set5
print(set6)

#part d)
set7=set(range(1,10))-set1
print(set7)

#part e)   
set8=set(range(1,10))-(set1|set2|set3)
print(set8)
                
                
            
            
            
    
            
           
            
    
        

        



        

