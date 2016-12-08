
# coding: utf-8

# In[11]:

import psycopg2 as db


# In[12]:

con = db.connect(database = 'db2',user="tcloudost",password="root",host="localhost",port=5432)


# In[13]:

cur = con.cursor()


# In[6]:

cur.execute("create table persons(id int, name varchar(50))")


# In[7]:

con.commit()


# In[14]:

q="insert into persons values(1,'name1')"
cur.execute(q)
con.commit()


# In[15]:

p_id = raw_input("Enter id:")
p_name = raw_input("enter name:")
q="insert into persons values({0},'{1}')".format(p_id,p_name)
cur.execute(q)
con.commit()


# In[17]:

l=[{'id':3,'name':'name3'},{'id':4,'name':'name4'}]
for record in l:
    print record['id'],record['name']


# In[18]:

l=[{'id':3,'name':'name3'},{'id':4,'name':'name4'}]
for record in l:
    print record.get('id'),record.get('name')


# In[19]:

l=[{'id':3,'name':'name3'},{'id':4,'name':'name4'}]
for record in l:
    q="insert into persons values({0},'{1}')".format(record.get('id'),record.get('name'))
    cur.execute(q)
con.commit()


# In[20]:

q="select * from persons"
cur.execute(q)


# In[21]:

cur.fetchall()


# In[23]:

cur.fetchall()


# In[24]:

q="select * from persons"
cur.execute(q)
cur.execute("update persons set name='updataed name' where id=1")
con.commit()


# In[25]:

cur.fetchall()


# In[26]:

import socket


# In[27]:

socket.gethostname()


# In[ ]:



