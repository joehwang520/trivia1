#Quiz v1.6
#Number of end user tests: 1
print("How much did you pay attention in school? Let's find out! ")
print(f"\n--Please capitalize all of your answers unless instructed otherwise. Otherwise they will NOT count!--\n")

score = 0

#Question 1
question1 = "1. How many planets are there in the solar system? (Yes, obviously not counting Pluto.) "
answer1 = input(question1)
answer1 = int(answer1)

if answer1 == 8:
    print(f"Correct!\n")
    score += 1
else:
    print(f"Sorry, that is incorrect.\n")


#Question 2
question2 = "2. Which U.S. state was the last to be admitted to the Union? "
answer2 = input(question2)

if answer2 == "Hawaii" or answer2 == "HI":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 3
question3 = "3. The three states of matter are solid, liquid, and _____. "
answer3 = input(question3)

if answer3 == "gas" or answer3 == "Gas":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 4
question4 = "4. What element in the periodic table does 'Pb' represent? "
answer4 = input(question4)

if answer4 == "lead" or answer4 == "Lead":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 5
question5 = "5. How many continents are there in the world? "
answer5 = input(question5)
answer5 = int(answer5)

if answer5 == 7:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 6
question6 = "6. How many oceans are there in the world? "
answer6 = input(question6)
answer6 = int(answer6)

if answer6 == 4:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 7
question7 = "7. 'A squared plus B squared equals C squared' refers to what theorem? "
answer7 = input(question7)

if answer7 == "Pythagorean" or answer7 == "pythagorean":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 8
question8 = "8. Abraham Lincoln was the __th president. "
answer8 = input(question8)
answer8 = int(answer8)

if answer8 == 16:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 9
question9 = "9. What does the 'D.C.' in 'Washington D.C.' stand for? "
answer9 = input(question9)

if answer9 == "District of Columbia":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 10
question10 = "10. What state is Mt. Rushmore in? "
answer10 = input(question10)


if answer10 == "South Dakota" or answer10 == "SD":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 12
question11 = "11. Rosa Parks refused to give up her seat to a white person in what vehicle? "
answer11 = input(question11)


if answer11 == "bus" or answer11 == "Bus":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 12
question12 = "12. A leap year occurs every __ years. "
answer12 = input(question12)
answer12 = int(answer12)


if answer12 == 4:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")


#Question 13
question13 = "13. A prime number is a number that is only divisible by __ and itself. "
answer13 = input(question13)
answer13 = int(answer13)

if answer13 == 1:
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 14
question14 = "14. True or False? Texas is the biggest state in the U.S. "
answer14 = input(question14)

if answer14 == "False" or answer14 == "F":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")



#Question 15
question15 = "15. True or False? Mercury is the hottest planet in the solar system. "
answer15 = input(question15)


if answer15 == "False" or answer15 == "F":
    print("Correct!\n")
    score += 1
else:
    print("Sorry, that is incorrect.\n")




percent = int((score/15)*100)

print(f"You answered {score} question(s) correctly! Your scored {percent}%!\n")
