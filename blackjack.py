# PROGRAM NAME    : GAME OF BLACKJACK
# FILE NAME       : BLACKJACK.PY
# DESCRIPTION     : THE GAME OF BLACKJACK PROGRAMMED AS A PYTHON CONSOLE APPLICATION
# PROGRAMMER      : JORDAN WICKENS
# DATE            : 01-10-2020
# VERSION         : 1.0.0

# Libraries
import random
import os

purse = 1000 # Starting balance for the player
play = True  # Bool to run game loop
ACE = 11     # Constant for an Ace

# Main game loop
while play:
  
  print('---New hand---')
  print('Your purse: $' + str(purse) + '\n')

  # Set of dealer cards
  dealer_cards = []
  # Set of player cards
  player_cards = []

  # Place bet
  betEntry = int(input("Enter bet amount: "))
  while purse - betEntry < 0:
    print('Not enough funds.')
    betEntry = int(input("Enter bet amount: "))

  bet = betEntry
  # ---------------------- Start of card dealing ---------------------------

  # Dealer's cards
  while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
      print ('Dealer has X & ' + str(dealer_cards[1]))

  # Player's cards
  while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
      print ('You have ' + str(player_cards[0]) + ' & ' + str(player_cards[1]))
      if sum(player_cards) == 21: # Player gets BlackJack
        print('You have BlackJack!')
        print('The dealer has a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)
        if sum(dealer_cards) == 21:
          print('PUSH... unlucky')
          break
        else:
          print('WINNER WINNER CHICKEN DINNER!!') 
          purse = purse + (bet / 2) * 3
          break
    # ------------------ End card dealing ------------------------------------


    # ------------------ Start of valuing an Ace as high or low --------------
      if 11 in player_cards: # Check if there is an 11 dealt to player
        if player_cards[0] == ACE and player_cards[1] == ACE: # Check if both cards are aces
          hand_value = int(input("Pocket Aces! Choose hand value: 2 or 12?\n"))
          if hand_value == 2: # reset the players hand to be a sum of 2
            player_cards[0] = 1
            player_cards[1] = 1
          elif hand_value == 12: # reset the players hand to be sum of 12
            player_cards[0] = 11
            player_cards[1] = 1
        elif player_cards[0] == ACE:
          ace_value = int(input("Value the Ace: 1 or 11?\n"))
          player_cards[0] = ace_value
          print('You now have a total of ' + str(sum(player_cards)) + ' from these cards', player_cards)
        elif player_cards[1] == ACE:
          ace_value = int(input("Value the Ace: 1 or 11?\n"))
          player_cards[1] = ace_value
          print('You now have a total of ' + str(sum(player_cards)) + ' from these cards', player_cards)
    # -------------------- End of Ace valuing ------------------------


  # ---------------------- Start of logic for hit and stay --------------------
  while sum(player_cards) < 21:
    action_taken = str(input("stay or hit?\n"))
    if action_taken == "hit":
      player_cards.append(random.randint(1, 11))
      if player_cards[-1] == ACE:
        ace_value = int(input("Player drew Ace. Value the Ace: 1 or 11?\n"))
        player_cards[-1] = ace_value
      print('You now have a total of ' + str(sum(player_cards)) + ' from these cards', player_cards)
    else:
      # Show current hands after player stays
      print('The dealer has a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)
      print('You have a total of ' + str(sum(player_cards)) + ' with ', player_cards)

      # Forces the dealer to hit until a sum of 17 or higher is reached
      while sum(dealer_cards) < 17:
        dealer_cards.append(random.randint(1, 11))
        print('The dealer draws ' + str(dealer_cards[-1]) + ' for a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)


      if sum(dealer_cards) > 21: # If the sum of dealer cards is over 21, they bust
        print('Dealer BUST! You Win!')
        purse = (purse + bet)
        break

      # By now, the player or dealer would have busted if sum over 21
      if sum(dealer_cards) > sum(player_cards): # If dealer is closer to 21 they win
        print('Dealer wins.')
        purse = (purse - bet)
        break # stops from repromting user b/c they arent at 21 yet in the loop
      elif sum(player_cards) > sum(dealer_cards): # If player is closer to 21 they win 
        print('You win!') # Player was closer so player wins
        purse = (purse + bet)
        break
      elif sum(player_cards) == sum(dealer_cards):
        print('PUSH')
        break

  if sum(player_cards) == 21:
    while sum(dealer_cards) < 17:
      dealer_cards.append(random.randint(1, 11))
      print('The dealer draws ' + str(dealer_cards[-1]) + ' for a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)
    if sum(dealer_cards) > 21:  # If the sum of dealer cards is over 21, they bust
      print('Dealer BUST! You Win!')
      purse = purse + bet
    elif sum(dealer_cards) < sum(player_cards):
      print('You win!')
      purse = (purse + bet)
    elif sum(dealer_cards) == sum(player_cards):
      print('PUSH')

  if sum(player_cards) > 21: # Player sum over 21 makes them bust
    print('You BUSTED! Dealer wins.')
    purse = (purse - bet)

  # -------------------- End of logic for hit and stay ---------------------

  # -------------------- Start of logic for quitting or replaying ----------
  choice = str(input("Another hand? (y)(n)\n"))

  if choice == 'n':
    print('You walk away with $' + str(purse))
    print('Good luck at the next table!')
    play = False
  elif choice == 'y':
    if purse > 0:
      os.system('cls' if os.name == 'nt' else 'clear')
    else:
      decision = str(input('Not enough funds. Would you like to add more or quit? (add)(quit)\n'))
      if decision == 'add':
        purse = int(input("Enter your deposit: "))
        print('Thanks!')
      else:
        print('You walk away with $' + str(purse))
        print('Good luck at the next table!')
        play = False
  # -------------------- End of logic for quitting or replaying -------------



  # TODO: Integrate splitting, doubling money, and a purse with running balance

  # TODO: Create menu / settings to display game instructions,
  # buy more chips, cash out, and other things like that
