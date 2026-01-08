import art
import game_data
import random

while True:
    # Write an intro and ask if the player wants to play
    print(art.logo)
    print("Welcome to the Higher or Lower game! Make a guess on who has more followers.")
    play = input("Type 'y' to play or 'n' to exit: ")
    # If the player doesn't want to play, exit
    if play == 'n':
        break

    print("\n" * 20)
    print(art.logo)
    # Data we need: score, the game data
    score = 0
    data = game_data.data

    # What the game will do: take two random instagram profiles and compare their follower count and come with a result
    profileA = data[random.randint(0, len(data)-1)]
    profileB = data[random.randint(0, len(data)-1)]

    in_round = True

    while in_round:
        # If both profiles are the same, change profileB
        while profileB == profileA:
            profile2 = data[random.randint(0, len(data)-1)]

        print(f"Compare A: {profileA['name']}, {profileA['description']}, from {profileA['country']}")
        print(art.vs)
        print(f"Against B: {profileB['name']}, {profileB['description']}, from {profileB['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")

        # Check if the choice is correct and the chosen profile has more follower count
        if choice == 'A' and profileA['follower_count'] > profileB['follower_count']:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
        elif choice == 'B' and profileB['follower_count'] > profileA['follower_count']:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
        else:
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score {score}")
            input("Press Enter to continue...")
            in_round = False
            print("\n" * 20)
            break

        profileA = profileB
        profileB = data[random.randint(0, len(data)-1)]