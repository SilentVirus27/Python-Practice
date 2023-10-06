#student Marks Memo
Rn=(input ("enter roll no"))
Nm=input("enter name")
m1=int(input("enter marks and subject"))
m2=int(input("enter marks and subject"))
m3=int(input("enter marks and subject"))
m4=int(input("enter marks and subject"))
m5=int(input("enter marks and subject"))
total=m1+m2+m3+m4+m5
per=total/500*100
if m1<40 and m2<40 and m3<40 and m4<40 and m5<40:
	gr="fail"
elif per>=70:
	gr="Distinction"
elif per>=60:
	gr="first class"
elif per>=50:
	gr="second class"
else:gr="pass class"
print("sibar")
print("seat no:_________",Rn)
print("name:_________",Nm)
print("___________________")
print("subject name_____________marks obtain")
print("________________")
print("subject1___________",m1)
print("subject2___________",m2)
print("subject3___________",m3)
print("subject4___________",m4)
print("subject5___________",m5)
print("_______________")
print("total ",total)
print("persentage:            ",per,"        Gread",gr)
print("___________")
