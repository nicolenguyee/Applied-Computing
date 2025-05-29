happy=int(input("Rate how happy do you feel on a scale between 1 and 10? "))
if happy<3:
    print ("Hope you cheer up!")
elif happy<=4 or happy>=7:
    print ("Lets get you happier!")
else:
    print ("Lets keep it that way!")