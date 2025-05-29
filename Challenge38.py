myFile = open ("example.txt", "rt")
myList= []  # define an empty list in which to store the information
for line in myFile:
    line = line.strip("\n")
    myList.append(line) 
print (myList)
myFile.close()
