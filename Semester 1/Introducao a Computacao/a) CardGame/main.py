import os
import random


class Card:
    def __init__(self, symbol: str, value: int, suit: str):
        self.symbol = symbol
        self.value = value
        self.suit = suit

    def to_string(self):
        return f"[{self.symbol}{self.suit}]"


class Deck:

    TOT_CARDS_PER_LINE = 14

    def __init__(self, name: str, cards_list: list[Card]):
        self.cards_list = cards_list
        self.name = name

    def to_string(self) -> str:
        string = f"{self.name}: \n"
        counter = 0
        for card in self.cards_list:
            if counter >= Deck.TOT_CARDS_PER_LINE-1:
                string += "\n"
                counter = 0
            string += card.to_string() + " "
            counter += 1
        return string

    def to_string_all_blocked(self) -> str:
        string = f"{self.name}: \n"
        counter = 0
        for card in self.cards_list:
            if counter >= Deck.TOT_CARDS_PER_LINE-1:
                string += "\n"
                counter = 0
            string += "[//]" + " "
            counter += 1
        return string

    def shuffle_it(self) -> None:
        random.shuffle(self.cards_list)

    def _get_last_2_cards(self) -> list[Card]:
        return [self.cards_list[len(self.cards_list)-2], self.cards_list[len(self.cards_list)-1]]

    def get_last_2_cards_as_string(self):
        txt = f"{self.name} last 2 cards: "
        for ending_card in self._get_last_2_cards():
            txt += ending_card.to_string() + " "
        txt += f"| sum = {self.get_sum_of_last_2_cards()}"
        return txt

    def get_sum_of_last_2_cards(self) -> int:
        return self._get_last_2_cards()[0].value + self._get_last_2_cards()[1].value


class Game:

    LIST_OF_SUITS = ["#", "&", "@", "?"]

    def __init__(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        self.buying_deck: Deck = Game._get_a_full_deck()
        print(self.buying_deck.to_string() + "\n")
        self.buying_deck.shuffle_it()
        print("SHUFFLE BUYING DECK")
        print(self.buying_deck.to_string() + "\n")

        input("press enter to generate a round")
        os.system('cls' if os.name == 'nt' else 'clear')

        print("GIVING RANDOM CARDS TO PLAYER AND COMPUTER\n")
        self.player_deck: Deck = Deck("player", self.get_14_random_cards_from_buying_deck())
        self.computer_deck: Deck = Deck("computer", self.get_14_random_cards_from_buying_deck())



        while True: # only breacks at play op

            print(self.buying_deck.to_string() + "\n")
            print(self.computer_deck.to_string_all_blocked() + "\n")
            print(self.player_deck.to_string() + "\n")

            op = input("OPTIONS:\n[1:Discard all]\n[2:Discard 1]\n[3:Play]\nInput: ")

            if op == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.give_14_cards_to_the_buying_deck(self.player_deck)
                print("BUYING DECK WITH NEW CARDS")
                print(self.buying_deck.to_string() + "\n")
                self.buying_deck.shuffle_it()
                print("SHUFFLE BUYING DECK")
                print(self.buying_deck.to_string() + "\n")
                self.player_deck = Deck("player", self.get_14_random_cards_from_buying_deck())
                print("DECKS AFTER BUYING DECK HAS GIVEN PLAYER NEW CARDS")

            elif op == "2":

                input_card_symbol = input("insert card symbol: ")
                input_card_suit = input("insert card suit: ")
                is_it_in_player_deck = False

                for card in self.player_deck.cards_list:
                    if card.symbol == input_card_symbol and card.suit == input_card_suit:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        is_it_in_player_deck = True
                        self.buying_deck.cards_list.append(card)
                        self.player_deck.cards_list.remove(card)
                        print("BUYING DECK WITH NEW CARDS")
                        print(self.buying_deck.to_string() + "\n")
                        self.buying_deck.shuffle_it()
                        print("SHUFFLE BUYING DECK")
                        print(self.buying_deck.to_string() + "\n")
                        self.player_deck.cards_list.append(self.get_1_random_card_from_buying_deck())
                        print("DECKS AFTER BUYING DECK HAS GIVEN PLAYER NEW CARDS")

                if not is_it_in_player_deck:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{input_card_symbol}{input_card_suit} is not in {self.player_deck.name}")
                    input(f"press enter to pick another action")
                    print()


            elif op == "3":
                print()
                print("\nLAST 2 CARDS OF EACH DECK ")
                print(self.player_deck.get_last_2_cards_as_string())
                print(self.computer_deck.get_last_2_cards_as_string() + "\n")
                if self.player_deck.get_sum_of_last_2_cards() > self.computer_deck.get_sum_of_last_2_cards():
                    print(f"{self.player_deck.name} wins")
                elif self.player_deck.get_sum_of_last_2_cards() < self.computer_deck.get_sum_of_last_2_cards():
                    print(f"{self.computer_deck.name} wins")
                else:
                    print("it's a draw")
                break

            else:
                os.system('cls' if os.name == 'nt' else 'clear')


    @staticmethod
    def _get_a_full_deck() -> Deck:
        buying_cards_list = []
        for k in range(0, len(Game.LIST_OF_SUITS)):
            for i in range(2, 10 + 1):
                buying_cards_list.append(Card(str(i), i, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("J", 11, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("Q", 12, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("K", 13, Game.LIST_OF_SUITS[k]))
            buying_cards_list.append(Card("A", 14, Game.LIST_OF_SUITS[k]))
        return Deck("Buying Deck", buying_cards_list)

    def get_14_random_cards_from_buying_deck(self) -> list[Card]:
        cards = []
        for i in range(0, 14-1):
            random_index = random.randint(0, len(self.buying_deck.cards_list)-1)
            cards.append(self.buying_deck.cards_list[random_index])
            self.buying_deck.cards_list.remove(self.buying_deck.cards_list[random_index])
        return cards

    def give_14_cards_to_the_buying_deck(self, deck: Deck) -> None:
        cards = []
        for i in range(0, 14 - 1):
            cards.append(deck.cards_list[i])
        for card in cards:
            self.buying_deck.cards_list.append(card)
            deck.cards_list.remove(card)




    def get_1_random_card_from_buying_deck(self) -> Card:
        random_index = random.randint(0, len(self.buying_deck.cards_list) - 1)
        card = self.buying_deck.cards_list[random_index]
        self.buying_deck.cards_list.remove(card)
        return card



Game()


"""
list_of_cards = []
deck1 = Deck("My Deck", list_of_cards)
deck2 = Deck("Computer", list_of_cards.copy())

print("\nINITIAL DECKS ")
print(deck1.to_string())
print(deck2.to_string() + "\n")

deck1.shuffle_it()
deck2.shuffle_it()
print("\nSHUFFLE DECKS ")
print(deck1.to_string())
print(deck2.to_string() + "\n")

print("\nLAST 2 CARDS OF EACH DECK ")
print(deck1.get_last_2_cards_as_string())
print(deck2.get_last_2_cards_as_string() + "\n")

if deck1.get_sum_of_last_2_cards() > deck2.get_sum_of_last_2_cards():
    print(f"{deck1.name} wins")
elif deck1.get_sum_of_last_2_cards() < deck2.get_sum_of_last_2_cards():
    print(f"{deck2.name} wins")
else:
    print("it's a draw")

"""
