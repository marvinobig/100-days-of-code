# Blind Auction
# Each person writes their name and bid.
# The program asks if there are others who need to bid. If so, then the computer clears the
# output (prints several blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid, the program works out who has the highest bid and prints it.

def bid_number(num):
    try:
        return float(num)
    except ValueError:
        return False

auction_bids = {}
add_bid = False

while not add_bid:
    new_user = input("Hello bidder! What is your name? ").capitalize()
    new_bid = bid_number(input("How much are you bidding? "))

    if new_bid:
        auction_bids.update({ new_user : new_bid })
    else:
        print("Bid number needs to be a valid number")
        continue

    confirmation = input("Are there more bidders? (yes/no) ").lower()

    add_bid = confirmation in ["no", "n"]
    print('\n' * 50)

print(f"The winner is {max(auction_bids, key=auction_bids.get)} with a bid of ${max(auction_bids.values())}")
