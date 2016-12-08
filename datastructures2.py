
# coding: utf-8

# In[1]:

def fun(a,b):
    return a+b
print fun(10,20)


# In[2]:

print fun(100,200,300)


# In[5]:

# *args
def fun(*a):
    print a
    if len(a)>0:
        print a[0]
fun()
fun(10)
fun(10,20)
fun(10,20,3)


# In[6]:

def fun(a=0,b=0):
    print "a={0},b={1}".format(a,b)
    return a+b
print fun(100,200)
print fun(100)
print fun()


# In[7]:

print fun(b=2000)


# In[8]:

def fun(a=10,b):
    print a,b


# In[9]:

def fun(b,a=0):
    print a,b


# In[10]:

def fun(a,b):
    print a,b
fun(10,20)
fun(a=100,b=200)


# In[11]:

def fun(a,b):
    print a,b
fun(10,20)
fun(a=100,b=200)
fun(a=10,b=20,c=30,d=40)


# In[12]:

def fun(a,b,*c1):
    print a,b,c1
fun(10,20)
fun(a=100,b=200)
fun(a=10,b=20,c=30,d=40)


# In[13]:

def fun(a,b,*c1):
    print a,b,c1
fun(10,20)
fun(a=100,b=200)
fun(a=10,b=20,30,40)


# In[14]:

#*kwargs
def fun(a,b,**c1):
    print a,b,c1
fun(10,20)
fun(a=100,b=200)
fun(a=10,b=20,c=30,d=40)


# In[15]:

import pandas as pd


# In[17]:

def add_ten(a):
    return a+10
for  i in [10,20,30,45,67,89,57]:
    print add_ten(i)


# In[18]:

def add_ten(a):
    return a+10
l=[]
for  i in [10,20,30,45,67,89,57]:
    l.append(add_ten(i))
print l


# In[19]:

l1=map(add_ten,[10,23,45,67,89,12,34,56])


# In[20]:

l1


# In[21]:

def add_ten(a):
    print a
    a=a+100
    c=1002+a
    return a+10
# lambda : single staement anonymous function...
f= lambda a:a+10
f(1000)


# In[22]:

f= lambda a:print a;a+10


# In[25]:

f= lambda a:a+10
for i in range(10,20,3):
    print "i=",i
    print "f(i)=",f(i)


# In[26]:

f= lambda a:a+10
l=[]
for i in range(10,20,3):
    l.append(f(i))
print l


# In[27]:

map(lambda a:a+10,range(10,20,3))


# In[28]:

map(lambda a:a+10 if a%2==0,range(10,20,3))


# In[29]:

f= lambda a:a+10
map(f,range(10,20,3))


# In[30]:

l=['1','2','3','4']
l1=[1,2,3,4]
print sum(l1)


# In[31]:

sum(l)


# In[32]:

sum(map(int,l))


# In[33]:

l2=[]
for i in l:
    l2.append(int(i))
print sum(l2)


# In[34]:

f= lambda a:int(a)
l2 = map(f,l)
print sum(l2)


# In[35]:

# list comprehension
l1 = [i+10 for i in [5,6,1,2,3,4,8,9]]


# In[36]:

l1


# In[39]:

l2=[int(i) for i in ['1','2','3','4']]
print l2
print sum(l2)


# In[40]:

9676622023
sambapython@gmail.com


# In[ ]:



