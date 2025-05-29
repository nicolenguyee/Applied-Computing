#Prompting user to enter name and age
name=str(input("What is your name? "))
age=float(input("How old are you? "))
days=(365/age)
hours=(365/age)*24
minutes=(hours/60)
print (name,"You have been alive for", days, "days ")
print (name,"You have been alive for", hours, "hours ")
print (name,"You have been alive for", minutes, "minutes ")
