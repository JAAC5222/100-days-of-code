# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

auction = {}

print(art.logo)

maxBid = 0

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    auction[name] = bid
    if bid > maxBid:
        maxBid = bid

    keep = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if keep == "yes":
        continue
    elif keep == "no":
        winner = [k for k, v in auction.items() if v == maxBid]
        if len(winner) == 1:
            print("The winner is ", winner[0], "with a bid of ", maxBid, ".")
        elif len(winner) > 1:
            print(f"The winners are ", end='')
            for i in winner:
                print(i, end=" ")
            print(f"with a bid of {maxBid}.")
    break