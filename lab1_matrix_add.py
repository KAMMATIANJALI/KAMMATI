r1=input("enter no.of rows for m1:");
c1=input("enter no.of coloumns for m1:");
r2=input("enter no.of rows for m2:");
c2=input("enter no.of coloumns for m2:");
a={}
print("enter elements for m1:")
for i in range(0,r1):
	for j in range(0,c1):
		a[i,j]=int(input())
b={}
print("enter elements for m2:")
for i in range(0,r2):
	for j in range(0,c2):
		b[i,j]=int(input())
c={}
for i in range(0,r1):
	for j in range(0,c1):
		c[i,j]=a[i,j]+b[i,j]
print("sum of two matrices is:")
for i in range(0,r1):
	for j in range(0,c1):
		print c[i,j]
