#1)
# def safe_int(s):
#     try:
#         int(s)
#         return s
#     except:
#         return None

#2)
# def safe_divide(a, b):
#     try:
#        return a / b 
#     except ZeroDivisionError:
#         return "undefined"

#3)
# def read_first_line(path):
#     try:
#         with open(path, "r",) as f:
#             f = f.readline()
#             print(f)
#             return f
#     except FileNotFoundError:
#         return None
#     finally:
#         print("file close")

#3)
# def get_value(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return "missing"

#4)
# def parse_ints(values):
#     new_list = []
#     for i in values:
#         try:
#             int(i)
#             new_list.append(i)
#         except ValueError:
#             continue   
#     return new_list

#5)
# def  set_age(age):   
#     try:
#         int(age)
#         if not 150 >= age >= 0:
#             raise ValueError("not corect age")
#         else:
#             return age
#     except ValueError:
#         print("not age")
#         raise

#6)
# def retry(func, n):
#     eror = None
#     try:
#         for i in range(n):
#             try:
#                 func()
#             except Exception as e:
#                 eror = e
#         return eror        
#     except ValueError:
#         print("n not a number")

#7)
# def count_errors(funcs):
#     count = 0
#     for i in funcs:
#         try:     
#             i()
#         except:
#             count += 1
#     return count
            
#8)
# def load_config(path):
#     try:
#         with open (path, "r") as f:
#             the_line = f.readline()
#             return int(the_line)
#     except Exception as e:
#         raise RuntimeError(f"the Eror is {e}")
