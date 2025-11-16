# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 1
while row <= size:
    for i in range(size):
        print("*", end="")
    print()  # move to next line
    row += 1