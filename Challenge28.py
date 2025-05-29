sentence = str(input("Type a setence. How many letter 'e''s are there in it? "))
numberE = 0
numberA = 0
numberI = 0
numberO = 0
numberU = 0


for letter in sentence:
    if letter =="a":
        numberA +=1
        
for letter in sentence:
    if letter =="e":
        numberE +=1
        
for letter in sentence:
    if letter =="i":
        numberI +=1
        
for letter in sentence:
    if letter =="o":
        numberO +=1

for letter in sentence:
    if letter =="u":
        numberU +=1
print ("The number of vowel's in the sentence is:", numberE+numberA+numberI+numberO+numberU)
