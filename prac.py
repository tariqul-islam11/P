#summation
# fnum = int(input("Enter first number: "))
# lnum = int(input("Enter last number: "))

# print("Sum=  ", fnum + lnum)

#Math
# side = float(input("Enter squar side: "))
# print("Area= ", side * side)

#Average
# a = float(input("Enter first number: "))
# b = float(input("Enter last number: "))
# print("Avg: ", (a+b)/2)

#Greater number
# a = int(input("Enter first number: "))
# b = int(input("Enter last number: "))

# if (a>=b):
#     print("True")
# else:
#     print("False")

#length
# c = str(input("Enter first name: "))
# print(len(c))
#How many character
# d = str("The code will start from $")
# print(d.count("$"))

#if__elif__else condition
# mark = int(input("Enter marks: "))

# if (mark >= 90):
#     print("The grade is A")
# elif (mark >= 80 and mark < 90):
#     print("The grade is B")
# elif (mark >= 70 and mark < 80):
#     print("The grade is C")
# elif (mark < 70):
#     print("The grade is D")

#Odd or Even
# num = int(input("Enter a number: "))
# rem = num % 2

# if (rem == 0):
#     print("The number is Even")
# else:
#     print("The number is Odd")

#Which number is greater
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if (num1 > num2 and num1 > num3):
#     print("The first number is greater.", num1)
# elif (num2 > num1 and num2 > num3):
#     print("The second number is greater.", num2)
# elif (num3 > num1 and num3 > num2):
#     print("The third number is greater.", num3)

#If a number can be divided by 7
# num = int(input("Enter a number: "))

# if(num % 7 == 0):
#     print("num is multiple of 7")
# else:
#     print("Num is not multiple of 7")

#List
# list1 = str(input("Enter first favourite movie: "))
# list2 = str(input("Enter second favourite movie: "))
# list3 = str(input("Enter third favourite movie: "))

# print([list1, list2, list3])

#List2
# list1 = [1, 2, 3, 2, 1]
# list2 = [1, 2, 3, 4, 5]

# c_list1 = list1.copy()
# c_list1.reverse()
# c_list2 = list2.copy()
# c_list2.reverse()

# if(c_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# if(c_list2 == list2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Tuple

#tup = ("C", "D", "A", "A", "B", "B", "A")
#tup.count("A")
#print(tup.count("A"))

#Sort
# tup = ["C", "D", "A", "A", "B", "B", "A"]
# tup.sort()
# print(tup)

#Dictionary1

# dict = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
# }

# print(dict)
# print(type(dict)) 

#Set1

# subjects = {
#     "python", "java", "C++", "python", "javascript", "java",
#     "python", "java", "C++", "C"
# }

# print(len(subjects))

#Dictionary2
# marks = {}

# x = int(input("Enter marks of Physics: "))
# marks.update({"Physics": x})

# x = int(input("Enter marks of Chemistry: "))
# marks.update({"Chemistry" : x})

# x = int(input("Enter marks of Maths: "))
# marks.update({"Maths" : x})

# print(marks)

#Set2

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)

#Loop
#While
#Problem 1
# i = 1

# while i <= 100:
#     print(i)
#     i += 1

#Problem 2
# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

#Problem3
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

#Problem4
# nums = [1, 4, 9, 16, 21, 36, 49, 64, 81, 100]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

#Problem5
# nums = (1, 4, 9, 16, 21, 36, 49, 64, 81, 100)

# x = 49

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#     else:
#         print("Finding...")
#     i += 1

#Break
 
# nums = (1, 4, 9, 16, 21, 36, 49, 64, 81, 100)

# x = 49

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break
#     else:
#         print("Finding...")
#     i += 1

#Continue

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

#Continue even

# i = 0
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#For Loop
# nums = [1, 4, 9, 16, 21, 36, 49, 64, 81, 100]

# for num in nums:
#     print(num)

#For Loop 2
# nums = (1, 4, 9, 16, 21, 36, 49, 64, 81, 100, 49)

# x = 49

# idx = 0
# for num in nums:
#     if (num == x):
#         print("The number is found at idx", idx)
#     idx += 1

#For Loop 3

# for i in range(10): #range(stop)
#     print(i)

# for i in range(2, 10): #range(start, stop)
#     print(i)

# for i in range(2, 10, 2): #range(start, stop, step size)
#     print(i)

#For loop practice
# for i in range(101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n * i)

#While loop practice 1
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Total sum = ", sum)

#While loop practice 2
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial = ", fact)

#For loop practice 1

# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print("Factorial =", fact)

#Funtions 1

# nums = [1, 2, 3, 4, 5]
# def print_len(list):
#     print(len(list))
# print_len(nums) 

#Funtions 2
# cities = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Rongpur"]
# heroes = ["Iron-Man", "Thor", "Spider-Man", "SuperMan", "Batman", "Bots"]

# def print_len(list):
#     print(len(list))

# print_len(heroes)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(heroes)

#Funtions 3

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)

#Funtions 4

# def converter(usd_val):
#     bdt_val = usd_val * 117.50
#     print(usd_val, "USD =", bdt_val, "BDT")

# converter(100)

#Recursive Function

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(4))

#Recursive Function Practice 1

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(20)
# print(sum)

#Recursive Function Practice 2

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["A", "B", "C", "D", "E"]

# print_list(fruits)

#File I/O

#Read File
# f = open("demo.txt", "r")

# data= f.read()
# print(data)

# data = f.readline()
# print(data)

# data = f.readline()
# print(data)

# f.close()

# f = open("demo.txt", "w")

# f.write("This is the new text using the write, which means we are overwriting the texts.")

# f.close()

# f = open("demo.txt", "a")

# f.write("\nThen this is the appended text.")

# f.close()

# f = open("sample.txt", "w")
# f.close()

#File I/O with "with" syntax

#File I/O practice 1

# f = open("practice.txt", "w")

# f.write("Hi everyone\nwe are learning file I/O\nusing Java.\nI likke programming in Java.")

# f.write()
# f.close()

#File I/O practice 1
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     data = f.write(new_data)


#File I/O practice 3
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found") 

# check_for_word()


#File I/O practice 4

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()


#File I/O practice 5

# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val)) % 2 == 0:
#             count += 1

# print(count)

#__init__ function

# class student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding student marks in database..")

# s1 = student("karan", 98)
# print(s1.name, s1.marks)

# s2 = student("arjun", 99)
# print(s2.name, s2.marks)

# print(s2.college_name)

#OOP Practice

# class Student:

#     @staticmethod
#     def hello():
#         print("Hello")

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is: ", sum/3)

# s1 = Student("Tony Stark", [97, 98, 99])
# s1.hello()
# s1.get_avg()

#Abstraction
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Tk.", amount, "was debited")
        print("Total Balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Tk.", amount, "was credited.")
        print("Total Balance is", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(5000)
acc1.credit(10000)
acc1.credit(15000)

#Private Public

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)


# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

#Static Method

# class Student:

#     @staticmethod
#     def hello():
#         print("Hello")

# s1 = Student   
# s1.hello()

#Single Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar:
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.name)
# print(car2.name)

#Multilevel Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()

#Multiple Inheritance

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#Super() Method

# class Car:
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")
    
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().start()
#         super().__init__(type)
#         super().stop()

# car1 = ToyotaCar("Prius", "Electric")
# print(car1.type)

#Class method

# class Person:
#     name = "anonymous"
    
#     def changeName(self, name):
#         self.__class__.name = "Tarek"
#         #self.__class__. OR Person.name 

# p1 = Person()
# p1.changeName("Tarek Islam")
# print(p1.name)
# print(Person.name)


#Class method 2

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Tarek Islam")
# print(p1.name)
# print(Person.name)


#Property decorator
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)

#Polymorphism

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
    
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg  = self.img - num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 5)
# num1.showNumber()

# num2 = Complex(3, 3)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num1 = Complex(5, 5)
# num1.showNumber()

# num2 = Complex(3, 3)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()

#OOPS Practice 1

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

#OOP Practice 2

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Elon Mask", 50)
# engg1.showDetails()


#OOP Practice 3

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
    
#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr1 = Order("chips", 20)
# odr2 = Order("tea", 15)

# print(odr1 > odr2)