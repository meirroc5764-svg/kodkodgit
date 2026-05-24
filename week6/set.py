#1
def remove_duplicate(user_list):
    return set(user_list)

#2
def count_elements(user_list):
    count = 0
    for i in set(user_list):
        count += 1
    return count

#3)
def common_elements(user_list1, user_list2):
    new_list = [set(user_list1) & set(user_list2)]
    return new_list
#4)
def not_comon(user_list1, user_list2):
       new_list = [set(user_list1) ^ set(user_list2)]
       return new_list 

#5)
def is_in(user_list1, user_list2):
    for i in user_list1:
        if not i in user_list2:
            return False
    return True 
#6)
def unique_characters(user_text):
    return len(user_text) == len(set(user_text))   

#7)
def first_repeated(user_list):
    for index,value in enumerate(user_list):
        if value in user_list[index + 1:]:
            return value
    return None

#8)
def distinct_words(user_text):
    return len(set(user_text.split()))

#9)
def pair_sum_exists(user_list, target):

    for i in set(user_list):
        num = target - i
        if num in user_list:
            return True
    return False

#10)
def symmetric_difference(user_list1, user_list2):
    new_list =[] 
    for number in user_list1:
        if (number in user_list1) and (number in user_list2):
            user_list2.remove(number)
            continue
        else:
            new_list.append(number)
    for number in user_list2:
        new_list.append(number)        
    return new_list           