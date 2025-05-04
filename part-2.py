# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array) == 0:
        return False

    if array[0] == query:
        return True
    return search(array[1:],query)



# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True

    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])



# digit_match
def digit_match(int1, int2):
    if int1 < 0 or int2 < 0:
        raise ValueError("Input must be a non-negative integer.")

    if int1 == 0 and int2 == 0:
        return 1

    match = 1 if (int1 % 10 == int2 % 10) else 0

    if int1 < 10 or int2 < 10:
        return match

    return match + digit_match(int1 // 10, int2 // 10)
