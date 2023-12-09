#!/usr/bin/python3
# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def Say_Hello(name, age):
    print(f"Hello {name} your age is {age}")

print("Using normal function:")
Say_Hello("Mohamed", 22)

# The same code put Using lambda

print("\nUsing lambda function:")
hello = lambda name, age: print(f"Hello {name} your age is {age}")
hello("Mohamed", 22)

print("\n")

print(Say_Hello.__name__)
print(hello.__name__)

print("\n")

print(type(Say_Hello))
print(type(hello))
# ========================================================================
print("=" * 30)
def sumTwoNumbers(a, b):
    return a + b

print("Using Normal function: {}".format(sumTwoNumbers(5, 10)))

# The same code put Using lambda
x = lambda a,b: a + b
print((lambda a,b: a + b)(2,3))
print("Using lambda function: {}".format(x(5, 5)))

# =======================================================================
print("=" * 30)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# =======================================================================
print("=" * 30)

# you can iterate in two list for exaple to add two list

num1 = [1, 2, 3]
num3 = [4, 5, 6]

result = map(lambda a,b: a + b, num1, num3)
print(list(result))   # output: [5, 7, 9]