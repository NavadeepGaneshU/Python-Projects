for i in range (0,100,1):
    print(i)
    
    
i=100
while i>0:
    print(i)
    i=i-1    
    
     
a=20
b=30
z=a+b
print(a,b,z)


x=20
y=10
z=x/y
print(x,y,z)


x=20
y=10
z=x//y
print(x,y,z)


x=20
y=10
z=x%y
print(x,y,z)


a=2+3*5/6**8//6+2*6
print(a)


a=5/6**8
print(a)
b=a//6
print(b)


a=4+5*6**4+4+8//2
print(a)


x=10
y=20
if x>y:
    print('x is greater than y')
elif x==y:
        print('x is equal to y')
else:
        print('y is greater than x')
        

        
for i in range(314,31428,2):
    print(i)
    
     
i=25
while i<100:
    print(i)
    i=i+5



i=int(input('Enter a number'))
if i%2==0:
    print('This number is Even')
else:
    print('This number is Odd')
    
    

x=int(input('entera number'))
y=int(input('enter a number'))
z=x+y
print(z)



i=5
while i>0:
    print(i)
    i=i-1
    if i%2==0:
        print('even=',i)
    else:
        print('odd=',i)
            
            
            
for i in range(1,100,2):
    print(i)
    
    
    
i=0
while i<100:
    print(i)
i=i-3



for i in range(100,1,-3):
    print(i)
    
    
sum=0   
x=int(input('enter first number'))
y=int(input('enter second number'))
for i in range(x,a):
    sum=sum+i
print(sum)



sum=0
x=int(input('enter range'))
    
for i in range(x):
    y=int(input('enter number')) 
    sum=sum+y
    print(sum)
    
    
s=0
x=int(input('enter number')) 
while x>0:
    a=x%10
    x=x//10
    s=s+a
    print(s)
    
    
    
x=int(input('enter x'))
y=int(input('enter y'))
for i in range(2,x):
        if(x%i==0):
            break
else:
        print('number is prime')

 
x=int(input('enter first number'))
y=int(input('enter last number'))
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print(x,y)


sum=0   
x=int(input('enter first number of series'))
y=int(input('enter last number of series'))
for i in range(x,y):
    print(i)
    

count1=0
count2=0
count3=0
count4=0
for num in range(2,100):
     for i in range(2,num):
          if (num%i==0):
               break
     else:
          if (num>2 and num<25):
               count1=count1+1
          elif(num>25 and num<50):
               count2=count2+1
          elif(num>50 and num<75):
               count3=count3+1
          elif(num>75 and num<100):
               count4=count4+1
               
               print("The number of primes between 2 and 25 is",count1)
               print("The number of primes between 25 and 50 is",count2)
               print("The number of primes between 50 and 75 is",count3)
               print("The number of primes between 75 and 100 is",count4)
               


x=int(input('how many terms'))
n1=0
n2=1
if x==1:
    print(n1)
else:
    print(n1,n2,end)
    
    
    
f=1
x=int(input('Enter a number to find factorial of'))
for i in range(1,x+1):
    f=i*f
print(f)


while(True):
    x=int(input('Enter [1] for Triangle , Enter [2] for Rectangle, Enter [3] for square, Enter [4] for Circle, Enter 5 to Exit'))
    if x==1:
        b=float(input('Enter the base'))
        h=float(input('Enter the height'))
        a1=0.5*b*h
        print('Area of Triangle is',a1)
    elif x==2:
        l=float(input('Enter the length'))
        br=float(input('Enter the breadth'))
        a2=l*br
        print('Area of Recrangle is', a2)
        
    elif x==3:
        s=float(input('Enter the side'))
        a3=s*s
        print('Area of Square is', a3)
    elif x==4:
        r=float(input('Enter the radius'))
        a4=3.1428*r*r
        print('Area of Circle is', a4)
    elif x==5:
        break



while(True):
    x=int(input('Enter [1] for Triangle , Enter [2] for Rectangle, Enter [3] for square, Enter [4] for Circle, Enter [5] to Exit'))
    if x==1:
        b,h=input('Enter the Base and the Height').split()
        print("Area of Triangle is", 0.5*float(b)*float(h))
    elif x==2:
        l,br=input('Enter the Length and Breadth').split()
        print('Area of Recrangle is', float(l)*float(br))
    elif x==3:
        s=float(input('Enter the Side'))
        print('Area of Square is', s*s)
    elif x==4:
        r=float(input('Enter the Radius'))
        print('Area of Circle is', 3.1428*r*r)
    elif x==5:
        break
         

x=int(input('Enter first number'))
y=int(input('Enter second number'))
temp=x
x=y
y=temp
print(x,y)



x=int(input('Enter first number'))
y=int(input('Enter second number'))
x=x+y
y=x-y
x=x-y
print(x,y)



x=int(input('Enter first number'))
y=int(input('Enter second number'))
x,y=y,x
print(x,y)
    
        

x=int(input('enter the year'))
if(x%4==0):
elif(x%100==0):
elif(x%400=0):
    print('It is leap ')
      
        
x=int(input('How many terms do you want in Series'))
a=1
b=1
print(a)
print(b)
for i in range(2,x):
    c=a+b
    a=b
    b=c
    print(c)
    
    
    
c=0   
a=1
b=1
i=2
x=int(input('Enter the last term'))
print(a)
print(b)
while(i<=x):
    c=a+b
    a=b
    b=c
    if c<=x:
        print(c)
    else:
        break


a=float(input('Enter first number :'))
b=float(input('Enter second number :'))
c=float(input('Enter third number :'))
if(a>b)and(a>c):
    print('a is greater than b and c',   a,    b,   c)
elif(b>a)and(b>c):
    print('b is greater than a and c',   b,   a,   c )
elif(c>a) and (c>b):
    print('c is greater than a and b',   c,   b,   a)
elif(a==b)and(a==c)and(b==c)and(b==a)and(c==a)and(c==b):
    print('all are equal', a,   b,  c)


num=int(input('Enter the number to which you want to get Tables of :')) 
for i in range (1,11):
    print(num,'x', i, '=',num*i) 
    


L=[0.96,1,2,3,'hello world!']
print(L[0])

    

L1= ['physics','chemistry','2001']
L2=[1,2,3,4,5,6,7]
print(L1[0][2],L1[1][2],L1[1][5])



l=[]
n=int(input("Enter the number of digits to be entered"))
for i in range(1,n+1):
    l.append(int(input("Enter the number")))
print(l)


L1=[1,3,2.05,'Hello',9.5]
L2=[2,4,6.25,'World',10.5]
L3=L1+L2
print(L3)


for x in ['hello world!!!!!!!']:
    print (x)
    
    
L=[4,6,9]
len=len(L)
print(len)



L=['spam', 'Spam','SPAM!']
print(L[0][0],L[1][1],L[2][4])
print(L[1:],L[-8:],L[-3:-7],L[1::],L[-3::-7])


L1,L2=[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0]
min=min(L1)
max=max(L2)
print(min)
print(max)



L2=[1,2,3,4,5,6,7,8,9,0]
print(L2.pop())
print(L2)


L1=[1,2,3,4,5,6,7,8,9,0]
L2=[2,4,6,8,10,12,14,16,18,20]
(L1.append(L2))
print(L1)



L1=[1,2,3,4,5,6,7,8,9,0]
L2=[2,4,6,8,10,12,14,16,18,20]
(L1.extend(L2))
print(L1)
print(L1.index(0))
print(L1.remove(1))
print(L1)
print(L1.reverse())
print(L1)
print(L1.sort([]))
print(L1)



L=['red','green','blue','yellow','white','black']
print(L)
L[0]='cyan'
print(L)
del L[3]
print(L)
L.insert(1,'is my favouraite colour')
print(L)
print(L[2:4])


N=[10,20,30,40,50,60,70,80,90,100]
print(N[::3])
print(N[::-3])
print(N[1:2])
print(N[-1:-3])
print(N[-1::2])
print(N[-2::3])


#program to find LCM
def lcm (x,y):
    a=x
    b=y
    while(x !=y):
        if(x>y):
            y=y+b
        else:
            x=x+a
    print(x,y)
lcm(4,2)


#program to find factorial
def fact(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return(x)
a=fact(4)
print('The factorial is=',a)


#program using lambda function
x=lambda a:a+25
print(x(10))
