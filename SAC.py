# This opens a file called COMM_SAC.txt for writing ("wt" means write text)
myFile = open("COMM_SAC.txt", "wt")

# Ask how many students are in the class
students = int(input("Enter the total number of students in the class: "))
# If they type less than 1, keep asking
while students < 1:
    print("Number of students must be at least 1")
    students = int(input("Enter the total number of students in the class: "))

# Ask how many class periods were held this week
periods = int(input("Enter total number of periods of the class held in the week (between 1 and 5):  "))
# If it's not between 1 and 5, keep asking
while periods < 1 or periods > 5:
    print("Periods must be between 1 and 5")
    periods = int(input("Enter total number of periods of the class held in the week (between 1 and 5):  "))

# Make a list to store each student's data (name, how many P, and percentage)
studentdata = []

# Loop through each student
for i in range(students):
    name = input(f"\nEnter name for student {i+1}: ")  # Ask for the student's name
    totalpresent = 0  # Start counting how many times they were present

    # Loop through each period
    for j in range(periods):
        answer = input(f"Enter attendance for {name} (P/A) for period {j+1} ").upper()
        # Keep asking until the answer is P or A
        while answer not in ("P", "A"):
            print("Answer only using p or a")
            answer = input(f"Enter attendance for {name} (P/A) for period {j+1} ").upper()

        # If they were present, add 1 to their count
        if answer == "P":
            totalpresent += 1

    # Calculate their attendance percentage
    percentage = (totalpresent / periods) * 100
    # Add their data to the list
    studentdata.append((name, totalpresent, percentage))

# Print the attendance report heading
print("\nAttendance Report: ")
myFile.write("\nAttendance Report:\n")

# Go through each student's saved data
for name, totalpresent, percentage in studentdata:
    # Print and write their name, presents, and percentage
    myFile.write(f"{name}: {totalpresent} periods present ({int(percentage)}%)\n")
    print(f"{name}: {totalpresent} periods present ({int(percentage)}%)")

    # If their attendance is below 75%, print and write a warning
    if percentage < 75:
        myFile.write("- Warning: Low attendance\n")
        warning = "- Warning: Low attendance"
        print(warning)

# Close the file so everything saves properly
myFile.close()