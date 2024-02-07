#ex1
# x = int(input())
# def translate(grams):
#     ounces = 28.3495231 * grams
#     print(ounces)
# translate(x)




#ex2
# f = int(input())
# def farenheit(F):
#     C = (5 / 9) * (F - 32)
#     print(C)
# farenheit(f)




#ex3
# a = 35
# b = 94
# def solve(numheads, numlegs):
#     x = (numlegs - 2 * numheads) / 2
#     y = numheads - x
#     print(x, y)
# solve(a, b)



# ex4
# def primes(somelist):
#     for i in somelist:
#         if (i <= 1 or (i % 2 == 0 and i != 2)):
#             continue
#         elif (i == 2):
#             print(i)
#         else:
#             x = 2
#             while (x * x <= i):
#                 if (i % x == 0):
#                     break
#                 x = x + 1
#             else:
#                 print(i)
# Mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# primes(Mylist)






#ex5
# from itertools import permutations
# def permut_string():
#     s = (input())
#     perms = permutations(s)
#     for perm in perms:
#         print(''.join(perm))
# permut_string()




# ex6
# s = str(input())
# x = s.split()
# r = x[::-1]
# rs = " ".join(r)
# print(rs)




#ex7
# nums = []
# def has_33(nums):
#     n = int(input())
#     for i in range(n):
#         element = int(input())
#         nums.append(element)
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False

# print(has_33(nums))




#ex8
# nums = []
# def spy(nums):
#     n = int(input())
#     count = 0
#     for i in range(n):
#         element = int(input())
#         nums.append(element)
#     for i in nums:
#         if i == 0:
#             count += 1
#         elif i == 7 and count >= 2:
#             return True
#             break
#     return False

# print(spy(nums))





#ex9
# rad = int(input())
# def volume(rad):
#     v = (4 * rad**3 * 3.14) / 3
#     print(v)
# volume(rad)


#ex10
# old = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     old.append(element)
# def unique(new):
#     for i in new:
#         if (new.count(i) > 1):
#             new.pop(new.index(i))
#     print(new)
# unique(old)


#ex11
# word = str(input())
# def palindrom(word):
#     rword = word[::-1]
#     if (rword == word):
#         print("This is a palindrom")
#     else:
#         print("This is not a palindrom")
# palindrom(word)


    
#ex12
# somelist = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     somelist.append(element)
# def histogram(somelist):
#     for x in somelist:
#         print(end='\n')
#         for i in range(x):
#             print("*", end = '')
# histogram(somelist)


# ex13
# import random
# def guess():
#     print("Hello! What is your name?")
#     name = str(input())
#     print("Well, " + name + ", I am thinking of a number between 1 and 20.\nTake a guess")
#     guess_num = random.randint(1, 20)
#     answer = False
#     count = 1
#     while answer == False:
#         chosen_num = int(input())
#         if (chosen_num == guess_num):
#             answer = True
#             print("Good job, " + name + "! You guessed my number in " + str(count) + " guesses!")
#             break
#         elif (chosen_num > guess_num):
#             count = count + 1
#             print("Your guess is too high.\nTake a guess.")
#         elif (chosen_num < guess_num):
#             count = count + 1
#             print("Your guess is too low.\nTake a guess.")
# guess()