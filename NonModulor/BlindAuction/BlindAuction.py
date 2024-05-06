# Blind Auction
from blindAuctionData import logo


guest = {}

print(logo)
print("Welcome to the blind auction.")

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    guest[name] = bid

    halt = input("Are there any other bidders? type 'y' for yes: ")
    if halt == 'y':
        for key in guest:
            if guest[key] == max(guest.values()):
                print("Winner is", key, "their bid was", guest[key])

        break
