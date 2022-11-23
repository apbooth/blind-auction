from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bid_details = {}

continue_auction = True
while continue_auction:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: £"))
    bid_details[bidder_name] = bid_amount
    more_bids = input("Any other bidders? : Type 'yes' or 'no' ").lower()
    
    if more_bids == "yes":
        clear()
    elif more_bids == "no":
        continue_auction = False
        highest_bid = 0
        for bidder in bid_details:
            if bid_details[bidder] > highest_bid:
                highest_bid = bid_details[bidder]
                winner_of_auction = bidder

        print(f"The winner is: {winner_of_auction} with a bid of £{highest_bid}")
