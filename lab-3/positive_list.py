def find_positive_numbers(lst):
    positive_nums = [num for num in lst if num > 0]
    return positive_nums


my_list = [-10, 21, -4, 45, -66, 93, -11]
print(f"Original list: {my_list}")
print(f"Positive numbers: {find_positive_numbers(my_list)}")
