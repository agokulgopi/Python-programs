# Write a python program to generate the following type of pattern for the given N rows .
# 1
# 1 2
# 1 2 3
# 1 2 3 4

def generate_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

while True:
    try:
        n = int(input("Enter the number of rows: "))
        if n <= 0:
            raise ValueError("Please enter the positive number of rows.")
        break
    except ValueError as e:
            print(e)
            print("Please enter a valid positive integer.")

print("Generated pattern:")
generate_pattern(n)