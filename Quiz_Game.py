input("Welcome to the Quiz!!")

play = input("Did you want play Quiz?(yes to start) ")

if play.lower() != "yes":
    quit()

print("Ok Let's Play..")
score = 0

answer = input("What does CPU stand for ? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect..")
answer = input("What does GPU stand for ? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect..")
answer = input("What does FPS stand for ? ")

if answer.lower() == "frames per seconds":
    print("Correct!")
    score += 1
else:
    print("Incorrect..")
answer = input("What does RAM stand for ? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect..")
answer = input("What does ROM stand for ? ")

if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect..")

print("Your Score is " + str(score) + ".")
print("Your got " + str((score / 5) * 100) + "%.")