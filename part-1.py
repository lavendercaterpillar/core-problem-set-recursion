# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    return factorial(n-1) * n


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2



# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True

    if parens[0] + parens[-1] != "()":
        return False
    return is_nested_parens(parens[1:-1])


# Extra challenge:
def is_nested_parens(parens):
    return helper(parens, 0, len(parens) - 1)

def helper(parens,left,right): # left and right are indices of first and last str char
    if left > right:
        return True

    if parens[left] != "(" or parens[right] != ")":
        return False
    return helper(parens, left+1 , right-1)