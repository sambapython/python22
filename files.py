
# coding: utf-8

# In[1]:

f=open('data.csv','r')
data = f.read()


# In[2]:

print data


# In[3]:

print type(data)


# In[4]:

data


# In[6]:

for k in data:
    print k
    break


# In[7]:

lines  =data.split('\n')


# In[8]:

lines


# In[10]:

for line in lines:
    print line
    break


# In[11]:

f=open('data.csv','r')
data = f.readlines()


# In[12]:

type(data)


# In[13]:

data[0]


# In[14]:

data[1]


# In[15]:

for i in data:
    print i
    break


# In[17]:

for i in data:
    print i[2:7]


# In[19]:

for i in data:
    print i.split(',')


# In[21]:

names=[]
for i in data:
    names.append(i.split(',')[1])


# In[22]:

names


# In[23]:

[i.split(',')[1] for i in data]


# In[24]:

map(lambda i:i.split(',')[1],data)


# In[26]:

f=open('data.csv')
data = f.re()
print data
print "reading second time$$$$$$$$$$$$$$"
data1=f.read()
print data1


# In[28]:

f=open('data.csv')
print f.tell()
data = f.read()
print data
print f.tell()
data1 = f.read()
print f.tell()


# In[30]:

f=open('data.csv')
print f.tell()
data = f.read()
print data
print f.tell()
f.seek(0)
print f.tell()
data1 = f.read()
print data1
print f.tell()


# In[33]:

f=open('data.csv')
l1 = f.readline()
print l1
print f.tell()
l2= f.readline()
print l2
print f.tell()
print f.readlines()


# In[35]:

f=open('f1.txt','w')
f.write('Some data')


# In[36]:

f=open('f1.txt','w')
f.write('Some data')
f.close()


# In[37]:

f=open('f1.txt','w')


# In[38]:

f=open('f1.txt','w')
f.write("somedata")
f.close()
f.write("some more data")


# In[39]:

f=open('f1.txt','w')
f.write("somedata")
f.flush()
f.write("some more data")
f.flush()


# In[40]:

data  = ['data1','data2','data3']
f=open('f1.txt','w')
for i in data:
    f.write(i)
f.close()


# In[41]:

data  = ['data1','data2','data3']
f=open('f1.txt','w')
f.writelines(data)
f.close()


# In[42]:

data  = ['data1','data2','data3']
f=open('f1.txt','a')
f.writelines(data)
f.close()


# In[43]:

f=open('f1.txt','w')
f.write(1234)
f.close()


# In[44]:

f=open('f1.txt','w')
f.write(str(1234))
f.close()


# In[45]:

d={'name':'na1','id':23}
f=open('f1.txt','w')
f.write(d)
f.close()


# In[46]:

d={'name':'na1','id':23}
f=open('f1.txt','w')
f.write(str(d))
f.close()


# In[47]:

d=['name1','name2','name3','name4']
f=open('f1.txt','w')
f.write(str(d))
f.close()


# In[48]:

f = open('f1.txt')
data = f.read()
print type(data)


# In[49]:

data


# In[50]:

import json
data_list = json.loads(data)


# In[51]:

import pickle


# In[52]:

l=['name1','name2','name3']
d={'id':1,'names':'name1'}
f=open('f1.txt','w')
pickle.dump(l,f)
pickle.dump(d,f)
f.close()


# In[53]:

f=open('f1.txt')
l1=pickle.load(f)
d1=pickle.load(f)
f.close()
print l1,type(l1)
print d1,type(d1)


# In[ ]:



