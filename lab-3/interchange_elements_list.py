def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
print(f"Updated List: {swap_first_last(my_list)}")
