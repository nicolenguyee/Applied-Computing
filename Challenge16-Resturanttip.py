people= int(input("How many people were dining today? "))
tip= int(input("What would you like to tip today? "))
bill= int(input("What was the total bill? "))

total=bill/people 
share=total*(1+tip/100) 
print ("Each person should pay ",share, "dollars ")

distance= float(input("how far are you travelling to your destination? in miles "))
fare= distance*0.45
print ("The taxi fare costs ",fare,"dollars ")

overallcost=share+fare
print ("For the whole evening, you have spent", overallcost, "dollars")

