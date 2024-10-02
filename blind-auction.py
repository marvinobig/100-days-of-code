# Blind Auction
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the
# output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it.
import os

def bid_number(num):
    try:
        return float(num) if float(num) > 0 else False
    except ValueError:
        return False

def clear_screen():
    print("\n" * 100)

auction_bids = {}
add_bid = False

while not add_bid:
    new_user = input("Hello bidder! What is your name? ").title()

    if not new_user.strip():
        clear_screen()
        print("Name cannot be empty")
        continue

    if new_user in auction_bids:
        overwrite = input(f"Bidder {new_user} already bid. Do you want to overwrite their bid? (yes/no) ")

        if overwrite in ["no", "n"]:
            clear_screen()
            continue

    new_bid = bid_number(input("How much are you bidding? "))

    if new_bid:
        auction_bids.update({ new_user : new_bid })
    else:
        clear_screen()
        print("Bid number needs to be a valid and positive number")
        continue

    confirmation = input("Are there more bidders? (yes/no) ").lower()

    add_bid = confirmation in ["no", "n"]
    clear_screen()

if auction_bids:
    print(f"The winner is {max(auction_bids, key=auction_bids.get)} with a bid of ${max(auction_bids.values()):.2f}")
else:
    print("No valid bids were placed")