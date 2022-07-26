#Created by Aswin ks
#This program check the follower count of celebeties and provide a high score.It uses dictionaries and lists


from logo import  logo,vs
from data import data
import random
import os,time

#for fetching 2 records

def get_random_account():
    return (random.choice(data))

def calculates(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a" #Return True if guess ==a
    else:
        return guess=="b"
def format_data(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return (f"{name}, a {description}, from {country}")




#main function
def game():

    account_a=get_random_account()
    account_b=get_random_account()
    continue_game=True
    score=0

    while continue_game==True:
        account_a=account_b
        continue_game=True
        account_b=get_random_account()
        while account_b==account_a:
            account_b=get_random_account()
        os.system('cls')
        print(logo)
        print(f"compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        guess=input("Who has more followers, A or B ? : ").lower()

        a_follower_count=account_a['follower_count']
        b_follower_count=account_b['follower_count']

        corrects=calculates(guess,a_follower_count,b_follower_count)

        if corrects:
            score+=1
            print(f"Correct!. Your score is {score}")
            time.sleep(1)
        else:
            print(f"Wrong. Your Final score is {score}")
            continue_game=False













game()