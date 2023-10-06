#sum of n natural number
n=int(input("Enter n"))
sum=0
for i in range(1,n+2,2):
	# if i % 2 == 0:
	sum+=i
print("sum of all odd natural number in given range is :",sum)