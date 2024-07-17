import random
winner = int(input("Enter your ticket number : "))
current = random.randint(1,10)
print("Winning ticket number is : ", current)
if current == winner:
    print(f"You ({winner}) win a FREE trip !!!")
else:
    print("Sorry, Try later")