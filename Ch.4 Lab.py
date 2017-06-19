import random

print("\nWelcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing your down!")
print("Survive your desert trek and outrun the natives.")

done = False

kilometers_travelled = 0
natives_travelled = -20
thirst = 0
camel_tiredness = 0
canteen_drinks = 3

while not done:
    natives_distance = (kilometers_travelled - natives_travelled)
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    user_choice = input("Your choice? ")
    print()
    if user_choice.upper() == "Q":
        done = True
        print("Game over.")
        print("Thank you for playing!")
    elif user_choice.upper() == "E":
        print("Kilometers travelled:", kilometers_travelled)
        print("Drinks in canteen:", canteen_drinks)
        print("The natives are", (kilometers_travelled - natives_travelled), "kilometers behind you.")
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("Your camel is rested.")
        natives_travelled += random.randrange(7,15)
    elif user_choice.upper() == "C":
        kilometers_travelled += random.randrange(10,21)
        print("You have travelled", kilometers_travelled, "kilometers.")
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_travelled += random.randrange(7,15)
        if random.randrange(1,21) == 1:
        	print("You found an oasis!")
        	print("Your canteen is refilled, your thirst is quenched, and your camel is rested.")
        	camel_tiredness = 0
        	thirst = 0
        	canteen_drinks = 3
    elif user_choice.upper() == "B":
        kilometers_travelled += random.randrange(5,13)
        print("You have travelled", kilometers_travelled, "kilometers.")
        thirst += 1
        camel_tiredness += 1
        natives_travelled += random.randrange(7,15)
        if random.randrange(1,21) == 1:
        	print("You found an oasis!")
        	print("Your canteen is refilled, your thirst is quenched, and your camel is rested.")
        	camel_tiredness = 0
        	thirst = 0
        	canteen_drinks = 3
    elif user_choice.upper() == "A":
        if canteen_drinks == 0:
            print("Your canteen is empty.")
        else:
            thirst = 0
            canteen_drinks -= 1
            print("You drink from your canteen.")
    if kilometers_travelled >= 200:
    	done = True
    	print()
    	print("You made it across the desert.")
    	print("You won!")
    if natives_distance <= 0:
    	done = True
    	print()
    	print("The natives caught you!")
    	print("Game over.")
    if natives_distance <= 15 and natives_distance > 0:
    	print("The natives are getting close!")
    if thirst > 6:
    	done = True
    	print()
    	print("You died of thirst.")
    	print("Game over.")
    if thirst > 4 and thirst < 7:
        print("You are thirsty.")
    if camel_tiredness > 8:
    	done = True
    	print()
    	print("Your camel is dead.")
    	print("Game over.")
    if camel_tiredness > 5 and camel_tiredness < 9:
    	print("Your camel is getting tired.")