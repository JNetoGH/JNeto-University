from ui import ui_resources
from battle_abilities.ability import *
from battle_entities.char_and_squad import Character, Squad, Ownership
from battle_core.round_and_battle_management import Battle

ui_resources.clear_terminal()
input("press enter to start\n")
ui_resources.clear_terminal()
print()


h_spell = HealingSpell("Heal", "heal 3 hp", 3, mana_cost=3, can_affect_allies=True, can_affect_caster=True)
pew_pew = DmgSpell("Pew Pew", "shoots a laser (5 dmg)", effect_points=5, mana_cost=2)
armor_cracker_spell = ArmorCracker()


stor_spell_Rush_Down = RushDown()
stor_spell_Exorcism = Exorcism()
stor_spell_Mend = Mend()

#                              HP  MP AP  WP INIT
warrior = Character("Warrior", 32,  5, 2, 5, 2, [stor_spell_Rush_Down])
priest = Character("Priest",   20, 25, 0, 2, 6, [stor_spell_Exorcism, stor_spell_Mend, h_spell])
cyborg = Character("Cyborg",   20, 10, 1, 3, 4, [armor_cracker_spell, pew_pew])
squad1 = Squad(Ownership.PLAYER, "player squad", [warrior, priest, cyborg])

#                                                                   HP MP AP WP  INIT
squad2 = Squad(Ownership.ENEMY, "enemy squad", [Character("Speedy", 2, 0, 1,  2, 10),
                                                Character("Orc",   15, 0, 3,  3, 2),
                                                Character("Fatty", 10, 0, 5,  2, 1),
                                                Character("Rage",   1, 0, 0,  8, 1)])


battle = Battle(squad1, squad2)
