print("Quiz Time!")
score = 0

hpmovies = input("1. How many Harry Potter movies are there:")

hpmovies = float(hpmovies)

if hpmovies == 8:
    print("Correct!")
    score = score + 1

if hpmovies != 8:
    print("Incorrect!")
   

mathq = input("2. What is the answer too 3(4+5):")

mathq = float(mathq)

if mathq == 27:
    print("Correct!")
    score = score + 1

if mathq != 27:
    print("Wrong!")
    

character = input("3. Who is the best Character from RE:ZERO:\n A) Felix\n B) Emeilia\n C) REM\n D) Ram\n Answer:")

if character.lower() == "c":
    print("Correct!")
    score = score + 1

if character.lower() != "c":
    print("Incorrect!")


potus = input("4. Who won the 2016 US Presidential Election:")

if potus.lower() == "donald trump":
    print("Correct!")
    score = score + 1

if potus.lower() != "donald trump":
    print("Wrong! Wrong! Wrong!")
    

earth = input("5. If the surface area of the earth is 510.1 million kilometers squared, and a cat jumps on a fence then lands on the ground after a dog barks at it. What is the surface area of the earth? (without units):")

earth = float(earth)

if earth == 510.1:
    print("nice one! you got it!")
    score = score + 1

if earth != 510.1:
    print("wrong! it's actually really easy, you could probably just google it..")
    
print("gg ez")
print("your final score is", score, "out of 5")

    






