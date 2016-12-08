
# coding: utf-8

# In[1]:

f=open('data1.csv')
data = f.read()


# In[2]:

data


# In[3]:

for i in data:
    print i
    break


# In[4]:

data.split(',')


# In[6]:

lines = data.split("\n")


# In[8]:

for line in lines:
    print line


# In[9]:

for line in lines:
    print line.split(',')


# In[10]:

for line in lines:
    print line.split(',')[-1]


# In[11]:

for line in lines[1:]:
    print line.split(',')[-1]


# In[12]:

import re
re.findall('[0-9]{10}',data)


# In[13]:

f=open('data1.csv')
data=f.read()


# In[14]:

data


# In[15]:

print data.split('\n')


# In[16]:

import re
re.findall('[0-9]{10}',data)


# In[17]:

# []{}?+*.$^


# In[18]:

s="python program"
re.findall('p',s)


# In[19]:

data


# In[20]:

re.findall('[abc]',data)


# In[21]:

re.findall('[a-z]',data)


# In[22]:

re.findall('[0-9]',data)


# In[23]:

re.findall('[a-z][0-9]',data)


# In[24]:

data


# In[25]:

re.findall('[a-z]{3}[0-9]',data)


# In[27]:

re.findall('[a-z]{1,5}[0-9]',data)


# In[28]:

re.findall('[a-z]+[0-9]',data)


# In[29]:

re.findall('[a-z]*[0-9]',data)


# In[30]:

re.findall('[a-z]{0,1}[0-9]',data)


# In[31]:

re.findall('[a-z]?[0-9]',data)


# In[32]:

re.findall('.',data)


# In[33]:

re.findall('.',data,re.DOTALL)


# In[34]:

data


# In[36]:

re.findall('[0-9]',data)


# In[37]:

data


# In[38]:

re.findall('[^0-9]',data)


# In[39]:

re.findall('^[0-9]',data)


# In[40]:

data


# In[41]:

re.findall('[0-9]$',data)


# In[43]:

data


# In[45]:

data.split('\n')


# In[46]:

data = open('data1.csv').read()


# In[47]:

data


# In[48]:

re.findall('^[0-9]',data)


# In[49]:

re.findall('^[0-9]',data)


# In[50]:

re.findall('^[0-9]',data,re.M)


# In[51]:

data


# In[53]:

re.findall('[a-z]{3}',data)


# In[56]:

data = open('data1.csv').read()
re.findall('[a-z]{3}',data)


# In[57]:

data = open('data1.csv').read()
re.findall('[a-zA-Z]{3}',data)


# In[58]:

data = open('data1.csv').read()
re.findall('[a-z]{3}',data,re.I)


# In[59]:

data


# In[66]:

re.findall('[a-z0-9]+@[a-z.]+',data,re.I)


# In[69]:

data = open('data1.csv').read()
re.findall('[+][0-9]{1,3}[0-9]{10}',data)


# In[70]:

import subprocess as sp


# In[72]:

sp.check_output('ls -l')


# In[75]:

sp.check_output(['ls','-l'])


# In[76]:

ps = sp.check_output(['ps','-aux'])


# In[77]:

ps


# In[78]:

"firefox" in ps


# In[79]:

ps.splitlines()


# In[80]:

ps.split('\t')


# In[81]:

ps.split(' ')


# In[82]:

ps


# In[83]:

ps.split('\n')


# In[84]:

lines = ps.split('\n')


# In[85]:

len(lines)


# In[86]:

lines[0]


# In[87]:

lines[1]


# In[88]:

for ps in lines:
    if "firefox" in ps:
        print ps


# In[89]:

for ps in lines:
    if "firefox" in ps:
        print ps.split()


# In[90]:

pid = None
for ps in lines:
    if "firefox" in ps:
        pid = ps.split()[1]
print pid


# In[91]:

import paramiko as pmk
ssh = pmk.SSHClient()
ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
ssh.connect("localhost",username="tcloudost",password="pythonrocks")
ssh.exec_command('mkdir ~/paramiko123')


# In[92]:

import os


# In[93]:

import sys


# In[ ]:

sys.

