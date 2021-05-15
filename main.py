############### Blackjack Project 

#TODO:1. Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from replit import clear 
from art import logo
"""returns a random cards from the deck"""
def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10]
  card = random.choice(cards)
  return card

#TODO:3. Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):
  """take a list of card and return the score calculated from the cards"""

#TODO:4. Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards)==21 and len(cards)==2 :
    return 0
  
#TODO:5. Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#TODO:10. Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score,computer_score):
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0 :
    return "Lose , opponent has a Blackjack 🥺"
  elif user_score == 0:
    return "Win with a Blackjack 🥳"
  elif user_score > 21 :
    return "You went over. You lose 🥺"
  elif computer_score > 21 :
    return "opponent went over. You Win 🥳"
  elif user_score > computer_score:
    return "You Win 🥳"
  else:
    return "You Lose 🥺"  

def play_game():

  print(logo)
  #TODO:2.Deal the user and computer 2 cards each using deal_card() and append().
  #user_cards = []
  #computer_cards = []

  user_cards=[]
  computer_cards=[]
  is_game_over=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #TODO:8. The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:

    #TODO:6. Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"your card = {user_cards}\nyour score = {user_score}\ncomputer first card = {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:

      #TODO:7. If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("type 'y' to get another card, type 'n' to pass:")
      if user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        is_game_over=True

  #TODO:9. Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(compare(user_score,computer_score))
#TODO:11. Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play Blackjack game ? type 'y' or 'n' : ")=="y":
  clear()
  play_game()

