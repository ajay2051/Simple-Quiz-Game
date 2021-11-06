print("Welcome To Quiz Game")

play = input("Do you want to play? ")

if play.lower() != 'yes':
    quit()

print('Lets play')

score = 0

answer = input("What is the capital of Nepal? ")
if answer.lower() == 'kathmandu':
    print("Correct")
    score += 1
else:
    print("Wrong answer")

answer = input("How many districts are there in Nepal? ")
if answer.lower() == '77':
    print("Correct")
    score += 1
else:
    print("Wrong answer")


answer = input("What is the capital of Lumbini Pradesh? ")
if answer.lower() == 'nepalgunj':
    print("Correct")
    score += 1
else:
    print("Wrong answer")


answer = input("How many proviences are there in Nepal? ")
if answer.lower() == '7':
    print("Correct")
    score += 1
else:
    print("Wrong answer")

print(f'You got {score} questions correct')


