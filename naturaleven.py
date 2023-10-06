#sum of n natural number
n=int(input("Enter n"))
sum=0
for i in range(1,n+1):
	if i % 2 == 0:
		sum+=i
print("sum of all even natural number in given range is :",sum)