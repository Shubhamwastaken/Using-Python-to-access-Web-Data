import re
hand=open('problem.txt')
x=list()
sum=[]
sum2=0
for l in hand:
	l=l.rstrip()
	y=(re.findall('[0-9]+',l))
	if len(y)> 0:
		x.append(y)

print(x)
for i in range(0,len(x)):
	sum1=0
	for j in range(0,len(x[i])):
		sum1=sum1+int(x[i][j])
	sum.append(sum1)
for a in range(0,len(sum)):
	sum2=sum2+sum[a]
print(sum2)