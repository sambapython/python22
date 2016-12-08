
# coding: utf-8

# In[3]:

#[SPACE]
s="python is pure object oriented programing language"
visited = ""
for char in s:
    output=""
    if char in visited:
        continue
    visited = visited+char
    print visited
    res = s.count(char)
    if char == " ":
           output = output+"[space]"
    if res == 1:
        output=output+char+" is not rpeated"
    else:
        output = output+char+" is repeated"+str(res)
    print output


# In[4]:

len("pythhn program")


# In[6]:

len('python \tprogram')


# In[7]:

len('python \tprogram\n\n')


# In[8]:

len(r'python \tprogram\n\n')


# In[9]:

len("123")


# In[10]:

len(123)


# In[11]:

len(True)


# In[12]:

len(None)


# In[13]:

print 1234
print 123
print 12
print 1


# In[ ]:

s="python program"
box_size = 25


# In[14]:

"abcd efgh".isspace()


# In[15]:

"       ".isspace()


# In[16]:

"".isspace()


# In[17]:

s="python program"
box_size = 25
print s
print s.center(box_size)
print s.ljust(box_size)
print s.rjust(box_size)


# In[18]:

s="python program"
box_size = 25
print s
print s.center(box_size,'$')
print s.ljust(box_size,'@')
print s.rjust(box_size,'*')


# In[19]:

s="python program"
box_size = 10
print s
print s.center(box_size)
print s.ljust(box_size)
print s.rjust(box_size)


# In[21]:

#https://docs.python.org/3/library/codecs.html#standard-encodings
pas = "python program"
enc = pas.encode('base64')


# In[22]:

print pas
print enc


# In[23]:

s1 = "python program"
if s1 == enc:
    print "password match"
else:
    print "password not match"


# In[25]:

s1 = "python program"
dec = enc.decode('base64')
if dec == s1:
    print "password match"
else:
    print "password not match"


# In[26]:

dec


# In[27]:

print enc
print s1
print dec


# In[28]:

enc1 = enc.encode("base64")


# In[29]:

enc1


# In[30]:

s


# In[31]:

s.endswith('gram')


# In[32]:

s.endswith('python')


# In[33]:

s.startswith("python")


# In[34]:

s.startswith('program')


# In[35]:

s.endswith("")


# In[36]:

s.startswith("")


# In[38]:

s="tab1\ttab2\ttab3\ttab4"
print s.expandtabs(16)


# In[40]:

name="Anil"
age=23
sal=23456
height=5.6
# name: Anil, age: 23, sal: 23456 height: 5.6
s1 = "name: "+name+", age: "+str(age)+", sal: "+str(sal)+", height: "+str(height)
print s1


# In[41]:

name="Anil"
age=23
sal=23456
height=5.6
# name: Anil, age: 23, sal: 23456 height: 5.6
s1 = "name: "+name+", age: "+str(age)+", sal: "+str(sal)+", height: "+str(height)
s2 = "name: %s, age: %d, sal: %d, height: %f"%(name,age,sal,height)
print s1
print s2


# In[42]:

name="Anil"
age=23
sal=23456
height=5.6
# name: Anil, age: 23, sal: 23456 height: 5.6
s1 = "name: "+name+", age: "+str(age)+", sal: "+str(sal)+", height: "+str(height)
s2 = "name: %s, age: %d, sal: %d, height: %d"%(name,age,sal,height)
print s1
print s2


# In[43]:

name="Anil"
age=23
sal=23456
height=5.6
# name: Anil, age: 23, sal: 23456 height: 5.6
s1 = "name: "+name+", age: "+str(age)+", sal: "+str(sal)+", height: "+str(height)
s2 = "name: %r, age: %r, sal: %r, height: %r"%(name,age,sal,height)
print s1
print s2


# In[44]:

name="Anil"
age=23
sal=23456
height=5.6
# name: Anil, age: 23, sal: 23456 height: 5.6
s1 = "name: "+name+", age: "+str(age)+", sal: "+str(sal)+", height: "+str(height)
s2 = "name: %s, age: %d, sal: %d, height: %f"%(name,age,sal,height)
s3 = "name: %s, age: %d, sal: %d, height: %d"%(name,age,sal,height)
s4 = "name: %r, age: %r, sal: %r, height: %r"%(name,age,sal,height)
s5 = "name: {0}, age: {1}, sal: {2}, height: {3}".format(name,age,sal,height)
print s1
print s2
print s3
print s4
print s5


# In[45]:

f=23.45678
print "price: {0}".format(f)


# In[46]:

f=23.45678
print "price: {0:.2f}".format(f)


# In[47]:

print 1234
print 123
print 12
print 1


# In[48]:

print "{0:4d}".format(1234)
print "{0:4d}".format(123)
print "{0:4d}".format(12)
print "{0:4d}".format(1)


# In[49]:

s


# In[50]:

s="python program"


# In[51]:

s.find('p')


# In[52]:

s.index('p')


# In[53]:

s.find('z')


# In[54]:

s.index('z')


# In[55]:

"123".isdigit()


# In[56]:

"1234qwe".isdigit()


# In[57]:

"1234 ".isdigit()


# In[58]:

"12.34".isdigit()


# In[59]:

"-10".isdigit()


# In[60]:

"".isdigit()


# In[61]:

s="python PROGRam"


# In[62]:

print s.capitalize()


# In[63]:

print s.title()


# In[64]:

"Python Program".istitle()


# In[65]:

"Python ProGram".istitle()


# In[66]:

"".istitle()


# In[67]:

"123".istitle()


# In[ ]:



