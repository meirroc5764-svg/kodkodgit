#1)
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         break
#     print(i)
#2)
# while True:
#     user_password = input("Enter your password:")
#     if user_password == "1234":
#         print("welcome")
#         break
#     print("Try again")
#3)
# product_list = []
# while True:
#     product = input("Enter product")
#     if product == "done":
#         print(product_list)
#         break
#     product_list.append(product)
#3.2.)
# for i in range(1,4):
#     for m in range(1,4):
#         if i == 2:
#             break
#         print(i)
#         print(m)    
#4)
# user_word = input("Enter word")
# sum=0
# for r in user_word:
#     if r in ["a", "e", "i", "o", "u"]:
#         sum += 1
# print(sum)
#5)
# for i in range(1,6):
#     for m in range(1,6):
#         print(f"{i} * {m} = {i * m}")
#6)
# user_word = input("enter word: ")
# revers = ""
# for i in user_word:
#     revers = i + revers
# print(revers)
#7)
# number = int(input("enter number: "))
# sum_digit = 0
# while number > 0:
#     if number % 2 == 0:
#         sum_digit += 1
#     number -= 1  
# print(sum_digit)
#8)
# user_word = input("enter word: ")
# finall_word = ""
# for i in user_word:
#     finall_word += i
#     finall_word += i
# print(finall_word)
#9)
# big_num = 0
# while True:
#     user_num = int(input("Enter number: "))
#     if user_num == 0:
#         print(big_num)
#         break
#     if user_num > big_num :
#         big_num = user_num    
#10)
# user_word = input("Enter word: ")
# finish = True
# for i in user_word:
#     if (i < "A") or (i > "Z" and i < "a") or (i > "z") \
#         and (i not in ["0","1","2","3","4","5","6","7","8","9"]):
#             finish = False    
#             break
# print(finish)
#11)
# user_num = int(input("enter number: "))
# final_num = 0
# while user_num > 0 :
#     if user_num < 10:
#         final_num += user_num
#         break  
#     final_num += (user_num % 10)
#     final_num = final_num * 10
#     user_num = user_num // 10    
# print(final_num)    