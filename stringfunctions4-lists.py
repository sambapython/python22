
# coding: utf-8

# In[2]:

s="   @#$user  @#$name$#@   "
print s
print s.strip()


# In[3]:

s="@#$user  @#$name$#@"
print s
print s.strip('@')


# In[4]:

s="@#$user  @#$name$#@"
print s
print s.strip('Z')


# In[5]:

s="@#$user  @#$name$#@"
print s
print s.strip('@#')


# In[6]:

s="@#$user  @#$name$#@"
print s
print s.strip('#')


# In[7]:

s="@#$user  @#$name$#@"
print s
print s.strip('#@')


# In[8]:

s="@#$user  @#$name$#@"
print s
print s.strip('#@$')


# In[9]:

s


# In[10]:

s.replace('@','@@')


# In[12]:

s.replace('@','@@',2)


# In[13]:

s


# In[14]:

s.replace('@','')


# In[15]:

"""
only digits
1   -> 000001
10  -> 000010
100 -> 000100
"""
"""
String reverse
"""


# In[17]:

s="123"
s.zfill(25)


# In[18]:

l=[1,1.2,"python",1+2j,[1,2,3,4,[10,20,30],[100,2003,00]],10000,20000]


# In[19]:

l=[10,20,30,40,50]


# In[20]:

l[0]


# In[21]:

l[-1]


# In[22]:

l[1:5]


# In[23]:

l


# In[24]:

l[0]=100


# In[25]:

l


# In[26]:

s="python"
s[0]="S"
print s


# In[27]:

s[0]


# In[28]:

s


# In[29]:

s.replace('p','s')


# In[30]:

s


# In[31]:

s.upper()


# In[32]:

s


# In[33]:

s.encode("base64")


# In[34]:

s


# In[35]:

s1 = s.encode("base64")


# In[36]:

s1


# In[37]:

s


# In[38]:

l


# In[39]:

l.append(5000)


# In[40]:

l


# In[41]:

l=[10,20,30,40,50]


# In[42]:

l=[10,20,30,40,50]
s="python"
l1=l.append(500)
s1 = s.replace('p','z')
print s
print l


# In[43]:

print l1
print s1


# In[44]:

def fun(a):
    a=a+10
s1 = fun(1000)
print s1


# In[45]:

def fun(a):
    a=a+10
    return a
s1 = fun(1000)
print s1


# In[46]:

l=[1,2,3,4]
l1=l
l2 = l.append(100)


# In[47]:

l


# In[48]:

print l2


# In[49]:

s


# In[50]:

s+ "c"+"cpp"


# In[51]:

s="python"
d=123
f=1.23


# In[52]:

"%s %d %f"%(s,d,f)


# In[53]:

"{0} {1} {2}".format(s,d,f)


# In[54]:

l=[1,2,3,4]
l1=[5,6,7,8]


# In[55]:

l+l1


# In[56]:

l-l1


# In[57]:

l+12


# In[58]:

l


# In[59]:

l+[12]


# In[60]:

l*2


# In[62]:

l*5


# In[64]:

l=[10,20,30,40]
l2=l+[100,200]
l1=l
l3=l+[1000]
print "l=",l
print"l1=", l1
print "l2=",l2
print "l3=",l3


# In[65]:

l=[1,2,3,4]
l1=l.append(5)
print l
print l1


# In[66]:

l=[1,2,3,4]
l1=l+[5]
print l
print l1


# In[ ]:



