# recursion.py
# IS211 Assignment 14 - Recursion


def fibonnaci(n):
    """Returns the nth Fibonnaci number using recursion."""
    # base cases: first two numbers in the sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Fn = Fn-1 + Fn-2
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    """Uses Euclid's algorithm to find the greatest common divisor of a and b."""
    # base case: when b is 0, a is the gcd
    if b == 0:
        return a
    else:
        # gcd(a, b) = gcd(b, remainder of a/b)
        return gcd(b, a % b)


def compareTo(s1, s2):
    """Recursively compares two strings.
    Returns negative if s1 < s2, 0 if equal, positive if s1 > s2."""
    # base case: both strings are empty, they're equal
    if len(s1) == 0 and len(s2) == 0:
        return 0
    # if s1 ran out first, it's the smaller string
    if len(s1) == 0:
        return -1
    # if s2 ran out first, s1 is the bigger string
    if len(s2) == 0:
        return 1

    # compare the first character of each string
    if ord(s1[0]) < ord(s2[0]):
        return -1
    elif ord(s1[0]) > ord(s2[0]):
        return 1
    else:
        # first chars are the same, compare the rest of the strings
        return compareTo(s1[1:], s2[1:])


# quick tests
if __name__ == '__main__':
    # test fibonnaci
    print("Fibonnaci sequence (first 10):")
    for i in range(10):
        print(f"  F({i}) = {fibonnaci(i)}")

    # test gcd
    print("\nGCD tests:")
    print(f"  gcd(48, 18) = {gcd(48, 18)}")
    print(f"  gcd(100, 75) = {gcd(100, 75)}")

    # test compareTo
    print("\ncompareTo tests:")
    print(f"  compareTo('apple', 'banana') = {compareTo('apple', 'banana')}")
    print(f"  compareTo('hello', 'hello') = {compareTo('hello', 'hello')}")
    print(f"  compareTo('zebra', 'apple') = {compareTo('zebra', 'apple')}")
