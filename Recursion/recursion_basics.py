'''Factorial Example.

5! = 120
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!

4! = 24
4! = 4 * 3 * 2 * 1
4! = 4 * 3!

3! = 6
3! = 3 * 2 * 1
3! = 3 * 2!

2! = 2
2! = 2 * 1
2! = 2 * 1!

base case
1! = 1
1! = 1
'''


def factorial(n):
    '''Find the value of 'n' factorial non-recursively.'''
    if n < 0:
        print("This function is only designed for non-negative integers.")
        quit(-1)

    result = 1
    while n > 1:
        result *= n
        n -= 1

    return result


def recursive_factorial(n: int) -> int:
    '''Find the value of 'n' factorial recursively.'''
    # 5! = 5 * 4!
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        print("This function is only designed for non-negative integers.")
        quit(-1)
    return n * recursive_factorial(n - 1)


# test that things work.
# print(factorial(3))
in_value = int(input('Please enter an integer value: '))
# print(f"factorial({in_value}): {factorial(in_value)}")
print(f"recursive_factorial({in_value}): {recursive_factorial(in_value)}")
