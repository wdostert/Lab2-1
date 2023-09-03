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


#Exercise 3 function
def count_letters(input_string):
    letter_count = {}
    cleaned_string = input_string.replace(" ", "").lower()
    for char in cleaned_string:
        if char.isalpha() and char.islower():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count


#Exercise 4 Function
def get_valid_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


#Exercise 1 Test
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)

#Exercise 2 Test
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)

#Exercise 3 Test
user_input = input("Enter a string: ")
result = count_letters(user_input)
print(result)

#Exercise 4 Test
total_sum = 0
for i in range(5):
    valid_input = get_valid_int_input(f"Enter integer {i + 1}: ")
    total_sum += valid_input
print("Sum of the integers:", total_sum)