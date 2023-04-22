from core.characters_and_squad.character import Character
from core.characters_and_squad.squad import Squad
from utilities import jneto_utility_methods


# todo solve draw cases in Action Order
class InitiativePhase:

    _playerSquad: Squad
    _enemySquad: Squad

    # holds the living characters in order to the action phase, is passed to the Round class via a getter
    _actionPhaseOrder: list[Character] = []

    def __init__(self, player_squad: Squad, enemy_squad: Squad):
        self.playerSquad = player_squad
        self.enemySquad = enemy_squad

        # Inits Initiative phase
        self.print_initiative_phase_ui_header()
        self.clear_actionPhaseOrder_list()
        self.generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self.playerSquad)
        self.generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self.enemySquad)
        self.select_sort_actionPhaseOrder_list()
        self.print_initiative_phase_ui_results()

    def clear_actionPhaseOrder_list(self):  # clears the action phase order list first, making sure it's empty
        self._actionPhaseOrder = []

    # basically checks if the character is alive, then set his/her currentActionPhaseOrder
    # then, adds the character to the _actionPhaseOrder, anf it sorts the list according to the action phase order
    def generate_action_phase_order_for_chars_in_squad_and_add_then_to_action_phase_order_list(self, squad: Squad):
        for char in squad.get_characterList():
            if char.get_if_is_alive_and_update_char_action_phase_order():
                d20: int = jneto_utility_methods.roll_dice(0, 20)
                char.set_currentActionPhaseOrder(char.initiative + d20)
                self._actionPhaseOrder.append(char)
                print(f"Name: {char.name} | Action Order => Initiative ({char.initiative}) + D20 ({d20})"
                      f" => {char.get_char_currentActionPhaseOrder()}")

    def select_sort_actionPhaseOrder_list(self):
        size = len(self._actionPhaseOrder)
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if self._actionPhaseOrder[i].get_char_currentActionPhaseOrder() > self._actionPhaseOrder[min_idx].get_char_currentActionPhaseOrder():
                    min_idx = i
            # put min at the correct position
            (self._actionPhaseOrder[step], self._actionPhaseOrder[min_idx]) = (self._actionPhaseOrder[min_idx], self._actionPhaseOrder[step])

    def print_initiative_phase_ui_header(self):
        jneto_utility_methods.draw_round_separator()
        print("Round phase: INITIATIVE")
        print()
        print("Generating action order with alive characters:")

    def print_initiative_phase_ui_results(self):
        print()
        print("Action Order:" + jneto_utility_methods.list_to_str(jneto_utility_methods.actionPhaseOrder_to_string(self._actionPhaseOrder)))
        jneto_utility_methods.draw_squad_separator()

    def get_actionPhaseOrder(self) -> list[Character]:
        return self._actionPhaseOrder