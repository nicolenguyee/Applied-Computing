# Ask the user to enter their own number
number = int(input("Enter a number to display its times table (1 to 12): "))

# Print the times table
print(f"\n{number} Times Table")
print("-" * 25)

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")