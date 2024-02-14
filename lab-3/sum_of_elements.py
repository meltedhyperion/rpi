def cumulative_sum(lst):
    cum_sum = [sum(lst[: i + 1]) for i in range(len(lst))]
    return cum_sum


my_list = [10, 20, 30, 40, 50]
print(f"Original list: {my_list}")
print(f"Cumulative sum: {cumulative_sum(my_list)}")
