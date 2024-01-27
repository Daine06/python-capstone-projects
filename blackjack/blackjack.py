############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
import os
import time
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list_cards):
    random_cards = random.choice(list_cards)
    return random_cards

def calculate_score(cards):
    sum_cards = sum(cards)
    if sum_cards > 21 and 11 in cards:
        num_index = cards.index(11)
        cards[num_index] = 1
        sum_cards += sum(cards)
        return sum_cards
    else:
        return sum_cards

def compare_score(user_card_score, computer_card_score):
    global player_wins, computer_wins
    
    if user_card_score > computer_card_score:
        if user_card_score > 21:
            print("You have exceeded.")
            if computer_card_score > 21:
                print("Both exceeded. You both lost.")
            elif computer_card_score == 21:
                computer_wins += 1
                print(f"Computer has Blackjack. You lost. Computer score is {computer_wins}")
            elif computer_card_score < 21:
                computer_wins += 1
                print(f"Computer won! Computer score is: {computer_wins}")
        elif user_card_score == 21:
            player_wins += 1
            print(f"You have blackjack. You win! Your score is: {player_wins}")
        elif user_card_score <= 21:
            player_wins += 1
            print(f"You are highest. You won! Your score is: {player_wins}")
            
    elif user_card_score == computer_card_score:
        if user_card_score > 21 and computer_card_score > 21:
            print("You both exceeded 21. You both lost!") 
        elif user_card_score == 21 and computer_card_score == 21:
            print("Both are blackjack. It's a draw. No points for the both of you.")
        elif user_card_score < 21 and computer_card_score < 21:
            print("It's a draw. No points for the both of you.")
        
    elif user_card_score < computer_card_score:
        if computer_card_score > 21:
            if user_card_score <= 21:
                player_wins += 1
                print(f"Computer exceeded 21. You win! Your score is: {player_wins}")  
            elif user_card_score > 21:
                print("Both exceeded 21. Both lost.") 
        elif computer_card_score == 21:
            computer_wins += 1
            print(f"Computer is Blackjack. You lose. Computer score is: {computer_wins}")
        elif computer_card_score < 21:
            computer_wins += 1
            print(f"Computer is highest. Computer wins! Computer score is: {computer_wins}") 
        
computer_wins = 0
player_wins = 0

user_cards = []
computer_cards = []

print(logo)
print("Welcome to the game Blackjack!")
decision = input("Enter 1 to start the game and 2 to exit. ")

if decision == "1":
    os.system("cls")
    print("Please wait while we're setting up the table for you and your opponent")
    time.sleep(3)
    print("Dealer is now distributing the cards...")
    time.sleep(3)
    
    game_state = True
    while game_state == True:
        for i in range(2):
            user_cards.append(deal_card(cards))
            computer_cards.append(deal_card(cards))
                
        print(f"This is your hand: {user_cards}")
        print(f"This is the computer's hand: {computer_cards[0]}, x")
        calculate_score(user_cards)
        
        player_turn = True
        while player_turn == True:
            if calculate_score(user_cards) <= 21:
                draw_choice = input("Do you want to draw another card? Y for yes or N for no: ").capitalize().strip()    
                if draw_choice == 'Y':
                    func_deal_card = deal_card(cards)
                    user_cards.append(func_deal_card)
                    calculate_score(user_cards)
                    print(f"This is your hand: {user_cards}")
                elif draw_choice == 'N':
                    os.system("cls")
                    print(f"This is your hand: {user_cards}")
                    time.sleep(1)
                    print("Computer's turn.")
                    time.sleep(3)
                    player_turn = False
                else:
                    "Answer Invalid."
            else:
                time.sleep(3)
                player_turn = False      

        computer_turn = True
        while computer_turn == True:
            func_comp_calc_score = calculate_score(computer_cards)
            if func_comp_calc_score < 21:
                if func_comp_calc_score < 17:
                    func_deal_card = deal_card(cards)
                    computer_cards.append(func_deal_card)
                    calculate_score(computer_cards)
                    print(f"This is the computer's hand: {computer_cards}") 
                elif func_comp_calc_score >= 17:
                    computer_turn = False
            else:
                time.sleep(3)
                computer_turn = False    
        if player_turn == False and computer_turn == False:
            os.system('cls')
            func_player_calc_score = calculate_score(user_cards)
            print(f"This is your hand: {user_cards}")
            print(f"This is the computer's hand: {computer_cards}")
            func_compare_score = compare_score(func_player_calc_score, func_comp_calc_score)
        else:
            print("Argument invalid. Try again.")
            
        condition = input("Do you want to play again? Y for yes or N for no: ").capitalize().strip()
        if condition == "N":
            os.system("cls")
            print(f"Scoreboard: \nPlayer: {player_wins}\nComputer: {computer_wins}")
            if player_wins > computer_wins:
                print(f"Player has the highest score. Congratulations!")
                time.sleep(3)
            elif player_wins == computer_wins:
                print(f"It's a tie. Congratulations, still!")
                time.sleep(3)
            elif player_wins < computer_wins:
                print(f"Computer has the highest score. Better luck next time.")
                time.sleep(3)
            print("Thank you for playing the game.")
            time.sleep(3)
            os.system("cls")
            game_state = False
        elif condition == "Y":
            os.system("cls")
            print(f"This is the latest scoring: \nPlayer:{player_wins}\nComputer:{computer_wins}")
            time.sleep(1.5)
            print("Clearing...")
            time.sleep(1.5)
            print("Dealing...")
            user_cards.clear()
            computer_cards.clear()
            time.sleep(1.5)
            os.system("cls")
            continue

elif decision == "2":
    print("We'll see you next time, then!")
    time.sleep(1.5)
    os.system("cls")