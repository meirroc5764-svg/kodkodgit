# 1)
def list_sum(numbers):
    all_sum = 0
    for number in numbers:
        all_sum += number
    return all_sum

# 2)
def max_num(list_numbers):
    big_value = 0
    for number in list_numbers:
        if number > big_value:
            big_value = number
    return big_value

# 3)
def how_many(list_value, value):
    count = 0
    for i in list_value:
        if i == value:
            count += 1
    return count

# 4)
def rever_list(user_list):
    new_list = []
    for i in user_list:
        new_list.insert(0,i)
    return new_list

# 5)
def Remove_duplicates(user_list):
    new_list = []
    for i in user_list:
        if i in new_list:
            continue
        new_list.append(i)
    return new_list

# 6)
def second_big(user_list):
    big_num = max(user_list)
    new_list = [x for x in user_list if x != big_num]
    if new_list == []:
        return None
    return max(new_list)

# 7)
def merge_two_list(user_list_one, sechond_user_list):
    user_list_one.extend(sechond_user_list)
    new_list = sorted(user_list_one)
    return new_list

# 8)
def rotate_a_list(user_list,k):
    if k > len(user_list):
        k = k % len(user_list)
    return user_list[-k:] + user_list[:-k]