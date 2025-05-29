# Set your name
my_name = "Nicole" or "nicole"

# Loop until the correct name is entered
while True:
    name = input("What is your first name? ")
    if name == my_name:
        print("Welcome!")
        break
    else:
        print("Sorry, that's not the name I'm looking for. Please try again.")