
# coding: utf-8

# In[1]:

get_ipython().run_cell_magic(u'timeit', u'', u'l1=range(10000)')


# In[2]:

get_ipython().run_cell_magic(u'timeit', u'', u'l1=range(1000)\nl2=range(1000)\n[i+j for i,j in zip(l1,l2)]')


# In[3]:

import numpy as np


# In[4]:

get_ipython().run_cell_magic(u'timeit', u'', u'ar1 = np.arange(1000)\nar2= np.arange(1000)\nar1+ar2')


# In[5]:

np.arange(0,1,0.1)


# In[6]:

ar1 = np.arange(20)


# In[7]:

ar1


# In[8]:

ar2 = ar1.reshape(5,4)


# In[9]:

ar2


# In[10]:

ar2.size


# In[11]:

ar2.shape


# In[13]:

ar2.ndim


# In[14]:

ar2.max()


# In[15]:

ar2.sum()


# In[16]:

ar2.mean()


# In[17]:

ar2.std()


# In[18]:

ar2


# In[19]:

ar2[ar2>10]


# In[20]:

ar2


# In[21]:

ar2.sum(axis=1)


# In[22]:

ar2.sum(axis=0)


# In[23]:

ar2.max(axis=1)


# In[24]:

ar2.max(axis=0)


# In[25]:

ar2


# In[26]:

ar2[0]


# In[27]:

ar2[1]


# In[28]:

ar2[0:0]


# In[29]:

ar2[0:1]


# In[30]:

ar2[0:3]


# In[31]:

ar2[0:4]


# In[32]:

ar2[0:2]


# In[33]:

ar2[0:2,0]


# In[34]:

ar2[:,0]


# In[35]:

ar2[0:2,0:2]


# In[36]:

ar2.argmax()


# In[37]:

ar2.argmax(axis=0)


# In[38]:

ar2


# In[40]:

ar3 = np.arange(10,30).reshape(5,4)


# In[41]:

ar3


# In[42]:

ar3.argmax()


# In[43]:

ar3[0]=[100,200,300,400]


# In[44]:

ar3


# In[45]:

ar3t = ar3.T


# In[46]:

ar3t


# In[47]:

l=[10,20,30,40]
ar1 = np.array(l)


# In[48]:

ar1


# In[49]:

ar1.dtype


# In[50]:

l=[10,20.3,40,50.6]
ar1 = np.array(l)


# In[51]:

ar1


# In[52]:

l=['qwe',10,20.3,1+2j,[1,2,3,4]]
ar1 = np.array(l)


# In[54]:

l=['qwe',10,20.3,1+2j]
ar1 = np.array(l)


# In[55]:

ar1


# In[56]:

c=1+2j


# In[57]:

type(c)


# In[58]:

str(c)


# In[59]:

l1=[1,23,4]
str(l1)


# In[61]:

l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ar1 = np.array(l)


# In[62]:

ar1


# In[63]:

l=[12,34,[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ar1 = np.array(l)


# In[64]:

ar1


# In[65]:

get_ipython().magic(u'pinfo np.append')


# In[66]:

ar1


# In[67]:

ar1.flatten()


# In[69]:

get_ipython().magic(u'pinfo np.append')


# In[70]:

ar1.shape


# In[71]:

ar2=np.arange(12)


# In[72]:

ar2


# In[73]:

ar2 = ar2.reshape(3,4)


# In[74]:

ar1


# In[75]:

ar2


# In[76]:

ar1+ar2


# In[77]:

ar1*ar2


# In[78]:

ar1/ar2


# In[79]:

ar1


# In[80]:

ar2


# In[81]:

ar4 = np.append(ar1,ar2)


# In[82]:

ar4


# In[83]:

ar4 = np.append(ar1,ar2,axis=0)


# In[84]:

ar4


# In[85]:

ar4 = np.append(ar1,ar2,axis=1)


# In[86]:

ar4


# In[87]:

ar1


# In[88]:

ar1+10


# In[89]:

ar2 = ar1+10


# In[90]:

ar2


# In[91]:

ar1


# In[92]:

"""  
y=f(x)
f(x)=2x+3
"""
x=[10,20,30,40,50,60]
def fun(x):
    return 2*x+3
y = map(fun,x)


# In[93]:

y


# In[94]:

# vector functioning
"""  
y=f(x)
f(x)=2x+3
"""
x=[10,20,30,40,50,60]
def fun(ar1):
    ar2 = ar1*2
    ar3 = ar2+3
    return ar3
fun(x)    


# In[95]:

# vector functioning
"""  
y=f(x)
f(x)=2x+3
"""
x=[10,20,30,40,50,60]
ar = np.array(x)
def fun(ar1):
    ar2 = ar1*2
    ar3 = ar2+3
    return ar3
y=fun(ar)    


# In[96]:

y


# In[99]:

"""
y=f(x){ x<1, 2x+3}
       {x>=1 x**2}
"""
import math
x=[-2,10,30,-4,1,5]
def fun(x1):
    if x1<1:
        return 2*x1+3
    else:
        return math.pow(x1,2)
y=map(fun,x)   
print y


# In[102]:

get_ipython().magic(u'pinfo np.where')


# In[106]:

x=[-2,10,30,-4,1,5]
x= np.array(x)
ar2 =np.where(x<1, 2*x+3,x**2)


# In[107]:

ar2


# In[108]:

"""
y=f(x){ x<1, 2x+3}
       {x>1 x**2}
       {x=1 x**3}
"""
x=[-2,10,30,-4,1,5]
x=np.array(x)
ar2 = np.where(x<1,2*x+3,x)
ar3 = np.where(x>1,x**2,ar2)
ar4 = np.where(x==1,x**3,ar3)


# In[109]:

ar4


# In[110]:

def fun(x):
    ar2 = np.where(x<1,2*x+3,x)
    ar3 = np.where(x>1,x**2,ar2)
    ar4 = np.where(x==1,x**3,ar3)
    return ar4
    
x=[-2,10,30,-4,1,5]
y=fun(np.array(x))


# In[111]:

x


# In[112]:

y


# In[113]:

import matplotlib.pyplot as plt
def fun(x):
    ar2 = np.where(x<1,2*x+3,x)
    ar3 = np.where(x>1,x**2,ar2)
    ar4 = np.where(x==1,x**3,ar3)
    return ar4
x=[-2,10,30,-4,1,5]
y=fun(np.array(x))
plt.plot(x,y)
plt.show()


# In[115]:

plt.plot(x,y,'r+')
plt.show()


# In[117]:

plt.bar(x,y)
plt.show()


# In[118]:

import pandas as pd


# In[119]:

tables = pd.read_html('http://www.w3schools.com/html/html_tables.asp')


# In[120]:

tables[0]


# In[121]:

import urllib2
resp = urllib2.urlopen('http://www.w3schools.com/html/html_tables.asp')


# In[122]:

resp.read()


# In[123]:

from bs4 import BeautifulSoup


# In[124]:

data = resp.read()


# In[125]:

data[0]


# In[126]:

import urllib2
from bs4 import BeautifulSoup
resp = urllib2.urlopen('http://www.w3schools.com/html/html_tables.asp')
data = resp.read()
soup = BeautifulSoup(data)


# In[127]:

soup


# In[129]:

soup.findAll('a')


# In[130]:

soup.findAll('h1')


# In[131]:

import turtle as t
class shape(object):
    def __init__(self,color="black",size=1):
        self.color=color
        self.size=size
class dot(shape):
    def __init__(self,x,y,color="black",size=1):
        self.x=x
        self.y=y
        shape.__init__(self,color,size)
class snow_man_parts(shape):
    def __init__(self,color="black",size=1):
        shape.__init__(self,color,size)
    def dot(self,x,y):
        t.up()
        t.goto(x,y)
        t.dot()
        
    def snowmansface(self,x,y):
        t.up()
        t.goto(x + 15,y)
        t.dot()
        t.goto(x - 15,y)
        t.dot()
        t.goto(x -15,y -25)
        t.down()
        t.forward(30)
        t.up()
    def snowmansarm(self,x,y,length,heading):
        t.up()
        t.goto(x,y)
        t.setheading(heading)
        t.down()
        t.forward(length)
        t.setheading(heading + 20)
        t.forward(20)
        t.up()
        t.back(20)
        t.down()
        t.setheading(heading - 20)
        t.forward(20)
        t.up()
        t.home()


class line(shape):
    def __init__(self,x1, y1, x2, y2,color='black',size=1):
        self.x1=x1
        self.y1=y1
        self.y2=y2
        self.x2=x2
        shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x1, self.y1)
          t.pendown()
          t.goto (self.x2, self.y2)
          t.penup()
    def __str__(self):
        return "line"
class circle(shape):
    def __init__(self,x,y,r,color="green",fill=0,size=1):
          # draw a circle
            self.x=x
            self.y=y
            self.r=r
            self.fill=fill
            shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x, self.y)
          t.pendown()
          t.begin_fill()
          t.width(7)
          t.color (self.color)
          t.fill(self.fill)
          t.circle (self.r)
          t.end_fill()
    def __str__(self):
        return "Circle"
class triangle(shape):
    def __init__(self,x,y,steps=3,color='black',size=1):
        self.x=x
        self.y=y
        self.steps=steps
        shape.__init__(self,color,size)

    def draw(self):
        t.pensize(3)
        t.penup()
        t.goto (self.x, self.y)
        t.color('yellow')
        t.begin_fill()
        t.forward(175)
        t.left(125)
        t.forward(200)
        t.left(125)
        t.forward(200)
        t.end_fill()
        t.penup()
        
    def __str__(self):
        return "triangle"
class rectangle(shape):
    def __init__(self,x,y,color="red",size=1):
        self.x=x
        self.y=y
        
        shape.__init__(self,color,size)
    def draw(self):
         t.pensize(3)
         t.penup()
         t.goto(self.x,self.y)
         t.color(self.color)
         t.begin_fill()
         t.forward(75)
         t.left(90)
         t.forward(90)
         t.left(90)
         t.forward(75)
         t.left(90)
         t.forward(90)
         t.left(90)
         t.end_fill()
    def __str__(self):
        return "rectangle"
class square(shape):
    def __init__(self,x,y,steps=4,color='black',size=1):
        self.x=x
        self.y=y
        self.steps=steps
        shape.__init__(self,color,size)
    def draw(self):
          t.penup()
          t.goto (self.x, self.y)
          t.pendown()
          t.begin_fill()
          t.color ('navy')
          t.circle (40, steps = 4)
          t.end_fill()
    def __str__(self):
        return "square"

def male_snow():
    circle_o=circle(-250,-250,120,color='red',fill=0)
    circle_o1=circle(-250,-10,90,color='red',fill=0)
    circle_o2=circle(-250,170,60,color='red',fill=0)
    circle_o3=circle(-250,85,10,color='green',fill=0)
    circle_o4=circle(-250,35,10,color='yellow',fill=0)
    circle_o5=circle(-250,-85,10,color='green',fill=0)
    circle_o6=circle(-250,-135,10,color='yellow',fill=0)
    circle_o2.draw()
    circle_o.draw()
    circle_o1.draw()
    parts_o=snow_man_parts()
    parts_o.snowmansarm(-150,60,70,20) 
    parts_o.snowmansarm(-350,60,70,160)
    parts_o.snowmansface(-250,240)
    line_o=line(-190,290,-310,290)
    line_o1=line(-240,215,-220,225)
    line_o2=line(-260,215,-280,230)
    line_o2.draw()
    line_o1.draw()
    line_o.draw()
    circle_o3.draw()
    circle_o4.draw()
    circle_o5.draw()
    circle_o6.draw()
    rectangle_o=rectangle(-285,290)
    rectangle_o.draw()
    
def female_snow():
    circle_o=circle(250,-250,120,color='black',fill=0)
    circle_o1=circle(250,-10,90,color='black',fill=0)
    circle_o2=circle(250,170,60,color='black',fill=0)
    circle_o3=circle(250,85,10,color='yellow',fill='yellow')
    circle_o4=circle(250,35,10,color='green',fill='pink')
    circle_o5=circle(250,-85,10,color='blue',fill='yellow')
    circle_o6=circle(250,-135,10,color='red',fill='pink')
    circle_o1.draw()
    circle_o.draw()
    circle_o2.draw()
    parts_o=snow_man_parts()
    parts_o.dot(235,220)
    parts_o.snowmansface(235,245)
    line_o=line(-60,290,-60,290)
    line_o1=line(160,80,80,10)
    line_o2=line(340,80,420,60)
    line_o3=line(420,60,330,-30)
    line_o4=line(230,290,200,230)
    line_o5=line(200,260,170,200)
    line_o6=line(260,280,320,230)
    line_o.draw()
    line_o1.draw()
    line_o2.draw()
    line_o3.draw()
    line_o4.draw()
    line_o5.draw()
    line_o6.draw()
    circle_o3.draw()
    circle_o4.draw()
    circle_o5.draw()
    circle_o6.draw()
    triangle_o=triangle(170,270)
    triangle_o.draw()
def main(): 
    t.title ('snowmen with colors')
    t.setup (1000, 1000, 0, 0)
    male_snow()
    female_snow()
    t.hidet()
    t.done()

main()


# In[ ]:



