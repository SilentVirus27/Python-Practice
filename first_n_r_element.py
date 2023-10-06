inpt=input('Enter a string input\n')
next=0
for a in inpt:
    next+=1
    if next<len(inpt):
        if a==inpt[next]:
            print(a,'=>',inpt[next],'Repeating Element')
            break;
    else: print('No repeating element found')
