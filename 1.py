print ("hello world")

if 5 > 2:
    print ("Five is greater than two.")

x = "fantastic"
def myfunc():
    x = "awesome"
    print("Python is " + x)

myfunc()
print("Python is " + x)

y = "Abc"
print(y)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

x = float(1)
y = int(2.8)
z = complex(1)

print(x)
print(y)
print(z)

import random
print(random.randrange(4, 10)) 

for x in 'banana':
    print(x)

a = 'Hello, World!'
print(len(a))
print(a.upper())
print(a.strip())
print(a.replace('H', 'J'))
print(a.split(','))

a = 'Hello'
b = 'World'
c = a + " " + b
print (c)

age = 50
txt = f"I am John, I am {age}"
print(txt)

txtx = f"I am John, I am {age:.3f}"
print(txtx)

abc = f"The age is {2*25}"
print(abc)

edf = "We are so-called the \"Vikings\" from the north"
print(edf)

c = 10
d = 5
if d > c:
    print("d is greater than c")
else:
    print("d is not greater than c")

f = 200
print (isinstance(f, int))

thislist = ["apple", "orange", "mango"]
thislist[1] = "blackcurrent"
print(thislist)

thislistt = ["Aplle", "Mapple", "Orange", "Mango", "Guava"]
thislistt[2:3] = ["Blackcurrent", "Lychi"]
print(thislistt)

tthislist = ["apple", "banana", "cherry"]
tthislist.append("orange")
print(tthislist)

tthislist.insert(0, "mango")
print(tthislist)

thislist.extend(tthislist)
print(thislist)

thislist.remove("orange")
print(thislist)

thislisst = ["apple", "banana", "cat"]
i = 0
while i < len(thislisst):
    print(thislisst[i])
    i = i + 1

[print(x) for x in thislisst]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

nowlist = [ x for x in range(10)]
print(nowlist)

nowlist = [x.upper() for x in fruits]
print(nowlist)

i = 1
while i < 6:
 print(i)
 i += 1

 adj = ("red", "big", "tasty")
 fruits = ("apple", "banana", "cherry")

for x in adj:
    for y in fruits:
        print(x, y)

def tri__recursion(k):
    if (k > 0):
        result = k + tri__recursion(k - 1)
        print (result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri__recursion(9)

class MyClass:
    x =5
p1 = MyClass()
print (p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1)


class Person:
    def __init__(idc, name, age):
        idc.name = name
        idc.age = age
    def myfunc(abc):
        print("My name is" + abc.name)

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1.age)   


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)


class  MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2020, 1, 1)
print(x.strftime("%B"))


import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])

import json
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x, indent=2)
print (y)

import re
txt = "The rain in Spain"
x= re.search("^The.*Spain$", txt)

if x: 
    print("YES! We have a match!")
else:
    print("No match")

    
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w", txt)
print(x.span())

#username = input("Enter username: " )
#9print("Username is: " + username)

price = 49 
txt = f"It is very {'Exprensive' if price>50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

f = open("C:\\Users\I-483\Desktop\P\demo.txt", "r")
print(f.read())

f = open("demo.txt", "r")
print(f.read(5))

f = open("demo.txt", "r")
for x in f:
    print(x)

"""
f = open("C:\\Users\I-483\Desktop\P\demo.txt", "a")
f.write("This is the new text!")
f.close()

f = open("demo.txt", "r")
print(f.read())
"""
f = open("C:\\Users\I-483\Desktop\P\demo.txt", "w")
f.write("Woops! I have deleted all the text.")
f.close()
f = open("demo.txt", "r")
print(f.read())

"""f = open("myfilee.txt", "w")"""