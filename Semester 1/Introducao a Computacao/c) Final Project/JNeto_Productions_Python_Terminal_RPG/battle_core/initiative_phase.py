from battle_entities.char_and_squad import Squad, Character
from random import *
import enum


class CharCodes(enum.Enum):
    DEAD_CHAR = -1


class InitiativePhase:

    def __init__(self, squad1: Squad, squad2: Squad):
        self.squad1 = squad1
        self.squad2 = squad2
        self.action_order_list: list[Character] = []  # this class just exists in order to generate this list
        self._generate_turn_orders_of_a_squad(self.squad1)
        self._generate_turn_orders_of_a_squad(self.squad2)
        self._treat_and_add_squad_to_action_order_list(self.squad1)
        self._treat_and_add_squad_to_action_order_list(self.squad2)
        self._insertion_sort_action_order_list()

    @staticmethod
    def _d20() -> int:
        result = randrange(1, 20)
        return result

    @staticmethod
    def _generate_turn_orders_of_a_squad(squad: Squad) -> None:
        for char in squad.list_of_char:
            if char.is_dead():
                char.turn_order = CharCodes.DEAD_CHAR
            else:
                char.turn_order = char.initiative + InitiativePhase._d20()

    def _treat_and_add_squad_to_action_order_list(self, squad: Squad) -> None:
        for char in squad.list_of_char:
            if char.turn_order != CharCodes.DEAD_CHAR:  # simply adds the chars to the list, except the dead ones
                self.action_order_list.append(char)

    def _insertion_sort_action_order_list(self) -> None:
        for i in range(1, len(self.action_order_list)):  # iterate over unsorted array
            val = self.action_order_list[i]  # get element value
            hole = i  # insertion "hole" is at index i
            # loop backwards until a value greater than current value is found
            while hole > 0 and self.action_order_list[hole - 1].turn_order < val.turn_order:
                self.action_order_list[hole] = self.action_order_list[hole - 1]  # swap elements towards correct pos
                hole -= 1  # move backwards
            self.action_order_list[hole] = val  # insert value into correct position

    def to_string(self) -> str:
        text = "ACTION ORDER(init+D20):"
        for i in range(0, len(self.action_order_list)):
            char = self.action_order_list[i]
            text += f" {char.name}({char.turn_order})"
        return text
