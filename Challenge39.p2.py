myFile = open("numbers.txt", "rt")
numbers = []

for line in myFile:
    line = line.strip("\n")
    numbers.append(int(line))

myFile.close()

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)