heightandweight = ["James", 73, 1.82, "Peter", 78, 1.80, "Beth", 65, 1.53, "Mags", 66, 1.50, "Joy", 62, 1.34]

myFile = open("people.txt", "wt")

# Write each value as a string, one per line
for item in heightandweight:
    myFile.write(str(item) + "\n")

myFile.close()