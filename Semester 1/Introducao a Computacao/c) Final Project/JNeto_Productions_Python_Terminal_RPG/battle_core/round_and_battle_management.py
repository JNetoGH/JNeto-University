from battle_entities.char_and_squad import Squad, Ownership
from battle_core.initiative_phase import InitiativePhase
from battle_core.action_phase_and_dependencies.action_phase import ActionPhase
from ui import battle_stats


class Round:
    def __init__(self, squad1: Squad, squad2: Squad):
        self.initiativePhase = InitiativePhase(squad1, squad2)
        self.actionPhase = ActionPhase(self.initiativePhase)


class Battle:
    def __init__(self, squad1: Squad, squad2: Squad):
        current_round = None
        while True:
            current_round = Round(squad1, squad2)
            if current_round.actionPhase.force_quit_battle:
                print("exit battle")
                break
            elif current_round.actionPhase.is_there_a_winner() != Ownership.NULL:
                break
            else:
                print("action order list is empty")
                print("another list will be generated")
                input("press enter to generate another round")

        print()
        print(battle_stats.get_battle_current_state(current_round.initiativePhase), end="")
        print()
        if current_round.actionPhase.is_there_a_winner() == Ownership.PLAYER:
            print("player venceu!!!!!!")
        elif current_round.actionPhase.is_there_a_winner() == Ownership.ENEMY:
            print("Enemy venceu!!!!!")
        print("Battle finished!!!!!")

