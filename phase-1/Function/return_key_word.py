def function(a,b):
	x=a+b
	return x
def function2(a,b):
	y=a-b
	return y
def function3(a,b):
	z=(a+b)+(a-b)
	return z
a=int(input("a = "))
b=int(input("b = "))
print("a+b =",function(a,b))
print("a-b =",function2(a,b))
print("(a+b)+(a-b) =",function3(a,b))