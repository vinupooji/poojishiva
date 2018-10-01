def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def multiply(a,b):
	return a*b

def division(a,b):
	return a/b

i=int(input("enter number A: "))
j=int(input("enter number B: "))

d=add(i,j)
print("addition:",d)

print("subtraction: ",sub(i,j))

print("multiplication: ",multiply(i,j))

print("division: ",division(i,j))

