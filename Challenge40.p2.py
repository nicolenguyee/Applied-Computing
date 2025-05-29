myFile = open("people.txt", "rt")
data = []

# Read the data and remove newlines
for line in myFile:
    data.append(line.strip("\n"))

myFile.close()

# Go through every 3 items (name, weight, height)
for i in range(0, len(data), 3):
    name = data[i]
    weight = float(data[i + 1])
    height = float(data[i + 2])
    print(name, "weighs", weight, "kg and is", height, "m tall")