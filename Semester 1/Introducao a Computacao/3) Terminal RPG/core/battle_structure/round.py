from core.characters_and_squad.character import Character
from core.characters_and_squad.squad import Squad
from core.battle_structure.InitiativePhase import InitiativePhase
from enum import Enum


class RoundPhase(Enum):
    ACTIVE = 0
    INITIATIVE = 1


class BattleWinner(Enum):
    UNDEFINED = 0
    PLAYER = 1
    ENEMY = 2


# todo IMPLEMENTAR a sgunda fase de aCTION
class Round:

    _playerSquad: Squad
    _enemySquad: Squad

    # holds the current Turn phase (active or initiative)
    _currentRoundPhase: RoundPhase
    _initiativePhase: InitiativePhase

    # holds the living characters in order to the action phase
    _actionPhaseOrder: list[Character] = []

    # holds a winner(player or enemy) or undefined value
    _battleWinner: BattleWinner = BattleWinner.UNDEFINED

    def __init__(self, player_squad: Squad, enemy_squad: Squad):

        self.playerSquad = player_squad
        self.enemySquad = enemy_squad

        # Inits Initiative phase
        self.set_current_round_phase(RoundPhase.INITIATIVE)
        # creates a Initiative, prints it on screen and
        self._initiativePhase = InitiativePhase(player_squad, enemy_squad)
        # gets the actionPhaseOrder form the Initiative Phase
        self._actionPhaseOrder = self._initiativePhase.get_actionPhaseOrder()

        # Inits Action Phase
        self.set_current_round_phase(RoundPhase.ACTIVE)
        self.check_if_there_is_a_battle_winner()

    def check_if_there_is_a_battle_winner(self) -> BattleWinner:
        are_all_player_chars_dead = True
        are_all_enemy_chars_dead = True
        # checks if all characters in each one of the squads are dead or not
        for enemy_char in self.enemySquad.get_characterList():
            if enemy_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_enemy_chars_dead = False
        for player_char in self.playerSquad.get_characterList():
            if player_char.get_if_is_alive_and_update_char_action_phase_order():
                are_all_player_chars_dead = False
        # if one of the two squads are completely dead, a winner is found
        if are_all_enemy_chars_dead:
            self._battleWinner = BattleWinner.PLAYER
        elif are_all_player_chars_dead:
            self._battleWinner = BattleWinner.ENEMY
        return self._battleWinner

    def get_current_round_phase(self) -> RoundPhase:
        return self._currentRoundPhase

    def set_current_round_phase(self, phase_state: RoundPhase):
        self._currentRoundPhase = phase_state

    def get_battle_winner(self) -> BattleWinner:
        return self._battleWinner

