#input mode of transport
variant = input ("Do you walk to school or drive? ")
variant= variant.lower()
#if walk input the distance 
if variant == 'walk':
    distance= float (input ('how many kilometres do you walk to school? '))
    if distance<=5:
        print ('Good on you for excercising!')
    #if less more than 5 print 
    else: print ('I could never walk like you!')
#if drive input distance 
else:
    drivedistance= float(input ('how many kilometres do you drive to school? '))
    if drivedistance>5:
        print ('I would do the same too')
    #if less then 5 print 
    else: print ("better start walking to school!")

    


