string1=input('Enter First String \n')
string2=input('Enter Second String \n')
l3=len(string1)+len(string2)
if l3>0:
    count1=0
    count2=0
    string3=" "
    for i in range(l3):
        if i % 2 == 0:
            if count1<len(string1):
                string3 += string1[count1]
                count1+=1
        else:
            if count2<len(string2):
                string3 += string2[count2]
                count2+=1
    print(string3)
else: print('Empty String')