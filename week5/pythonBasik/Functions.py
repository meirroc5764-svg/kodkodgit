#1)
# def is_even(n):
#     if int(n) % 2 == 0:
#         return True
#     else:
#         return False
#2)
# def factorial(n):
#     sum = 1
#     for i in range(1,n+1):
#         sum *= i
#     return sum
#3)
# def sum_digit(n):
#         final_sum = 0
#         for i in n:
#             final_sum += int(i)
#         return str(final_sum)
# def digit_root(n):
#     if len(n) == 1:
#         return n 
#     else:
#         return digit_root(sum_digit(n))
#4)
# def is_palindrom(n):
#     if n[::-1] == n:
#         return True
#     else:
#         return False 
#6)
# def sum_digit(n):
#     sum = 0
#     while n > 0:
#         if n < 10:
#             sum += 1
#             return sum
#         n = n // 10
#         sum += 1
#7)
# def is_rever(n):
#     revers = ""
#     for i in str(n[::-1]):
#         if i == "0":
#             continue
#         revers += i
#     return revers 
#8)
# def move_zero(n):
#     for i in n:
#         if i == 0:
#             n.remove(i)
#             n.append(i)
#     return n
#9)
# def information(list_number):
#     big_num = max(list_number)
#     small_num = min(list_number)
#     totall = sum(list_number)
#     averge = totall / len(list_number)
#     # for i in list_number:
#     #     sum += i
#     return big_num, small_num, totall, averge
#10)
# def reverse_list(number_list):
#     revers_number_list = []
#     for i in number_list[::-1]:
#         revers_number_list.append(i)
#     return revers_number_list
#11)
def list_without_duplicates(user_list):
    new_list = []
    for i in user_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
print(list_without_duplicates([1,1,2,2,3,3,4,4,5,5,6,7,7,8,8,9,9,]))

    
