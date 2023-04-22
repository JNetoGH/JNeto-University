from core.battle_structure.round import *
from core.characters_and_squad.character import Character
from core.characters_and_squad.squad import Squad


class Battle:

    playerSquad: Squad
    enemySquad: Squad
    currentRound: Round

    # holds a winner(player or enemy) or undefined value
    battleWinner: BattleWinner = BattleWinner.UNDEFINED

    def __init__(self, player_squad: Squad, enemy_squad: Squad):
        self.playerSquad = player_squad
        self.enemySquad = enemy_squad

    def init_new_round(self):
        self.currentRound = Round(self.playerSquad, self.enemySquad)
        self.battleWinner = self.currentRound.get_battle_winner()


squadPlayer = Squad([Character("JNeto", 5, 10, 10, 10, 11), Character("Dani", 0, 10, 10, 10, 10)])
squadEnemy = Squad([Character("Bilu", 10, 10, 10, 10, 10), Character("Teteia", 10, 10, 10, 10, 12)])
battle1: Battle = Battle(squadPlayer, squadEnemy)
battle1.init_new_round()
battle1.init_new_round()

"""
battle1.init_new_round()
jneto_utility_methods.draw_round_separator()
print("Action Order:" + jneto_utility_methods.list_to_str(battle1.currentRound.get_actionPhaseOrder_list_as_string()))
print("Round phase:   " + battle1.currentRound.get_current_round_phase().name)
print("Battle winner: " + battle1.battleWinner.name)

jneto_utility_methods.draw_squad_separator()
print("Player Squad \n\n" + battle1.playerSquad.to_string())
jneto_utility_methods.draw_squad_separator()
print("Enemy  Squad \n\n" + battle1.enemySquad.to_string())
jneto_utility_methods.draw_squad_separator()
"""

