# ============================================================
#       Topics: Numbers, Strings, Lists
# ============================================================


# ─────────────────────────────────────────
#  NUMBERS
# ─────────────────────────────────────────

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Returns the factorial of n (e.g. factorial(5) = 120)."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def fibonacci(n):
    """Returns a list of first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    for i in range(2, n):
        next_num = fibs[i - 1] + fibs[i - 2]
        fibs.append(next_num)
    return fibs


def is_even(n):
    """Returns True if n is even, otherwise False."""
    if n % 2 == 0:
        return True
    return False


def sum_of_digits(n):
    """Returns the sum of all digits of n (e.g. sum_of_digits(123) = 6)."""
    n = abs(n)           # handle negative numbers
    total = 0
    for digit in str(n):
        total = total + int(digit)
    return total


# ─────────────────────────────────────────
#  STRINGS
# ─────────────────────────────────────────

def reverse_string(s):
    """Returns the reverse of a string."""
    return s[::-1]


def is_palindrome(s):
    """Returns True if the string reads the same forwards and backwards."""
    s = s.lower()
    return s == s[::-1]


def count_vowels(s):
    """Returns the count of vowels (a, e, i, o, u) in the string."""
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count = count + 1
    return count


def remove_spaces(s):
    """Returns the string with all spaces removed."""
    result = ""
    for char in s:
        if char != " ":
            result = result + char
    return result


def capitalize_words(s):
    """Returns the string with the first letter of each word capitalized."""
    words = s.split()
    new_words = []
    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        new_words.append(new_word)
    return " ".join(new_words)


# ─────────────────────────────────────────
#  LISTS
# ─────────────────────────────────────────

def find_max(lst):
    """Returns the largest number in the list."""
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


def find_min(lst):
    """Returns the smallest number in the list."""
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val


def sum_list(lst):
    """Returns the sum of all elements in the list."""
    total = 0
    for num in lst:
        total = total + num
    return total


def remove_duplicates(lst):
    """Returns a new list with duplicate values removed."""
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


def second_largest(lst):
    """Returns the second largest number in the list."""
    unique = remove_duplicates(lst)
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]