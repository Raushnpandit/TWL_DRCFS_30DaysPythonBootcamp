# Quiz app 

question = ("How many planets in our solar system?",
            "What is the name of the moon of mars?"
            "What is the distance between Earth and Moon?"
            "Which planet is most hottest planet?"
            "What is the name of our Galaxy?")

options= (("a.8", "b.5", "c.9", "d.7"),
           ("a.Phobos", "b.Demos", "c.Both", "d.None"),
           ("a.384400km", "b.484200km", "c.854200km", "d.585400km"),
           ("a.Mars", "b.Mercury", "c.Earth", "d.Venus"),
           ("a.Andromeda", "b.Milky way", "c.Sagrigattus", "d.None"))

answers = ("a", "c", "a", "d", "b")
guess = []
score = 0
question_num = 0

for question in question:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (a, b, c, d): ").lower()
    guess.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guess:
    print(guess, end=" ")
print()

score = int(score / len(question) * 100)
print(f"Your score is: {score}%")

    