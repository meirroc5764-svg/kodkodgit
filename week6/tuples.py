import math
#1)
# def elements_sum(user_tuple):
#     tuple_sum = 0
#     for i in user_tuple:
#         tuple_sum += i
#     return tuple_sum

#2)
# def big_number(user_tuple):
#     biger = 0 
#     for i in user_tuple:
#         try:
#             int(i)
#             if i > biger:
#                 biger = i
#         except:
#             continue
#     return biger

#3)
def how_many(user_tuple, user_value):
    count = 0
    for i in user_tuple:
        if i == user_value:
            count += 1
    return count

#4)
# def rever_tuple(user_tuple):
#     new_tuple = ()
#     for i in user_tuple[::-1]:
#         new_tuple = new_tuple + (i,)
#     return new_tuple

#5)
# def swap_tuple(user_tuple):
#     new_tuple = ()
#     starting=0
#     for i in user_tuple[::2]:
#             if len(user_tuple[starting:i+1]) == 2:  
#                 x,y = user_tuple[starting:i+1]
#                 new_tuple =new_tuple + (y,x)
#                 starting = i+1
#             else:
#                  new_tuple = new_tuple + (i,)    
#     return new_tuple            

#6)
# def min_and_max(user_tuple):
#     biger,smaler = user_tuple[0], user_tuple[0]
#     for i in user_tuple:
#         if i > biger:
#             biger = i
#         if i < smaler:
#             smaler = i
#     return biger,smaler

#7)
# def distance(x_tuple, y_tuple):   
#     x1, y1 = x_tuple
#     x2, y2 = y_tuple
#     the_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     return the_distance

#8)
def sort_tuple(user_tuple1, user_tuple2):
    new_tuple = user_tuple1 + user_tuple2
    return sorted(new_tuple)

t1 =1,3,5
t2 = 2,4,6
print(sort_tuple(t2 ,t1)) 

#9)
# def frequency_table(user_taple):
#     filt_taple = ()
#     new_tapule = ()
#     for i in user_taple:
#         if not i in filt_taple:
#             filt_taple += (i,)
#     for i in filt_taple:
#         if not i in new_tapule:
#             count = how_many(user_taple, i)
#             new_tapule += ((i,count),)
#     return new_tapule

#10)
def rotate_a_tuple(user_tuple,k):
    new_tuple = user_tuple[-k:] + user_tuple[:-k]
    return new_tuple
