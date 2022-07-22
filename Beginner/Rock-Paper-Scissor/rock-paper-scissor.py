#Created By: Aswin ks
#More @ https://github.com/aswinks1995

import random  #for using random function

#Defining the ASCII image for rock paper and scissor

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


game_image=[rock,paper,scissor]
uwin=0  #For win,loss,draw counter
cwin=0
cdraw=0

while True: #For playing the game continuously until loop breaks

    try: #To avoid user from providing non intiger values in user_choice
        print(f"Current score : WIN : {uwin}  LOSE : {cwin}  DRAW : {cdraw}")
        user_choice=int(input("Choose one: 0 for Rock, 1 for Paper, 2 for scissors '99' to Exit\n"))

    except:
        print("invalid") #if user provide non intiger it will print this
    else:  #if all satisfy move down


        if user_choice==99:  #for quitting the game
            exit()
        else:

            if user_choice>2 or user_choice<0:
                print("Invalid choice")
                continue
            else:
                print("You choose: ")
                print(game_image[user_choice]) #showing the hand ASCII icons
                computer_choice=random.randint(0,2)
                print("Computer choose: ")
                print(game_image[computer_choice]) #showing the hand ASCII icons


            if user_choice==computer_choice:
                print("Its a DRAW!")
                cdraw+=1  #counter


            elif user_choice==0:  #rock
                if computer_choice==1: #paper
                    print("You Lose")
                    cwin+=1  #counter
                else:
                    print("You Win")#scissor
                    uwin+=1  #counter

            elif user_choice==1: #paper
                if  computer_choice==0: #rock
                    print("You win")
                    uwin += 1  #counter
                else:
                    print("You lose")#scissor
                    cwin+=1  #counter

            elif user_choice==2: #scissor
                if  computer_choice==0: #rock
                    print("You Lose")
                    cwin += 1  #counter
                else:
                    print("You Win") #Paper
                    uwin += 1  #counter




#Thankyou