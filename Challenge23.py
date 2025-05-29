import math

# Ask for inputs
pic = float(input("How many pictures do you have? "))
picbill = pic * 0.35

text = float(input("How many messages do you have? "))
textbill = text * 0.10

data = float(input("How much data (MB) do you use? "))

# Round up data to the nearest 500MB block
blocks = math.ceil(data / 500)
databill = blocks * 2.50

# Calculate total bill
bill = picbill + textbill + databill

# Display results
print("This is your total for the month: $", bill)

if bill > 10:
    print("A contract would be more suitable for your needs.")