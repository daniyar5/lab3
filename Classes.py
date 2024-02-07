#ex1
# class First:
#     def getString(self):
#         self.s = input("Enter a string: ")

#     def printString(self):
#         print(self.s)

# someobj = First()
# someobj.getString()
# someobj.printString()




#ex2 + ex3
# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
    

# choice = str(input("Which shape's area do you want to find? Square or Rectangle?"))
# if (choice == "Square"):
#     user_length = int(input("Please enter the length of the square: "))
#     square_obj = Square(user_length)
#     print("This is the area of your square: ", square_obj.area())

# elif(choice == "Rectangle"):
#     user_length = int(input("Please enter the length of the rectangle: "))
#     user_width = int(input("Please enter the width of the rectangle: "))
#     rectangle_obj = Rectangle(user_length, user_width)
#     print("This is the area of your rectangle: ", rectangle_obj.area())




#ex4
# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def show(self):
#         print("My current coordinates are: "+ str(self.x) + " " + str(self.y))

#     def move(self, new_x, new_y):
#         self.x = new_x 
#         self.y = new_y
#     def dist(self, x, y, x2, y2):
#         self.x2 = x2
#         self.y2 = y2
#         distance = (x2 - x)**2 + (y2 - y)**2
#         print("The distance between this two points is approximately " + str(round(math.sqrt(distance))))


# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# mycord = Point(x, y)
# mycord.show()



# new_x = int(input("Enter new x: "))
# new_y = int(input("Enter new y: "))
# mycord.move(new_x, new_y)
# mycord.show()



# x2 = int(input("Enter second x: "))
# y2 = int(input("Enter second y: "))
# mycord.dist(x, y, x2, y2)




#ex5

# class Account:

#     def __init__(self, owner, initial_balance = 0):
#         self.owner = owner
#         self.balance = initial_balance


#     def deposit(self, owner, depo_check):
        
#         depo_check = int(input("How much money do you want to deposit? "))
#         self.balance = self.balance + depo_check
#         print(str(owner) + ", you deposited " + str(depo_check) + ". The balance is " + str(self.balance))
        

#     def withdraw(self, owner, withdraw_check):
#         withdraw_check = int(input("How much money do you want to withdraw? "))
#         if (withdraw_check > self.balance):
#             print("You cannot withdraw all your balance.")
#         else:
#             self.balance = self.balance - withdraw_check
#             print(str(owner) + ", you withdrew " + str(withdraw_check) + ". The balance is " + str(self.balance))


# name = input("Enter your name: ")
# initial_balance = int(input("Enter balance on your Account: "))
# somef = Account(name, initial_balance)
# somef.deposit(name, initial_balance)
# somef.withdraw(name, initial_balance)






#ex6

#main function
def is_prime(n):    
    if n < 2:
        return False    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:            
            return False
    return True

#inputing our list of numbers
numbers = [int(i) for i in input().split()]

#creating our lambda function
myfilter = lambda x: is_prime(x)

#into the list() we filter our list of numbers with conditions of lambda function
listof_primes = list(filter(myfilter, numbers))

#printing our new list of primes
print("Prime numbers:", listof_primes)



