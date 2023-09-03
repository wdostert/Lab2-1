#Will Dostert

#Exercise 1 function
def get_unique_list(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


#Exercise 2 function
def get_combined_dict(dict1, dict2):
    combined_dict = {}
    for key in dict1:
        if key in dict2:
            combined_dict[key] = dict1[key] + dict2[key]
    return combined_dict



#Exercise 1 Test
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)



#Exercise 2 Test
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_co