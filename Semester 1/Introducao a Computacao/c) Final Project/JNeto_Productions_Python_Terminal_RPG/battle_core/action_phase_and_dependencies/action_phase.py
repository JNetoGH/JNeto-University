from random import randrange

from battle_abilities.ability import PhysicalAtk
from battle_core.action_phase_and_dependencies.player_action_manager import PlayerActionManager
from ui import ui_resources, battle_stats
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.initiative_phase import InitiativePhase


class ActionPhase:

    def __init__(self, initiative_phase: InitiativePhase):

        self.initiative_phase = initiative_phase
        self.squad1 = self.initiative_phase.squad1
        self.squad2 = self.initiative_phase.squad2
        self.action_order_list: list[Character] = self.initiative_phase.action_order_list                               # used for action order control: char will be removed if dead or if has already played
        self._all_chars = self.action_order_list.copy()                                                                 # used for combat: chars will not be removed

        self._force_skip_turn = False
        self.force_quit_battle = False

        while len(self.action_order_list) != 0 and self.is_there_a_winner() == Ownership.NULL:                          # while action_order_list is not empty and there is no winner
            print(battle_stats.get_battle_current_state(self.initiative_phase), end="")                                 # prints Ui
            current_char = self.action_order_list[0]                                                                    # sets the current char according to the action order list
            self._run_action_turn_for_char(current_char)                                                                # runs action of the current char user/AI based
            self.remove_a_char_from_action_order_list(current_char)                                                     # removes from the action order list the current char, passing the action to the next on if the is any
            self.remove_dead_chars_from_action_order_list()                                                             # removes all dead chars from the action order list th
            if self._force_skip_turn:                                                                                   # ActionPhase flow control: checks for skips and breaks, if there is none, cleans the screen to next char, if there is any
                self._force_skip_turn = False
                ui_resources.clear_terminal()
                print()
                continue
            elif self.force_quit_battle:
                ui_resources.clear_terminal()
                break
            else:
                input("press enter to next turn")
            ui_resources.clear_terminal()                                                                               # clears the screen for the next ui
            print()

    def _run_action_turn_for_char(self, char: Character) -> None:
        if char.ownership == Ownership.PLAYER:
            self._player_action(char)
        elif char.ownership == Ownership.ENEMY:
            self._ai_action(char)
        print()  # jumps a line

    def _player_action(self, current_char: Character) -> None:
        PlayerActionManager(self, current_char, all_chars=self._all_chars)

    def _ai_action(self, char: Character) -> None:
        print("\nai can only make physical atks according to professor's rules")

        # generates a list of possible chars
        list_of_possible_targets = []
        for target in self._all_chars:
            if (not target.is_dead()) and target.ownership != char.ownership:
                list_of_possible_targets.append(target)

        chosen_index = -1
        # can't make a  range between 0 and 0, so whe there is only one possibility i hardcoded it
        if len(list_of_possible_targets) == 1:
            chosen_index = 0
        else:
            chosen_index = randrange(0, len(list_of_possible_targets)-1)
        chosen_target = list_of_possible_targets[chosen_index]
        atk = PhysicalAtk()
        atk.exec(char, chosen_target)
        print(f"{char.name} attacked {chosen_target.name} dmg dealt = {atk.dmg}")


    def remove_a_char_from_action_order_list(self, char: Character) -> bool:
        if char in self.action_order_list:
            self.action_order_list.remove(char)
            return True

    def remove_dead_chars_from_action_order_list(self) -> bool:
        for char in self.action_order_list:
            if char.is_dead():
                self.action_order_list.remove(char)
                return True

    def is_there_a_winner(self) -> Ownership:
        if ActionPhase.is_squad_all_dead(self.squad1):
            return self.squad2.ownership
        elif ActionPhase.is_squad_all_dead(self.squad2):
            return self.squad1.ownership
        return Ownership.NULL

    @staticmethod
    def is_squad_all_dead(squad: Squad) -> bool:  # used in is_there_a_winner()
        is_squad_all_dead = True
        for char in squad.list_of_char:
            if not (char.is_dead()):
                is_squad_all_dead = False
        return is_squad_all_dead

