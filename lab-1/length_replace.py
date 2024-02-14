def find_length(word):
    return len(word)


def replace(word, old, new):
    return word.replace(old, new)


str = "Computer Science"
print(f"The length of the string is: {find_length(str)}")
old = "Science"
new = "Electronics"
print(f"The new string is: {replace(str, old, new)}")
