#Write a Python program to reverse a number and also find the sum of digits of the number.Prompt the user for input.

def reverse_and_sum(num):
    reversed_num = 0
    sum_of_digits = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        sum_of_digits += digit
        num //= 10
    return reversed_num,sum_of_digits



number = int(input("Enter a positive integer: "))
reversed_number, sum_of_digit = reverse_and_sum(number)
print(f"origial number: {number}")
print(f"reversed number: {reversed_number}")
print(f"sum of digit: {sum_of_digit}")