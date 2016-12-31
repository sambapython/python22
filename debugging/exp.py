
a=10
b=20
c=30
l=['1','2',10]
l2=[]

for i in l:
	if isinstance(i,str) and i.isdigit():
		res=int(i)
		l2.append(res)
	elif isinstance(i,int) or isinstance(i,float):
		l2.append(i)
	else:
		l2.append(0)
a,b,c=l2
def fun(a1,b1,c1):
	print "a={0},b={1},c={2}".format(a,b,c)
	a1=a1+10
	b1=b1+10
	c1=c1+10
	return a1+b1+c1
print fun(a,b,c)
print l2
print sum(l2)