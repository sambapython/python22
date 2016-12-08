
# coding: utf-8

# In[1]:

s="python program"
print s[:7]+s[-1:-8:-1]


# In[2]:

# functions


# In[3]:

def fun():
    print "this is function"


# In[4]:

fun()


# In[5]:

def fun(a,b):
    print a,b


# In[6]:

fun(10,20)


# In[7]:

fun(100,200)


# In[8]:

fun(100,200)


# In[10]:

def fun(a,b):
    print a,b
    c=a+b
    return c
d=fun(100,200)


# In[11]:

# scope of a variable
a=100
def fun():
    print a
fun()


# In[12]:

def fun():
    a1 = 1000
fun()
print a1


# In[13]:

a=1000
def fun():
    a2=3000
    print a2
    print a
def fun1():
    print a
    print a2
fun()
fun1()
print a2


# In[18]:

#print dir()
#print "$$$$$$$$$$$$$$$$$$$$$$$$"
a1234=1000
#print dir()
#print "$$$$$$$$$$$$$$$$$$$$$$$$"
def fun():
    print dir()
    print "$$$$$$$$$$$$$$$$$$$$$$$$"
    a2=3000
    print a2
    print a1234
    print dir()
    print "$$$$$$$$$$$$$$$$$$$$$$$$"
def fun1():
    print dir()
    print "$$$$$$$$$$$$$$$$$$$$$$$$"
    print a1234
    print a2
#print dir()
#print "$$$$$$$$$$$$$$$$$$$$$$$$"
fun()
fun1()
#print a2


# In[19]:

def fun():
    a5=5000

print a5


# In[20]:

def fun():
    a5=5000
fun()
print a5


# In[21]:

a=1000
def fun():
    a=20000
fun()
print a


# In[22]:

a=1000
def fun():
    a=20000
    print "a=",a
    
fun()
print a


# In[23]:

a=1000
def fun():
    a=20000
    print "a=",a
    a=a+2
    
fun()
print a


# In[25]:

a=1000
def fun():
    print "a=",a
    #a=20000
fun()
print a


# In[26]:

a=1000
def fun():
    print "a=",a
    a=20000
fun()
print a


# In[27]:

a=1000
def fun():
    b=a+200
    print b
fun()
print a


# In[28]:

def fun(a,b):
    print a,b
    c=a+b
    print c
fun(100,200)
print c


# In[31]:

def fun(a,b):
    print a,b
    c=a+b
    print c
    return c
d=fun(100,200)
print "d=",d


# In[32]:

# write a function to cjeck given nuber is odd/even/prime/perfect
# write a funtion to findout area and perimeter of circle
# write function to conert fun(degree, value, conversion degree)


# In[33]:

def fun(a,b):
    return a+b
d=fun(100,200)


# In[34]:

e=fun(100,200,300)


# In[35]:

def fun(a,b,c):
    return a+b+c
d=fun(100,200,300)


# In[36]:

e=fun(100,200)


# In[37]:

# default parameter concept
def fun(a,b,c=0):
    print "a=",a,"b=",b,'c=',c
    return a+b+c
d=fun(100,200,300)
e=fun(1000,2000)


# In[38]:

# default parameter concept
def fun(a,b,c=0,d=0,e=0,f=0):
    print "a=",a,"b=",b,'c=',c
    return a+b+c
d=fun(100,200,300)
e=fun(1000,2000)


# In[39]:

#*args
def fun(*args):
    print args
fun()
fun(10)
fun(10,20)
fun(10,20,30)


# In[ ]:

def fun(a,b,c=0,d=0):
    print "a=",a,"b=",b,'c=',c,'d=',d
fun(100,200)
fun(1000,2000,3000,4000)
fun(10,20,,40)

