import random



#Creating ART to show when user gueeses
art=('''
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
 |G|u|e|s|s| |t|h|e| |n|u|m|b|e|r| 
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
''')
win=('''
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
 THANKYOU. YOU WIN.
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
''')
loss=('''
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
 You LOSE.Try Again
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+ 
''')


#Function to calculate the win

def calculate(numbers):
    if difficulty=='easy':
        count=10
    elif difficulty=='hard':
        count=5

    for i in range(count):
        print(f"You have {count} Guess left")
        inp=int(input("Enter a Guss: "))

        if inp>numbers:
            print("Guessed number is higher!")
            count-=1
        elif inp<numbers:
            print("Guesses number is lower!")
            count -=1
        else:
            print("You found the number.Great!!")
            print(win)
            break

    if count==0:
        print(loss)

        choice=input("Do you want to play again?: (Y/N)").lower()
        if choice!='y':
            playagain=False
            exit()


#Program starting with while
playagain=True
while True:
    print("Welcome to guessing game")
    print(art)
    difficulty=input("Select a difficulty mode  easy or hard : ")
    if difficulty =='easy' or difficulty=='hard':
        print("I Guessed a number between 1 and 100\n")
        gussed_number=random.randint(1,100)
        
        calculate(gussed_number)
    else:
        print("Invalid difficulty chosen.Try again")
