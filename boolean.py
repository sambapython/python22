
# coding: utf-8

# In[1]:

10>20


# In[2]:

"program" in "python program"


# In[3]:

s="python program"
sub = raw_input("Enter sub string:")
res = sub in s
print res
print "Given substring find in the actual string"
print "Given substring not find in the actual string"


# In[4]:

s="python program"
sub = raw_input("Enter sub string:")
res = sub in s
print res
print "Given substring find in the actual string"
print "Given substring not find in the actual string"


# In[6]:

s="python program"
sub = raw_input("Enter sub string:")
res = sub in s
print res
if res == True:
 print "Given substring find in the actual string"  
if res == False:
 print "Given substring not find in the actual string"



# In[7]:

#== > >= < <= is in 
a=10
b=10.0
print a==b
print a is b


# In[8]:

print 10>=10


# In[9]:

print 10>10


# In[10]:

print 12>=10


# In[11]:

print '10'>'20'


# In[12]:

#'python','java','c','cpp','zyt'
'c','cpp'.'java','python','zyt'


# In[13]:

print '100'<'20'


# In[14]:

print 100<20


# In[15]:

print '100'<20


# In[16]:

print '1'<20


# In[17]:

print '1'>20


# In[18]:

print "200">2


# In[19]:

print "12000">1


# In[20]:

print "python"<2


# In[21]:

print "str1">23


# In[22]:

print "123"+123


# In[23]:

a=123
print "123"+a


# In[24]:

a=123
a=str(a)
print "123"+a


# In[25]:

bool(10>20)


# In[26]:

a=20
b=100
print bool(a>b)


# In[27]:

bool(a<b)


# In[28]:

bool(0)


# In[29]:

bool(1)


# In[30]:

bool(-10)


# In[31]:

def fun(a):
    print "function started"
    if a==0:
        return False
    if a>0 or a<0:
        return True
    print "function ended"


# In[32]:

True or False


# In[33]:

False or True


# In[34]:

False and True


# In[35]:

True and False


# In[36]:

True and True


# In[38]:

def fun(a):
    print "function started"
    if a==0:
        res =False
    if a>0 or a<0:
        res = True
    print "function ended"
    return res
print fun(-10)


# In[39]:

def fun():
    print "hello function"
    


# In[40]:

fun()


# In[41]:

def fun(inp):
    return "output"
res = fun('input')


# In[42]:

res


# In[43]:

def sum1(a,b):
    return a+b
print sum1(10,20)
print sum1(100,200)
print sum1(300,400)


# In[44]:

def fun():
    print "hello function"


# In[45]:

fun()


# In[46]:

def fun():
    return "hello function"
def fun1():
    print "function started"
    print "hello function1234"
    print "function ended"
  
res = fun()
res1 = fun1()


# In[47]:

def fun():
    return "hello function"
def fun1():
    print "function started"
    print "hello function1234"
    print "function ended"
print "calling functions"


# In[48]:

def fun():
    return "hello function"

def fun1():
    print "function started"
    print "hello function1234"
    print "function ended"
  print "decide whether this statement is executes or not"
print "calling functions"


# In[49]:

def fun():
    return "hello function"

def fun1():
    print "function started"
    print "hello function1234"
    print "function ended"
print "decide whether this statement is executes or not"
return "output"
res = fun1()
print "calling functions"


# In[ ]:



