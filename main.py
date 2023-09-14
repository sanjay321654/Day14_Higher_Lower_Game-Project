from game_data import data
from art import logo
from art import vs
import random
from replit import clear


score = 0
#account_B = random.choice(data)
game_continue = True
while game_continue:
    print(logo)
    def compare_Data():
        
        a_account = random.choice(data)
        return a_account
          
        B_account = random.choice(data)
        return B_account
        if a_account == B_account:
            B_account = random.choice(data)
            return B_account

    def checking():  
        A_compare = compare_Data()
        B_compare = compare_Data()
        
        print(f"compare A: {A_compare['name']}, {A_compare['description']}, {A_compare['country']}")
        print(vs)
        print(f"Compare B: {B_compare['name']}, {B_compare['description']}, {B_compare['country']}")
        user = input("who has more followers. Type A or B.").lower()
        a_follower = A_compare["follower_count"]
        b_follower = B_compare["follower_count"]
        clear()
        if a_follower > b_follower:
            return user == "a"
        else:
            return user == "b"
    correct = checking()

    
    if correct:
        score+=1
        print(f"You are right.your current score is {score}")
    else:
        game_continue = False
        print(f"sorry you are wrong.your final score is {score}")
        
