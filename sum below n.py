#Find the sum of all the multiples of 3 or 5 below n
#!/bin/python3

import sys

t = int(input().strip())

def triangleNumber (x) :
    return (x * x + x) // 2

for a0 in range(t):
    n = int(input().strip())
    threes = triangleNumber((n - 1) // 3) * 3
    fives = triangleNumber((n - 1) // 5) * 5
    fifteens = triangleNumber((n - 1) // 15) * 15
    total = threes + fives - fifteens
    print(int(total))
'''
import sys
t = int(input())
for _ in range(t):
    n,i,addition= int(input()),0,0
    while i<n:
        if ((i%3 == 0) or(i%5 == 0)):
            addition = addition + i
        i += 1
    print(addition)
'''
'''    
    if (n<=10**5):
        lis = [i for i in range (n) if ((i%3 == 0) or(i%5 == 0))]
        addition=sum(lis)
        print(addition)
    else:
        lis1 = [i for i in range (10**5) if ((i%3 == 0) or(i%5 == 0))]
        addition1=sum(lis1)
        lis2 = [i for i in range (10**5,n) if ((i%3 == 0) or(i%5 == 0))]
        addition2=sum(lis2)
        print(addition1+addition2) 
'''