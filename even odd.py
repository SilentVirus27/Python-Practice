A = [10, 31, 6, 45, 62, 83, 1]
even = []
odd = []
for b in A:
	if b % 2 == 0:
		even.append(b)
	else:
		odd.append(b)
print("Even numbers: ",even)
print("Odd numbers: ",odd)