import random

def simulate_coupon_collector():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    cards_picked = set()
    picks_needed = 0

    while len(cards_picked) < len(suits):
        card = f"{random.choice(ranks)} of {random.choice(suits)}"
        print(card)
        
        cards_picked.add(card.split()[-1])  # Extract the suit and add it to the set
        picks_needed += 1

    print(f"\nNumber of picks: {picks_needed}")

# Run the simulation
simulate_coupon_collector()
