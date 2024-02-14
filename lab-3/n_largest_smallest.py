def find_n_largest_smallest(lst, n):
    lst.sort()
    smallest = lst[:n]
    largest = lst[-n:]
    return smallest, largest


my_list = [10, 20, 4, 45, 99, 30, 85, 22]
n = 3
smallest, largest = find_n_largest_smallest(my_list, n)
print(f"{n} smallest elements: {smallest}")
print(f"{n} largest elements: {largest}")
