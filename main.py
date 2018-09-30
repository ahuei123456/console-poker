import os, io, itertools, random


opening_message = 'Welcome to Console Poker!'
suits = ['Club', 'Diamond', 'Heart', 'Spade']
numbers = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
cards = list(itertools.product(numbers, suits))
hand = []


def poker_loop():
    poker_start()


def poker_start():
    print(opening_message)

    random.shuffle(cards)
    for i in range(5):
        hand.append(cards.pop())

    print(hand)


def identify_hand():


def print_hand():
    i = 1
    for card in hand:
        print('{}: {} of {}')



if __name__ == '__main__':
    poker_loop()
