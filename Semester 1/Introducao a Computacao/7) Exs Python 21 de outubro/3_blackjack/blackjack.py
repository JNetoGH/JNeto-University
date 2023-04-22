import os
import time
from random import randint


class Card:
    sp_cards_dictionary = {
        "king": 10,
        "jack": 10,
        "queen": 10,
        "ace": 1
    }

    def __init__(self, value):
        self.isSpCard = False
        self.isAce = False
        self.name = str(value)
        self.suit = ""
        if type(value) is int and 2 <= value <= 10:
            self.numericValue = value
        elif type(value) is str and value in Card.sp_cards_dictionary:
            self.numericValue = Card.sp_cards_dictionary[value]
            self.isSpCard = True
            self.isAce = True if value == "ace" else False
        else:
            raise Exception("Invalid card value was insert")


class Actor:

    def __init__(self):
        self.cards: list[Card] = []
        self.totAces: int = 0
        self.totAmount: int = 0

    def add_card(self, card1):
        if card1.isAce:
            self.totAces += 1
        self.cards.append(card1)
        self._update_totAmout()

    def _update_totAmout(self):
        self.totAmount = 0  # sets the total amount to 0 and recalculates it
        has_already_found_an_sp_but_not_ace_card = False
        for i in range(0, len(self.cards)):
            self.totAmount += self.cards[i].numericValue  # adds up the value of each car to the value amount
            if self.cards[i].isSpCard and (not self.cards[i].isAce) and (not has_already_found_an_sp_but_not_ace_card):
                has_already_found_an_sp_but_not_ace_card = True
                self.totAmount += self.totAces * 10  # (ace bonus when combine with another sp) - (ace default value)

    def print_cards(self):
        print("CARDS: [ ", end="")
        for card in self.cards:
            print(card.name + card.suit, end=" ")
        print(f"] \nTOTAL POINTS: {self.totAmount}")


class SuitDeck:

    def __init__(self, suit_name):
        self.name = suit_name
        self.cardsList = [Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10),
                          Card("king"), Card("queen"), Card("jack"), Card("ace")]
        for card in self.cardsList:
            card.suit = suit_name

    def to_string(self) -> str:
        string = f"{self.name} ["
        for card in self.cardsList:
            string += card.name + self.name + " "
        string += "]"
        return string


class Round:

    def __init__(self):
        self.player = Actor()
        self.dealer = Actor()
        self.suitDecksList: list = [SuitDeck("*"), SuitDeck("$"), SuitDeck("+"), SuitDeck("!")]

        print()
        self.print_available_cards()

        print("\nGIVING CARDS TO PLAYER AND DEALER...")
        time.sleep(1)
        self.give_a_random_card_to_actor_from_a_random_suit_deck(self.player)
        self.give_a_random_card_to_actor_from_a_random_suit_deck(self.dealer)
        self.give_a_random_card_to_actor_from_a_random_suit_deck(self.player)
        self.give_a_random_card_to_actor_from_a_random_suit_deck(self.dealer)

        print()
        self.print_available_cards()
        print("\n\33[92mPLAYER ")
        self.player.print_cards()
        print("\n\33[93mDEALER ")
        self.dealer.print_cards()
        print("\33[0m")

        print("=" * 50)
        if self.player.totAmount > self.dealer.totAmount:
            print("\33[92mPLAYER WINS\33[0m")
        elif self.player.totAmount < self.dealer.totAmount:
            print("\33[93mDEALER WINS\33[0m")
        else:
            print("\33[95mIT'S A DRAW\33[0m")
        print("=" * 50)

    def give_a_random_card_to_actor_from_a_random_suit_deck(self, actor: Actor):
        actor_suit_deck: SuitDeck = self.suitDecksList[randint(0, len(self.suitDecksList) - 1)]
        actor_card: Card = actor_suit_deck.cardsList[randint(0, len(actor_suit_deck.cardsList) - 1)]
        actor.add_card(actor_card)
        actor_suit_deck.cardsList.remove(actor_card)

    def print_available_cards(self):
        print("THESE ARE THE AVAILABLE CARDS:")
        for suit in self.suitDecksList:
            print(suit.to_string())


# Game Loop
flag = True
while flag:
    Round()
    while True:
        code = input("wanna play another round? [y/n]: ")
        if code.upper() == "N" or code.upper() == "NO":
            flag = False
            break
        elif code.upper() == "Y" or code.upper() == "YES":
            print("starting another round \n")
            os.system('cls')
            break
        else:
            print("please insert y or n")