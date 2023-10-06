import os 
fn=input("Enter FieName:")
fp=open(fn,"r")
str=fp.read()
fp.close()
os.remove(fn)
fp=open(fn,"w")
for i in range(len(str)):
	if((ord(str[i])>=ord('a')) and (ord(str[i])<=ord('z'))):
		fp.write(chr(ord(str[i])-(ord('a') -ord('A'))))
	else:
		fp.write(str[i])
	close()