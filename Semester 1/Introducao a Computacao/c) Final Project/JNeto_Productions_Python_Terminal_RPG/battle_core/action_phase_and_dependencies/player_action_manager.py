from ui import battle_stats
from typing import Union
from battle_abilities.ability import *
from battle_entities.char_and_squad import Character, Ownership


# It manages the user's input in order to make an action.
# The Action Phase Caller is required only to set the skip and quit battle option at the Phase Loop
class PlayerActionManager:

    def __init__(self, ActionPhaseCaller, current_char: Character, all_chars):

        self.all_chars = all_chars
        print(f"\nTURN: {current_char.name}")
        print(battle_stats.get_char_card(current_char))  # prints the current char card

        action_done = False
        while not action_done:

            action_kind = input(f"What should {current_char.name} do? [1:Atk] [2:Spell] [3:Skip] [4:Quit]: ")

            if action_kind.capitalize() == "Atk" or action_kind == "1":
                atk = PhysicalAtk()
                target_char: Character = self._get_a_target_by_name_from_player_and_validate_target(current_char, atk.can_affect_allies, atk.can_affect_caster)
                if target_char == "RETURN":  # if the player picks a char called return target will be "RETURN"
                    continue
                atk.exec(current_char, target_char)
                print(f"{current_char.name} attacked {target_char.name}: tot dmg(atk-def) = {atk.dmg}\n")
                action_done = True

            elif action_kind.capitalize() == "Spell" or action_kind == "2":
                spell = PlayerActionManager.get_a_spell_in_char_from_player_and_validate_spell(current_char)
                if spell == "RETURN":  # if player has chosen return spell won't be a Spell, will be "RETURN"
                    continue
                target = self._get_a_target_by_name_from_player_and_validate_target(current_char, spell.can_affect_allies, spell.can_affect_caster, spell.can_affect_enemy)
                if target == "RETURN":  # if the player picks a char called return target will be "RETURN"
                    continue
                spell.exec(current_char, target)
                action_done = True

            elif action_kind.capitalize() == "Skip" or action_kind == "3":
                ActionPhaseCaller._force_skip_turn, action_done = True, True

            elif action_kind.capitalize() == "Quit" or action_kind == "4":
                ActionPhaseCaller.force_quit_battle, action_done = True, True

    @staticmethod
    def get_a_spell_in_char_from_player_and_validate_spell(current_char: Character) -> Union[Spell, str]:
        if not current_char.have_spells():
            print(f"invalid, {current_char.name} doesn't have any spells")
        else:
            battle_stats.display_char_spells(current_char)
            while True:  # gets a valid spell asking its index
                spell_input = input("insert a spell number or type return to choose another action: ")
                if spell_input.upper() == "RETURN":
                    return "RETURN"
                elif not (spell_input.isnumeric()):
                    print("invalid input, please insert a index")
                elif spell_input.isnumeric():
                    spell_index = int(spell_input)
                    if 0 <= spell_index < len(current_char.spells):
                        spell: Spell = current_char.spells[spell_index]
                        if current_char.mana < spell.mana_cost:
                            print(f"{spell.name} cost({spell.mana_cost}) > {current_char.name} mana {current_char.mana}")
                        else:
                            return spell
                    else:
                        print(f"invalid input, there is no spell with index {spell_input}")

    def _get_a_target_by_name_from_player_and_validate_target(self, current_char: Character, can_pick_allies: bool, can_pick_itself: bool, can_pick_enemy: bool = True) -> Union[Character, str]:
        target_char: Character = None
        while not isinstance(target_char, Character):
            chosen_char_name = input(f"Which char should {current_char.name} pick? insert its name or type return: ").capitalize()
            if chosen_char_name == "":
                continue
            if chosen_char_name.upper() == "RETURN":
                return "RETURN"
            # gets the chosen char among the avaliables one in battle
            for char in self.all_chars:
                if char.name.capitalize() == chosen_char_name:
                    target_char = char
            # checks if the chosen char is valid according to those rules
            if target_char is None:
                print(f"invalid input, {chosen_char_name} does not exist")
            elif target_char is current_char and not(can_pick_itself):
                print("invalid input, this ability can't affect its caster")
                target_char = None
            elif target_char.is_dead():
                print(f"invalid input, {target_char.name} is already dead")
                target_char = None
            elif (not can_pick_allies) and target_char.ownership == current_char.ownership:
                print(f"invalid input, this ability doesn't allow picking an ally")
                target_char = None
            if target_char.ownership == Ownership.ENEMY and can_pick_enemy == False:
                print(f"invalid input, this ability doesn't allow picking an enemy")
                target_char = None

        return target_char
