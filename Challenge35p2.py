monday = ["French", "English", "PSHE", "ICT", "Maths"]
Monday:  monday.append ("Geography")

print("The list monday contains the following information:")
print(monday[2])  # prints the subject at position 2

print("We can also just ask to print out the list. So here is monday:")
print(monday)  # prints the entire list

print("We can also print them out one at a time")
for i in monday:
    print(i)  # prints each item one by one