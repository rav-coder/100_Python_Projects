
bidder = 'yes'

bidders = {}

highest_bid = {}

highest_amount = 0

while bidder != 'no':
    name = input("What is your name?: ").lower()
    amount = int(input("What is your bid?: $"))

    bidders[name] = amount

    bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    #print(bidder)

if bidder == 'no':
    for key in bidders:
        if bidders[key] > highest_amount:
            highest_bid['name'] = key
            highest_bid['amount'] = bidders[key]
            highest_amount = bidders[key]

    print(f"{highest_bid['name']} has the highest bid of ${highest_bid['amount']}")




