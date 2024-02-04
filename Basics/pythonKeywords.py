import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")

print(keyword.kwlist)

# True, False, and None Use in Python

print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == None)


# For, while, break, continue keyword Use in Python

for i in range(10):

	print(i, end=" ")
	if i == 6:
		break

print()

i = 0
while i < 10:
	
	print(i, end=" ")

    
	i += 1 
     
print()

# def keyword for functiom
def fun():
	print("Inside Function")


fun()


# class keyword for to create classes

class Dog:

	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()




import math as gfg

print(gfg.factorial(26))

n = 10
for i in range(n):

	# pass can be used as placeholder
	# when code is to added later
	pass

# Lambda keyword
g = lambda x: x*x*x

print(g(7))


# Return keyword
def fun():
	S = 0

	for i in range(10):
		S += i
	return S


print(fun())

# Yield Keyword


def fun():
	S = 0

	for i in range(10):
		S += i
		yield S


for i in fun():
	print(i)



# import keyword
from math import factorial
import math
print(math.factorial(10))

# from keyword
print(factorial(10))

a = 4
b = 0
try:
	k = a//b
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')

print("The value of a / b is : ")

# assert b != 0, "Divide by 0 error"
# print(a / b)

# temp = "geeks for geeks"
# if temp != "geeks":
# 	raise TypeError("Both the strings are different.")


# del in Python

# del is used to delete a reference to an object. Any variable or list value can be deleted using del.

my_variable1 = 20
my_variable2 = "GeeksForGeeks"
print(my_variable1)
print(my_variable2)
del my_variable1
del my_variable2
print(my_variable1)
print(my_variable2)


# Global, Nonlocal in Python

# global: This keyword is used to define a variable inside the function to be of a global scope.

# non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.


a = 15
b = 10
def add():
	c = a + b
	print(c)
add()
def fun():
	var1 = 10

	def gun():
		nonlocal var1
		
		var1 = var1 + 10
		print(var1)

	gun()
fun()
