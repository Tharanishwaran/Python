def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = int(n) / 10
    return reversed_num

# Test the function
num = 12
reversed_num = reverse_number(num)
print(reversed_num)

