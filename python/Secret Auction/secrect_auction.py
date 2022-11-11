#Secret Auction Program
import replit
from secret_art import logo
print (logo)

bids = {}

status = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not status:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $ "))
    bids[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if again == 'no':
        status = True
        find_highest_bidder(bids)
    elif again == 'yes':
        replit.clear()