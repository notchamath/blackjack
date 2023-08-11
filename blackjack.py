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

from art import logo
import os
import random


# Clear console
def clear(): os.system("clear")


# Print all cards and results
def show_cards(player, dealer, is_final_hand):

    # Normal print
    if not is_final_hand:
        print(f"Your cards: {player['cards']}, current score: {player['total']}")
        print(f"Dealer's first card: {dealer['cards'][0]}")
    
    # Final print
    else:
        p_total = player["total"]
        d_total = dealer["total"]

        print(f"Your final hand: {player['cards']}, final score: {p_total}")
        print(f"Dealer's final hand: {dealer['cards']}, final score: {d_total}")

        if p_total > 21:
            print("You lose.")
        elif d_total > 21:
            print("You win.")
        elif p_total == d_total: 
            print("Its a Draw.")
        elif (21 - p_total) < (21 - d_total):
            print("You win.")
        else:
            print("You lose.")
        

# Chooses cards for dealer and player randomly
def choose_card(num_of_cards, person):
    cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for i in range(num_of_cards):
        card = random.choice(cards)

        if card == "ace":
            if (person["total"] + 11) > 21:
                card = 1
            else:
                card = 11

        person["cards"].append(card)
        person["total"] += card

    return person


# Chooses all of dealer's cards outside of the initial two
def get_dealer_cards(dealer):
    while dealer["total"] <= 17:
        dealer = choose_card(1, dealer)
    
    return dealer


# Start game
def play_blackjack():

    dealer = {
        "cards": [],
        "total": 0,
    }
    player = {
        "cards": [],
        "total": 0,
    }
    is_final_hand = False

    clear()
    print(logo)

    # Initial Dealer cards
    dealer = choose_card(2, dealer)

    # Initial Player cards
    player = choose_card(2, player)

    # Display cards
    show_cards(player, dealer, is_final_hand)

    # While loop to allow user to hit or stand
    while not is_final_hand:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        # Player choose to hit
        if add_card == "y":
            # Give another card
            player = choose_card(1, player)
            
            # If player total over 21, game ends
            if player["total"] > 21:
                is_final_hand = True
            # If player total is 21 game ends but dealer gets to complete his hand
            elif player["total"] == 21:
                is_final_hand = True
                dealer = get_dealer_cards(dealer)
            # Display cards
            show_cards(player, dealer, is_final_hand)
        
        # Player chose to stand, game ends, dealer gets to complete his hand
        elif add_card == "n":
            is_final_hand = True
            dealer = get_dealer_cards(dealer)
            show_cards(player, dealer, is_final_hand)


# While loop to give user the option to start game or leave
while True:
    is_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if is_playing == "y":
        play_blackjack()
    elif is_playing == "n":
        print("Goodbye.")
        break

