import random
 
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
 
print("Welcome to the Magic 8 Ball game—use it to "+
"answer your questions...")
 
choice = input("Ask me for any advice and I’ll help you out."+
"Type in your question and then press Enter for an answer. ")
 
print("shaking.... \n" * 4)
 

if choice == 1:
	answer=answer1
elif choice == 2:
	answer=answer2
else:
	answer=answer3

print(answer)
