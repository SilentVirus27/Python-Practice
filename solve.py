#print and solve fibbonanci series
n=int(input("Enter n"))
sum=2
a=1
b=1
print("1+1",end='+')
for i in range(n+1):
	c=a+b
	a=b
	b=c
	if c<n+1:
		sum=sum+c
		print(c,end='+')
	else:
		break
print("=",sum)