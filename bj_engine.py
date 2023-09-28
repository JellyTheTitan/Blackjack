#All code is by JellyTheTitan! If you are copying this file, please give attribution. Thank you!

import math
import random
from os import system
from termcolor import colored

def reset_deck():
  global card_deck
  
  card_deck = []
  card_deck = ["Ace of Spades", "Ace of Hearts", "Ace of Clubs", "Ace of Diamonds", "2 of Spades", "2 of Hearts", "2 of Clubs", "2 of Diamonds", "3 of Spades", "3 of Hearts", "3 of Clubs", "3 of Diamonds", "4 of Spades", "4 of Hearts", "4 of Clubs", "4 of Diamonds", "5 of Spades", "5 of Hearts", "5 of Clubs", "5 of Diamomds", "6 of Spades", "6 of Hearts", "6 of Clubs", "6 of Diamonds", "7 of Spades", "7 of Hearts", "7 of Clubs", "7 of Diamonds", "8 of Spades", "8 of Hearts", "8 of Clubs", "8 of Diamonds", "9 of Spades", "9 of Hearts", "9 of Clubs", "9 of Diamonds", "10 of Spades", "10 of Hearts", "10 of Clubs", "10 of Diamonds", "Jack of Spades", "Jack of Hearts", "Jack of Clubs", "Jack of Diamonds", "Queen of Spades", "Queen of Hearts", "Queen of Clubs", "Queen of Diamonds", "King of Spades", "King of Hearts", "King of Clubs", "King of Diamonds"]

def generate_hands():
  global hand
  global hand_value
  global dealer_hand
  global picked_card
  global sc
  global set_card
  global picked_card_dealer
  global card_deck
  global set_hand
  global hand_value

  hand = []
  dealer_hand = []
  for i in range(2):
    set_hand = "player"
    picked_card = random.randrange(0,len(card_deck))
    sc = picked_card
    set_card = card_deck[sc]
    hand.append(card_deck[sc])
    check_card()
    
    set_hand = "dealer"
    picked_card_dealer = random.randrange(0, abs(len(card_deck)))
    sc = picked_card_dealer
    set_card = card_deck[sc]
    dealer_hand.append(card_deck[sc])
    check_card()
    
def reset_game():
  
  global card
  
  card = None
  
  global hand
  
  hand = []
  
  global hand_value
  
  hand_value = 0
  
  global chips
  
  chips = 0
  
  global dealer_hand 
  
  dealer_hand = []
  
  global dealer_hand_value
  
  dealer_hand_value = 0
  
  global picked_card
  
  picked_card = 0
  
  global picked_card_dealer
  
  picked_card_dealer = 0
  
  global difficulty
  
  difficulty = "n"
  
  global game
  
  game = True
  
  global sc
  
  sc = None
  
  global bet
  
  bet = 0
  
  global set_card
  
  set_card = None
  
  global current_hand
  
  current_hand = None
  
  global ace
  
  ace = None
  
  global action
  
  action = None
  
  global set_hand
  
  set_hand = None

  global hand2

  hand2 = []

  global hand_value2

  hand_value2 = 0

  global hand_value3

  hand_value3 = 0

  global index

  index = 0

  global splitting

  splitting = False

  #alr_ace means "already aced?" 
  
  global alr_ace

  alr_ace = False

  global dealer_alr_ace

  dealer_alr_ace = False

  global dealer_action

  dealer_action = None

  #doudow means "double downed?"

  global doudow

  doudow = False

  #dbs means "dealer busted said?"

  global dbs

  dbs = False

  global h1s

  h1s = False

  global h2s

  h2s = False

  global action2

  action2 = None

  global winner 

  winner = None

  global char

  char = ("a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "-", "_", "[", "]", "{", "}", "/", "|", "\\", "'", "\"", ";", ":", ",", ".", "<", ">", "?", "`", "~")

  global contains_char

  contains_char = False

  global alr_ace2

  alr_ace2 = False

  global set_card2

  set_card2 = None

  global sc2

  sc2 = None

  global picked_card2

  picked_card2 = None
  
  reset_deck()

def check_card():
  
  global hand_value
  global dealer_hand_value
  global set_card
  global splitting
  global hand_value2
  global set_hand
  global hand_value3
  
  if set_hand == "player":
    if "Ace" in set_card:
      hand_value = hand_value + 11
      if hand_value > 21:
        hand_value = hand_value - 10
    if "2" in set_card:
      hand_value = hand_value + 2
    if "3" in set_card:
      hand_value = hand_value + 3
    if "4" in set_card:
      hand_value = hand_value + 4
    if "5" in set_card:
      hand_value = hand_value + 5
    if "6" in set_card:
      hand_value = hand_value + 6
    if "7" in set_card:
      hand_value = hand_value + 7
    if "8" in set_card:
      hand_value = hand_value + 8
    if "9" in set_card:
      hand_value = hand_value + 9
    if "10" in set_card:
      hand_value = hand_value + 10
    if "Jack" in set_card:
      hand_value = hand_value + 10
    if "Queen" in set_card:
      hand_value = hand_value + 10
    if "King" in set_card:
      hand_value = hand_value + 10
  
  elif set_hand == "dealer":
    if "Ace" in set_card:
      dealer_hand_value = dealer_hand_value + 11
      if dealer_hand_value > 21:
        dealer_hand_value = dealer_hand_value - 10
    if "2" in set_card:
      dealer_hand_value = dealer_hand_value + 2
    if "3" in set_card:
      dealer_hand_value = dealer_hand_value + 3
    if "4" in set_card:
      dealer_hand_value = dealer_hand_value + 4
    if "5" in set_card:
      dealer_hand_value = dealer_hand_value + 5
    if "6" in set_card:
      dealer_hand_value = dealer_hand_value + 6
    if "7" in set_card:
      dealer_hand_value = dealer_hand_value + 7
    if "8" in set_card:
      dealer_hand_value = dealer_hand_value + 8
    if "9" in set_card:
      dealer_hand_value = dealer_hand_value + 9
    if "10" in set_card:
      dealer_hand_value = dealer_hand_value + 10
    if "Jack" in set_card:
      dealer_hand_value = dealer_hand_value + 10
    if "Queen" in set_card:
      dealer_hand_value = dealer_hand_value + 10
    if "King" in set_card:
      dealer_hand_value = dealer_hand_value + 10
    
  elif set_hand == "h1":
    if "Ace" in set_card:
      hand_value2 = hand_value2 + 11
      if hand_value2 > 21:
        hand_value2 = hand_value2 - 10
    if "2" in set_card:
      hand_value2 = hand_value2 + 2
    if "3" in set_card:
      hand_value2 = hand_value2 + 3
    if "4" in set_card:
      hand_value2 = hand_value2 + 4
    if "5" in set_card:
      hand_value2 = hand_value2 + 5
    if "6" in set_card:
      hand_value2 = hand_value2 + 6
    if "7" in set_card:
      hand_value2 = hand_value2 + 7
    if "8" in set_card:
      hand_value2 = hand_value2 + 8
    if "9" in set_card:
      hand_value2 = hand_value2 + 9
    if "10" in set_card:
      hand_value2 = hand_value2 + 10
    if "Jack" in set_card:
      hand_value2 = hand_value2 + 10
    if "Queen" in set_card:
      hand_value2 = hand_value2 + 10
    if "King" in set_card:
      hand_value2 = hand_value2 + 10

  elif set_hand == "h2":
    if "Ace" in set_card:
      hand_value3 = hand_value3 + 11
      if hand_value3 > 21:
        hand_value3 = hand_value3 - 10
    if "2" in set_card:
      hand_value3 = hand_value3 + 2
    if "3" in set_card:
      hand_value3 = hand_value3 + 3
    if "4" in set_card:
      hand_value3 = hand_value3 + 4
    if "5" in set_card:
      hand_value3 = hand_value3 + 5
    if "6" in set_card:
      hand_value3 = hand_value3 + 6
    if "7" in set_card:
      hand_value3 = hand_value3 + 7
    if "8" in set_card:
      hand_value3 = hand_value3 + 8
    if "9" in set_card:
      hand_value3 = hand_value3 + 9
    if "10" in set_card:
      hand_value3 = hand_value3 + 10
    if "Jack" in set_card:
      hand_value3 = hand_value3 + 10
    if "Queen" in set_card:
      hand_value3 = hand_value3 + 10
    if "King" in set_card:
      hand_value3 = hand_value3 + 10

def check_split():
  global set_card
  global action
  global splitting
  global hand
  global hand2
  
  if not len(hand) > 2:
    if "Ace" in hand[0] and "Ace" in hand[1] or "2" in hand[0] and "2" in hand[1] or "3" in hand[0] and "3" in hand[1] or "4" in hand[0] and "4" in hand[1] or "5" in hand[0] and "5" in hand[1] or "6" in hand[0] and "6" in hand[1] or "7" in hand[0] and "7" in hand[1] or "8" in hand[0] and "8" in hand[1] or "9" in hand[0] and "9" in hand[1] or "10" in hand[0] and "10" in hand[1] or "Jack" in hand[0] and "Jack" in hand[1] or "Queen" in hand[0] and "Queen" in hand[1] or "King" in hand[0] and "King" in hand[1]:
      if splitting == False:
        splitting = True
        set_card = hand[1]
        hand.remove(set_card)
        hand2.append(set_card)
    else:
      action = None
      print("{You can only split with 2 of the same cards!}")
      print()
  else:
    action = None
    print("{You can only split on the beggining of your turn!}")
    print()

def check_for_char():
  global bet
  global char
  global contains_char

  i = 0
  contains_char = False
  while not i == len(char) and not contains_char == True:
    if char[i] in bet:
      contains_char = True
    i = i + 1

def check_deck_length():
  global card_deck
  
  if len(card_deck) < 5:
    reset_deck()

reset_game()

print("Welcome to JellyTheTitan's Blackjack!")
print("To play Blackjack, your goal is simple: get up to (but not over!) 21, while also trying to outdo the dealers hand.")
print('''On your turn, put down the amount of chips you want to bet, then decide if you want to hit (add a card to your hand), stay (end your turn), double down (double bet and add a card,  but can only do once and on the beginning of your turn), or split (take two of your same cards and make a seperate hand and bet).''')
print()
print('''You can hit as many times as you want, just as long as you don't go over 21, because if you do, you lose!''')
print()
print('''Always keep in mind that some cards have different values (read the "Card Value Key" for more imformation).''')
print()
print('''[Card Value Key]
{Ace} - 1 or 11
{2 - 10} - Face Value
{Jack} - 10
{Queen} - 10
{King} - 10''')
print()

difficulty = input("Select your difficulty (this will determine your amount of starter chips) [Difficulty Key - e = Easy, n = Normal, h = Hard]: ")

if difficulty == "e" or difficulty == "E":
  chips = 10000
elif difficulty == "n" or difficulty == "N":
  chips = 5000
elif difficulty == "h" or difficulty == "H":
  chips = 1000
else:
  print()
  print("{Your option could not be read, so it was set to normal mode.}")
  chips = 5000
  
print()
print("The game has started!")
print()

#The while loop below will repeat until the player doesn't have any money 

while not chips <= 0: 
  print("Your Current Amount of Chips:")
  print()
  print("$" + str(chips))
  print()
  bet = input('''How much do you bet?: ''')
  check_for_char()
  if not contains_char == True:
    if not bet == "" and not bet == "0":
      if int(bet) > chips:
        bet = "1"
        print()
        print("{You can't bet more than what you have.}")       
    else:
      bet = "1"
      print()
      print("{Your bet could not be read, so it was set to the minimum bet ($1).}")
  else:
    bet = "1"
    print()
    print("{Your bet could not be read, so it was set to the minimum bet ($1).}")

  chips = chips - int(bet)
  print()
  print("You decide to bet " + "$" + str(bet))
  print()
  print("The dealer hands out the cards. . .")
  
  generate_hands()
  
  print()
  print('''Your Hand:''')
  for x in hand:
    print(x)
  print()
  print('''Your Hand Value:''')
  print()
  print(int(hand_value))
  print()
  print("Dealers Showing Card:")
  print(dealer_hand[1])
  print()
  if not hand_value == 21:
    while hand_value < 21 and not action == "st" and not action == "ST" and not action == "St" and not action == "sT" and not action == "dd" and not action == "DD" and not action == "Dd" and not action == "dD" and not action == "sp" and not action == "SP" and not action == "St" and not action == "sT":
      action = input('''What do you want to do? (h = Hit, st = Stay, dd = Double Down, sp = Split): ''') 
      print()

      #This code is for hitting
      
      if action == "h" or action == "H":
        print("You decide to hit")
        print()
        print("The dealer draws you a card. . .")
        set_hand = "player"
        check_deck_length()
        picked_card = random.randrange(0, abs(len(card_deck)))
        sc = picked_card
        set_card = card_deck[sc]
        hand.append(card_deck[sc])
        check_card()
        print()
        print("Your New Card:")
        print(set_card)
        print()
        if hand_value > 21:
          index = 0
          if not alr_ace == True: 
            while not index == len(hand) and alr_ace == False:
              if "Ace" in hand[index]:
                if not alr_ace == True:
                  hand_value = hand_value - 10
                  alr_ace = True
              index = index + 1
            if hand_value > 21:
              winner = "dealer"
              print(colored("You bust!", "red"))
              print()
            else:
              print("Your New Hand Value:")
              print()
              print(hand_value)
              print()
          else:
            winner = "dealer"
            print(colored("You bust!", "red"))
            print()
        else:
          print("Your New Hand Value:")
          print()
          print(hand_value)
          print()

      #This code is for staying
        
      elif action == "st" or action == "ST" or action == "St" or action == "sT":
        print("You decide to stay")
        print()

      #This code is for double downing
        
      elif action == "dd" or action == "DD" or action == "Dd" or action == "dD":
        if not len(hand) > 2 and not int(bet) * 2 > chips:
          chips = chips - int(bet)
          bet = int(bet) * 2 
          print("You decide to double down")
          print()
          print("The dealer draws you a card. . .")
          dowdou = True
          set_hand = "player"
          check_deck_length()
          picked_card = random.randrange(0, abs(len(card_deck)))
          sc = picked_card
          set_card = card_deck[sc]
          hand.append(card_deck[sc])
          check_card()
          print()
          print("Your New Card:")
          print(set_card)
          print()
          if hand_value > 21:
            index = 0
            if not alr_ace == True: 
              while not index == len(hand) and alr_ace == False:
                if "Ace" in hand[index]:
                  if not alr_ace == True:
                    hand_value = hand_value - 10
                    alr_ace = True
                index = index + 1
              if hand_value > 21:
                winner = "dealer"
                print(colored("You bust!", "red"))
                print()
              else:
                print("Your New Hand Value:")
                print()
                print(hand_value)
                print()
            else:
              winner = "dealer"
              print(colored("You bust!", "red"))
              print()
          else:
            print("Your New Hand Value:")
            print()
            print(hand_value)
            print()
        else:
          if len(hand) > 2 and not int(bet) * 2 > chips:
            print("{You can only double down on the beggining of your turn!}")
            print()
            action = None
          else:
            print("{You can't double down more than what you have!}")
            print()
            action = None

      #This code is for splitting
          
      elif action == "sp" or action == "SP" or action == "Sp" or action == "sP": 
        check_split()
        if splitting == True:
          check_deck_length()
          alr_ace = False
          chips = chips - int(bet)
          print("You decide to split your cards")
          print()
          print("Your First Hand:")
          for i in hand:
            print(i)
          print()
          set_hand = "h1"
          check_card()
          print("Your Second Hand:")
          for i in hand2:
            print(i)
          print()
          set_hand = "h2"
          check_card()
          bet = int(bet) * 2
          set_hand = "h1"
          while not action2 == "st" or action2 == "ST" or action2 == "St" or action2 == "sT" and not hand_value2 >= 21: 
            action2 = input('''What do you want to do? (h = Hit, st = Stay): ''')
            if action2 == "h" or action2 == "H":
              print()
              print("You decide to hit")
              print()
              print("The dealer draws you a card. . .")
              print()
              check_deck_length()
              picked_card2 = random.randrange(0, abs(len(card_deck)))
              sc = picked_card
              set_card = card_deck[sc]
              hand.append(set_card)
              check_card()
              print("Your New Card:")
              print(set_card)
              print()
              if hand_value2 > 21:
                index = 0
                if not alr_ace == True: 
                  while not index == len(hand) and alr_ace == False:
                    if "Ace" in hand[index]:
                      if not alr_ace == True:
                        hand_value2 = hand_value2 - 10
                        alr_ace = True
                    index = index + 1
                  if hand_value2 > 21:
                    winner = "dealer"
                    print(colored("You bust!", "red"))
                    print()
                  else:
                    print("Your New Hand Value:")
                    print()
                    print(hand_value2)
                    print()
                else:
                  winner = "dealer"
                  print(colored("You bust!", "red"))
                  print()
              else:
                print("Your New Hand Value:")
                print()
                print(hand_value2)
                print()
            else:
              if not action2 == "" and action2 == "st" or action2 == "ST" or action2 == "St" or action2 == "sT":
                h1s = True
          print()
          print("You decide to stay")
          print()
          print("You move on to your second hand. . .")
          print()
          print("Your Second Hand:")
          for i in hand2:
            print(i)
          print()
          print("Your Second Hand's Value:")
          print()
          print(hand_value3)
          print()
          action2 = None
          alr_ace = False
          set_hand = "h2"
          alr_ace = False
          while not action2 == "st" or action2 == "ST" or action2 == "St" or action2 == "sT" and not hand_value3 >= 21:
            action2 = input('''What do you want to do? (h = Hit, st = Stay): ''')
            if action2 == "h" or action2 == "H":
              print("You decide to hit")
              print()
              print("The dealer draws you a card. . .")
              print()
              check_deck_length()
              picked_card = random.randrange(0,abs(len(card_deck)))
              sc = picked_card
              set_card = card_deck[sc]
              hand2.append(set_card)
              check_card()
              print()
              print("Your New Card:")
              print(set_card)
              print()
              if hand_value3 > 21:
                index = 0
                if not alr_ace == True: 
                  while not index == len(hand2) and alr_ace == False:
                    if "Ace" in hand[abs(index)]:
                      if not alr_ace == True:
                        hand_value3 = hand_value3 - 10
                        alr_ace = True
                    index = index + 1
                  if hand_value3 > 21:
                    winner = "dealer"
                    h2s = "st"
                    print(colored("You bust!", "red"))
                    print()
                  else:
                    print("Your New Hand Value:")
                    print()
                    print(hand_value3)
                    print()
                else:
                  winner = "dealer"
                  h2s = "st"
                  print(colored("You bust!", "red"))
                  print()
              else:
                print("Your New Hand Value:")
                print()
                print(hand_value3)
                print()
            else:
              if not action2 == "" and action2 == "st" or action2 == "ST" or action2 == "St" or action2 == "sT":
                print()
                print("You decide to stay")
                print()
                h2s = True

    #The dealer does his stuff here
    
    if not hand_value > 21:
      print("The dealer reveals his hidden card. . .")
      print()
      print("The Dealers Hand:")
      for i in dealer_hand:
        print(i)
      print()
      print("The Dealer's Hand Value:")
      print()
      print(dealer_hand_value)
      print()
      while not dealer_hand_value >= 17:
        print("The dealer hits and draws a card. . .")
        set_hand = "dealer"
        picked_card = random.randrange(0,len(card_deck))
        sc = picked_card
        set_card = card_deck[sc]
        dealer_hand.append(card_deck[sc])
        check_card()
        print()          
        print("The Dealer's New Card:")
        print(set_card)
        print()
        if dealer_hand_value > 21:
          index = 0
          if not dealer_alr_ace == True: 
            while not index == len(dealer_hand) and dealer_alr_ace == False:
              if "Ace" in dealer_hand[index]:
                if not dealer_alr_ace == True:
                  dealer_hand_value = dealer_hand_value - 10
                  dealer_alr_ace = True
              index = index + 1
            if dealer_hand_value > 21:
              if not dbs == True:
                dbs = True
                print(colored("The dealer busts!", "green"))
                print()
            else:
              print("The Dealer's New Hand Value:")
              print()
              print(dealer_hand_value)
              print()
          else:
            if not dbs == True:
              dbs = True
              print()
        else:
          print("The Dealer's New Hand Value:")
          print()
          print(dealer_hand_value)
          print()

      #The code below checks the dealers hand value, and then prints if he won or lost

      if not dealer_hand_value > 21:
        print("The dealer stays. . .")
        print()
      else:
        if not dbs == True:
          print(colored("The dealer busts!", "green"))
          print()

  #This code checks who won the hand
  
  if not splitting == True:
    if not dealer_hand_value > hand_value:
      if not hand_value == 21 and not len(hand) == 2:
        if not hand_value == dealer_hand_value:
          if not hand_value > 21:
            chips = chips + int(bet) * 2
            print(colored("You win!", "green"))
            print()
          else:
            print(colored("You lose the hand!", "red"))
            print()
        else:
          chips = chips + int(bet)
          print(colored("You and the dealer push.", "yellow"))
          print()
      else:
        if len(hand) == 2 and hand_value == 21:
          chips = chips + int(bet) * 4
          print(colored("You got a blackjack!", "green"))
          print()
        else:
          if not hand_value == dealer_hand_value:
            chips = chips + int(bet) * 2
            print(colored("You win!", "green"))
            print()
          else:
            chips = chips + int(bet)
            print(colored("You and the dealer push.", "yellow"))
            print()
    else:
      if not dealer_hand_value > 21 and not dealer_hand_value == hand_value and not hand_value > 21: 
        print(colored("The dealer wins!", "red"))
        print()
      else:
        if hand_value > 21 and not dealer_hand_value == hand_value and dealer_hand_value > 21:
          print("The dealer busts; however, because you busted, you lose!")
          print()
        else:
          if not hand_value > 21:
            if not hand_value == dealer_hand_value:
              chips = chips + int(bet) * 2
              print(colored("You win!", "green"))
              print()
            else:
              chips = chips + int(bet)
              print(colored("You and the dealer push.", "yellow"))
              print()
          else:
            print(colored("You lose!", "red"))
            print()
  else:
    if not dealer_hand_value > hand_value2:
      if not hand_value2 == dealer_hand_value:
        chips = chips + int(bet) * 2
        print(colored("You win the first hand!", "green"))
        print()
      else:
        chips = chips + int(bet)
        print(colored("You and the dealer push on the first hand.", "yellow"))
        print()
    else:
      if hand_value2 > 21 or dealer_hand_value > hand_value2:
        print(colored("You lose the first hand!", "red"))
        print()         
      else:
        if not hand_value2 > 21:
          chips = chips + int(bet) * 2
          print(colored("You win the first hand!", "green"))
          print()
        else:
          print(colored("You lose the first hand!", "red"))
          print()
    
    if not dealer_hand_value > hand_value3:
      if not hand_value3 == dealer_hand_value:
        chips = chips + int(bet) * 2
        print(colored("You win the second hand!", "green"))
        print()
      else:
        chips = chips + int(bet)
        print(colored("You and the dealer push on the second hand.", "yellow"))
        print()
    else:
      if hand_value3 > 21 or dealer_hand_value > hand_value3:
        print(colored("You lose the second hand!", "red"))
        print()         
      else:
        if not hand_value3 > 21:
          chips = chips + int(bet) * 2
          print(colored("You win the second hand!", "green"))
          print()
        else:
          print(colored("You lose the second hand!", "red"))
          print()
   
  con = input(colored("Press Enter To Continue ", "blue"))
  system("clear")

  #This code resets everything after a hand ends
  
  hand = []
  hand2 = []
  dealer_hand = []
  hand_value = 0
  hand_value2 = 0
  hand_value3 = 0
  dealer_hand_value = 0
  bet = "0"
  splitting = False
  action = None
  action2 = None
  alr_ace = False
  dealer_alr_ace = False
  dealer_action = None
  dealer_alr_ace = False
  dbs = False
  doudow = False
  h1s = False
  h2s = False
  winner = None
  contains_char = False
  
print(colored("You don't have any chips left!", "red"))
print()
print(colored("Game Over!", "red"))