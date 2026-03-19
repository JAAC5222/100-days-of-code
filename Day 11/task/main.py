import art
import random

def check_ace(game_cards):
    if sum(game_cards) > 21 and 11 in game_cards:
        for card in range(len(game_cards)):
            if game_cards[card] == 11:
                game_cards[card] = 1
                break

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    if input("Do you want to play a game of Blackjack?: Type 'y' or 'n': ") == 'n':
        break

    print("\n" * 20)
    print(art.logo)

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    final_message = ""

    in_round = True

    print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

    while in_round:

        option = input("Type 'y' to get another card, type 'n' to pass: ")
        if option == 'y':

            player_cards.append(random.choice(cards))
            check_ace(player_cards)

            print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"    Computer's first card: {computer_cards[0]}")

            if sum(player_cards) > 21:
                print(f"   Your final hand: {player_cards}, final score: {sum(player_cards)}")
                print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                in_round = False
                print("You went over. You lose 😭")
        elif option == 'n':
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))

            if sum(computer_cards) <= 21:
                if sum(computer_cards) > sum(player_cards):
                    final_message = "You lose! 😤"
                elif sum(computer_cards) == sum(player_cards):
                    final_message = "Draw! 😯"
                else:
                    final_message = "You win! 😃"
            else:
                final_message = "Opponent went over. You win! 😁"

            print(f"   Your final hand: {player_cards}, final score: {sum(player_cards)}\n"
                  f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
                  f"{final_message}")
            in_round = False
