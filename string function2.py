
# coding: utf-8

# In[1]:

s="python program"


# In[2]:

s.find('hon')


# In[3]:

s.rfind("hon")


# In[4]:

s.find('p')


# In[5]:

s.rfind('p')


# In[6]:

s="python prohongram"
print s.find('hon')
print s.rfind('hon')


# In[7]:

"abcd".isalpha()


# In[8]:

"abCD".isalpha()


# In[9]:

"abcd@#$".isalpha()


# In[10]:

"abcd123".isalpha()


# In[11]:

"".isalpha()


# In[12]:

"".isupper()


# In[13]:

"abc123".isalnum()


# In[14]:

"abc".isalnum()


# In[15]:

"123".isalnum()


# In[16]:

"abcd123@".isalnum()


# In[17]:

s=raw_input("Enter a string:")
if s.isalnum():
    print "given string doesnot contains special chars"
else:
    print "it contains special chars"


# In[18]:

s=raw_input("Enter a string:")
if s.isalnum():
    print "given string doesnot contains special chars"
else:
    print "it contains special chars"


# In[19]:

s=raw_input("Enter a string:")
if s.isalnum():
    print "given string doesnot contains special chars"
else:
    print "it contains special chars"


# In[20]:

s=raw_input("Enter a string:")
if s.isalnum():
    print "given string doesnot contains special chars"
else:
    print "it contains special chars"


# In[21]:

s=raw_input("Enter a string:")
if s.isalnum():
    print "given string doesnot contains special chars"
else:
    print "it contains special chars"


# In[22]:

s=raw_input("Enter string:")
if s == "":
    print "not entered"
else:
    print "Entered: ",s


# In[23]:

s=raw_input("Enter string:")
if s == "":
    print "not entered"
else:
    print "Entered: ",s


# In[24]:

s=raw_input("Enter string:")
if len(s)>0:
    print "Entered: ",s
else:
    print "not entered"
    


# In[25]:

s=raw_input("Enter string:")
if len(s)>0:
    print "Entered: ",s
else:
    print "not entered"
    


# In[35]:

if 0:
    print "0 is true"
else:
    print "0 is false"


# In[26]:

bool(0)


# In[27]:

bool(1)


# In[28]:

bool(-10)


# In[29]:

bool("0")


# In[30]:

bool("ptyo")


# In[31]:

bool("")


# In[32]:

bool([])


# In[33]:

bool(())


# In[34]:

bool({})


# In[36]:

s=raw_input("Enter a string:")
if s:
    print "s is true"
else:
    print "s is false"


# In[37]:

s=raw_input("Enter a string:")
if s:
    print "s is true"
else:
    print "s is false"


# In[38]:

s=raw_input("Enter a string:")
if s:
    print "s is true"
else:
    print "s is false"


# In[39]:

s=raw_input("Enter a string:")
if s:
    print "s is true"
else:
    print "s is false"


# In[40]:

if 10<20:
    print "10<20 is true"


# In[41]:

bool(10<20)


# In[42]:

bool(10>20)


# In[43]:

s="abcd"
s1="abcdasdfg"
print s.count('a')
print s1.count('a')


# In[44]:

s.count("python")


# In[45]:

for char in "python program":
    print char


# In[46]:

s="python is pure object oriented programing language"
for char in s:
    print char,"=",s.count(char)


# In[47]:

s="python is pure object oriented programing language"
for char in s:
    if s.count(char) == 1:
        print char,"is not rpeated"
    else:
        print char,"is repeated"
    


# In[48]:

s="python is pure object oriented programing language"
for char in s:
    if s.count(char) == 1:
        print char,"is not rpeated"
    else:
        print char,"is repeated",s.count(char)
    


# In[49]:

#[SPACE]
s="python is pure object oriented programing language"
for char in s:
    res = s.count(char)
    if res == 1:
        print char,"is not rpeated"
    else:
        print char,"is repeated",res
    


# In[50]:

#[SPACE]
s="python is pure object oriented programing language"
for char in s:
    res = s.count(char)
    if res == 1:
        if char == " ":
            print "[SPACE]"
        print char,"is not rpeated"
    else:
        print char,"is repeated",res
    


# In[51]:

#[SPACE]
s="python is pure object oriented programing language"
for char in s:
    res = s.count(char)
    if res == 1:
        if char == " ":
            print "[SPACE]"
        print char,"is not rpeated"
    else:
        if char == " ":
            print "[SPACE]"
        print char,"is repeated",res
    


# In[52]:

#[SPACE]
s="python is pure object oriented programing language"
for char in s:
    res = s.count(char)
    if char == " ":
            print "[SPACE]"
    if res == 1:
        print char,"is not rpeated"
    else:
        print char,"is repeated",res
    


# In[53]:

print "hello world"
print "hello world"


# In[55]:

#[SPACE]
s="python is pure object oriented programing language"
output=""
for char in s:
    res = s.count(char)
    if char == " ":
           output = output+"[space] "
    if res == 1:
        output=output+char+" is not rpeated"
    else:
        output = output+char+" is repeated"+str(res)
    


# In[56]:

#[SPACE]
s="python is pure object oriented programing language"
output=""
for char in s:
    res = s.count(char)
    if char == " ":
           output = output+"[space] "
    if res == 1:
        output=output+char+" is not rpeated"
    else:
        output = output+char+" is repeated"+str(res)
    print output


# In[58]:

#[SPACE]
s="python is pure object oriented programing language"

for char in s:
    output=""
    res = s.count(char)
    if char == " ":
           output = output+"[space]"
    if res == 1:
        output=output+char+" is not rpeated"
    else:
        output = output+char+" is repeated"+str(res)
    print output


# In[59]:

#[SPACE]
s="python is pure object oriented programing language"

for char in s:
    output=""
    res = s.count(char)
    if char == " ":
           output = output+"[space]"
    if res == 1:
        output=output+char+" is not rpeated"
    else:
        output = output+char+" is repeated"+str(res)
print output


# In[ ]:



