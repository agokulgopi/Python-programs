# Write a Python program to count number of even numbers
#  and odd numbers in a given set of n numbers.

# def count_even_odd(numbers):
#     even_count = 0
#     odd_count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return even_count,odd_count
#
# n = int(input("Enter the Number of elements: "))
# numbers = []
# for i in range(n):
#     num = int(input("Enter the number {}: ".format(i+1)))
#     numbers.append(num)
# even_count, odd_count = count_even_odd(numbers)
#
# print("Even Numbers: ",even_count)
# print("Odd Numbers: ",odd_count)

n = int(input("Enter the Number of elements: "))
even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter the number {}: ".format(i+1)))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")