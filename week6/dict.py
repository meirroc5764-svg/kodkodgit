#1)
def dict_sum(user_dict):
    the_sum = 0
    for values in user_dict.values():
        try:   
            the_sum += values
        except TypeError:
            continue    
    return the_sum

#2)
def bigger(user_dict):
    big_value = 0
    big_key = ""
    for key,value in user_dict.items():
        if value > big_value:
            big_value = value
            big_key = key
    return big_key, big_value

 #3)
def how_many(user_word):
    leter_dict= {}
    for i in user_word:
        if not i in leter_dict:
            leter_dict[i] = 1
        else:
            leter_dict[i] += 1
    return leter_dict            

#4)
def swaps(user_dict):
    new_dict = {}
    for key,value in user_dict.items():
        new_dict[value] = key
    return new_dict
    
#5)
def merge(user_dict1, user_dict2):
    return user_dict1 | user_dict2

#6)
def filter_value(user_dict, num):
    new_dict ={}
    for key,value in user_dict.items():
        if value > num:
            new_dict[key] = value
    return new_dict        
            

#7)
def first_lettter(user_list):
    letter_dict = {}
    for word in user_list:
        if not word[0] in letter_dict:
            letter_dict[word[0]] = [word]
        else:
            letter_dict[word[0]].append(word)
    return letter_dict
            
#8)
def frequency(user_text):
    leter_dict= {}
    for i in user_text.split(" "):
        if not i in leter_dict:
            leter_dict[i] = 1
        else:
            leter_dict[i] += 1
    return leter_dict

#9)
def common_keys(first_dict, sechond_dict):
    comm_keys_list = []
    for key in first_dict.keys():
        if key in sechond_dict:
            comm_keys_list.append(key)
    return comm_keys_list

#10)
def frequent_value(user_dict):
    new_dict = {}
    the_bigger_value = 0
    for value in user_dict.values():
        if not value in new_dict:
            new_dict[value] = 1
        else:
            new_dict[value] += 1
    the_big_num = 0
    for key,value in new_dict.items():
        if value > the_big_num:
            the_big_num = value
            the_bigger_value = key

    return the_bigger_value           
