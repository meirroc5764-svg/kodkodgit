#1
# def sort_active_pepole(pepole_list):
#     active_pepole = []
#     for person in pepole_list:
#         if person[1] >= 18 and person[2] == "active":
#             active_pepole.append(person[0])
#     return active_pepole

# pepole = [
#     ["Dan", 25, "active"],
#     ["Noa", 16, "active"],
#     ["Yael", 30, "inactive"],
# ]

# print(sort_active_pepole(pepole))
#2 
# def stock_sum(stock, quantity):
#     stock -= quantity
#     return stock

# def order_print(order):
#     print(f"Order {order[-1]}: {order[0]} bought {order[2]}x {order[1]} for ${order[3]}")

# def full_order(user_email, product_name, price, quantity):
#     order_user = user_email
#     order_product = product_name
#     order_quantity = quantity
#     order_total = price
#     order_status = "confirmed"
#     return order_user, order_product, order_quantity, order_total, order_status
    
# def discount(product_price,quantity):
#     price = product_price * quantity
#     if quantity >= 10:
#         price *= 0.9
#     if quantity >= 50:
#         price *= 0.85
#     return price

# def product_chek_quantity(quantity,stock):
#     if quantity <= 0 or quantity > stock:
#         print("Invalid quantity")
#         return None
#     return True

# def product_chek_email(user_email):
#     if not user_email:
#         print("Invalid user")
#         return None
#     return True

# def handle_purchase(user_email, product_name, product_price, stock, quantity):
#     if (product_chek_email(user_email)) and (product_chek_quantity(quantity,stock)):
#         sum_price = discount(product_price,quantity)
#         order = full_order(user_email, product_name, sum_price, quantity)
#         stock_sum(stock,quantity)
#         order_print(order)        
#         return
#     return None
#3
# def save_new_information(names,grades):
#      # save to file
#         with open("students.txt", "w") as f:
#             for i in range(len(names)):
#                 f.write(f"{names[i]},{grades[i]}\n")

# def print_all_information(names,grades,all_information):
#         # print report
#         print("=== Student Report ===")
#         for i in range(len(names)):
#             print(f"  {names[i]}: {grades[i]}")
#         print(f"Average: {all_information[1]:.1f}")
#         print(f"Top students: {all_information[2]}")
#         print(f"Failing: {all_information[3]}")

#         return names, grades

# def sum_students_information(grades):
#     # calculate stats
#         total = sum(grades)
#         average = total / len(grades)
#         top_count = sum(1 for g in grades if g >= 90)
#         failing_count = sum(1 for g in grades if g < 56)
#         return (total,average,top_count,failing_count)

# def add_studens(grades,new_grade):
#     # add student
#     grades.append(new_grade)
#     return grades

# def student_name_chek(new_name):
#     # validation
#     if not new_name or len(new_name) < 2:
#         print("Error: invalid name")
#         return None
#     return True

# def student_grade_chek(new_grade):
#     # validation
#     if new_grade < 0 or new_grade > 100:
#         print("Error: grade must be 0-100")
#         return None
#     return True

# def manage_students(names, grades, new_name, new_grade):
#     if (student_name_chek(new_name)) and (student_grade_chek(new_grade)):
#         add_studens(grades,new_grade)
#         studens_information = sum_students_information(grades)
#         print_all_information(names,grades,studens_information)
#         save_new_information(names,grades)
# manage_students(["anny"],[100],"danny",90)
#4
