
print("This is a simple Quiz Game")

answer = float(input("1. What is 1 + 1: "))
if answer == 2:
    print("You are correct")
elif answer != 2:
    print("You are not correct")

answer = input("2. What is the combination color of yellow and blue?: ")
if answer.lower() == 'green':
    print("You are correct")
elif answer.lower() != 'green':
    print("You are not correct")

answer = (input("3. What is the number next to 7?: "))
if answer == '8':
    print("You are correct")
elif answer != '8':
    print("You are not correct")

answer = int(input("4. How many days are there in a week?: "))
if answer == 7:
    print("You are correct")
elif answer != 7:
    print("You are not correct")

answer = input("5. What are is the color of a sun?: ")
if answer == 'yellow':
    print("You are correct")
elif answer != 'yellow':
    print("You are not correct")

options = ['You are correct', 'You are not correct']

number_correct = options.count("You are correct")

print("Congrats, You got ", number_correct, "!")
