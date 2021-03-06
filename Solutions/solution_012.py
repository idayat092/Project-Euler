"""Problem 12: Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?"""

def triangle_numbers(number, limit):
    div_nums = 2
    num_range = range(2, (number // 2) + 1)
    if len(num_range) <= limit:
        return False
    for _ in num_range:
        if number % _ == 0:
            div_nums += 1
    return div_nums > limit

limit = 500

i, triangle, num = 1, 1, 0
while True:
    if triangle_numbers(triangle, limit):
        num = triangle
        break
    i += 1
    triangle += i

print(num)
