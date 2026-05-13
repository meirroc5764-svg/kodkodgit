# #1
# age = int(input("enter age:"))
# if age < 0 and age > 120:
#     print("Invalid")
# elif age <= 12:
#     print("child")
# elif age < 18:
#     print("teen")
# else:
#     print("adult")
#2
# User_char = input("enter character:")
# if  not (User_char >= "A" and User_char <= "Z") and not(User_char >= "a" and User_char <= "z"):
#     print("Invalid")

# elif User_char in ["a", "e", "i", "o", "u"]:
#     print("Vowel")

# else:
#     print("Consonant") 
#3
# age = int(input("enter age:"))
# vip_cart=input("You have VIP cart?(enter yes or no)")
# if age < 18 :
#     print("")
# elif   age >= 18 and vip_cart == "yes":
#     print("welcome")
# elif age in [19,20,21]:
#     print("welcome")       
#4
# the_password = "12345678"
# user_enter = input("enter password")
# if len(user_enter)<8:
#     print("Too short")
# elif user_enter == the_password:
#     print("Access Granted")
# else:
#     print("Wrong password")
#5
# x = int(input("enter x cordinator:"))
# y = int(input("enter y cordinator:"))
# if (x < 10 or y < 20) or (x > 50 or y > 80):
#     print("Outside the rectangle")
# elif x == 10 or y == 20 or x == 50 or y == 80:
#     print("On the edge")
# else:
#     print("Inside the rectangle")       
#6
# user_name = input("Enter your name:")
# print("welcome",user_name or "anonim")
#8
# a = int(input("enter number"))
# b = int(input("enter number"))
# c = int(input("enter number"))
# print((a > 0)+(b > 0)+ (c > 0))
#10
# score = int(input("enter score"))
# print("A"if score > 90 else "B" if score > 80 and score < 90 else "C" if score < 80 and score > 69 else "F" )