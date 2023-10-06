number=int(input('Enter random Number'))
c=1
for i in range(number,0,-2):
    c*= i
print('the double factorial of given number{',number,'}=',c)
