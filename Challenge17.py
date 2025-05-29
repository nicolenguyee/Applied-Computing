import random
 
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
answer4=("You lose!")
answer5=("You win!")
 
print("Welcome to the Magic 8 Ball game—use it to answer your questions...")
 
question = input("Ask me for any advice and I’ll help you out."
+ "Type in your question and then press Enter for an answer. ")
 
print("shaking.... \n" * 4)
 

choice = int(input("Enter a number (1–5): "))

if choice == 1:
    answer = answer1
elif choice == 2:
    answer = answer2
elif choice == 3:
    answer = answer3
elif choice == 4:
    answer = answer4
elif choice == 5:
    answer = answer5
else:
    answer = "Invalid choice"

print(answer)
