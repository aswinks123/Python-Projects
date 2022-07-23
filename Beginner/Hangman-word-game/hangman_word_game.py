#Handman word guessing game
#Created by Aswin ks

import random
from hangman_game_graphic import stages
from hangman_wordlist import word_list

print("Welcome to hangman Game.Objective is to find the correct word.You have only 6 lives in total")




#Choosing a random word list from hangman_wordlist file's wordlist list
instance=random.choice(word_list).lower()
l=len(instance)
output=[]
lives=6

#-------------------------------------#For finding number of _ required to print
for i in range(len(instance)):
    output+= "_"


print(output)


end_of_game=False



#--------------------------------For looping until lives end
while not end_of_game:

    guess=input("Guss a word: ").lower()
   
    if guess in output:
        print(f"You already gussed {guess}")



    for position in range(l):
        letter=instance[position]
        if letter==guess:
            output[position]=letter
        else:
            pass


    if guess not in instance:
        print("Gusses word not in list! .You lose a life")
        lives-=1

        if lives==0:
            end_of_game=True
            print("You Lose!. Try Again")

    print(output)
    if "_" not in output:
        end_of_game=True
        print("YOU WIN")

    print(stages[lives])  #Printing image of hangman as per the life count
