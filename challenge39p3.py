myFile = open("numbers.txt", "at")

for i in range(4):
    new_number = input("Enter another number: ")
    myFile.write(new_number + "\n")

myFile.close()