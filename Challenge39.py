myFile = open("numbers.txt", "wt")

for i in range(6):
    number = input("Enter a number: ")
    myFile.write(number + "\n")

myFile.close()