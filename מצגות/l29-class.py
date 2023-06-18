import random
# print("Hello class")

num = 8
# print(type(num))

# c = num + 1.7
# print(c)
# print(type(c))

# print("printing new c")
# c=int(c)
# print(type(c))
# print(c)

# answer=True
# print(type(answer))
# print(2>3)
# print("num =",num,"answer =",answer)
# print(num)

# a=56
# b=32
# c=a//b

# print("a =",a)
# print("b =",b)
# print("c =",c)
# print("shever",int(a/b),c,"/",b)

# print("1 numer is: " + str(random.randrange(1,37)))
# print("2 numer is: " + str(random.randrange(1,37)))
# print("3 numer is: " + str(random.randrange(1,37)))


# def generate_lotto_numbers():
#     lotto_numbers = []
#     while len(lotto_numbers) < 6:
#         number = random.randint(1, 37)  # Generate a random number between 1 and 49
#         if number not in lotto_numbers:
#             lotto_numbers.append(number)
#     return lotto_numbers

# # Generate and print the lotto numbers
# numbers = generate_lotto_numbers()
# print("Lotto Numbers:", numbers)

# x = 22
# if not x == 21:
#     print("Yes, x is 21")
#     if x:
#         print("ok")


# x = False
# if x:
#     print("Yes, x is True")
# else:
#     print("No, x is False")

# age = 24
# print("Congratulation!") if age == 23 else print("your are so young!") if age < 23 else print("we love adult people!") 


# if age < 23:
#     print("your are so young!")

# if age > 23:
#     print("we love adult people!")


# לולאת while

# number_of_bugs = 1
# while number_of_bugs < 5:
#     number_of_bugs +=1 # number_of_bugs = number_of_bugs + 1
#     print("Not Critical")

# while True:
#     print("Hi")

# while True:
#     print("Hi")
#     break
#     print("Bye")

# while True:
#     print("Hi")
#     while True:
#         print("Bye")
#         break     
#     break 

# i=1
# while i<=75:
#     if i%2 != 0:
#       print(i,end =" ") # use end = " " to print in the same line
#     i += 1

# לולאות for

# for i in [0,1,2,3]:
#     print(i*5, end = " ")

# print("\n")
# for i in ['Ben gurion', 'Sharet', 'Begin', 'Rabin','Netanyahu']:
#     if i=="Netanyahu":
#         print(i+" was Israel's crime minister")
#     else:
#         print(i+" was Israel's prime minister")

# for i in range(10):
#      print(i, end = " ")

# for i in range(2,10,3):
#     print(i, end = " ")

# for i in range(1,75,2):
#     print(i, end = " ")

# for i in range(16):
#     print("2 ^",i, "=",2**i)

# for i in range(8):
#     for j in range (i):
#         print("*", end =" ")
#     print()

# for i in range(8):    
#     print("*"*i)


# greetings ='Hello'
# greetings ="Hello"
# greetings = "what's up, doc?"
# greetings = 'Hi "QA"'

# print(greetings)

# a=2
# b=3
# print(a+b)

# a='2'
# b='3'
# print(a+b)
# print(type(a+b))

# a=2
# b=int('3')
# print(a+b)

# חיתוך מחרוזות

# greetings ='Hello class QA'
# print(greetings[0:2])
# print(greetings[1:7])
# print(greetings[-5:-1])

# print(greetings[-1::-1]) # מה זה מדפיס?

# message = "Hello " + "class QA"
# print(message)
# print(len(message))
# print(message.upper())
# print(message.lower())
# print(message.find('s'))


# def print_hello():
#     for i in range(4):
#      print("Hello class")

# # print("Hello class")

# print_hello()

# def print_seven(a):
#     x = 7*a
#     return x

# print_seven(6)
# print(print_seven(print_seven(6)))

# def seven_eleven():
#     x = 7
#     y = 11
#     return x, y

# var1, var2 = seven_eleven()
# print("{} {}".format(var1, var2))