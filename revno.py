#Reverse of digits of a given number
n=int(input("Enter number"))
sum=0
st=str(n)
rv=" "
for i in st:
	rv=i+rv
	r=int(rv)
print("Reverse Number of ",n,"is",r)