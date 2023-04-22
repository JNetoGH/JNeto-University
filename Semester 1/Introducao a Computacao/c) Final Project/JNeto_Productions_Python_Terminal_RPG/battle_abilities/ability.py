from random import randrange

# BLUE PRINT CLASSES
# ====================================================================================================================

class Ability:
    def __init__(self, can_affect_allies: bool, can_affect_caster: bool):
        self.can_affect_caster = can_affect_caster
        self.can_affect_allies = can_affect_allies

    def exec(self, caster, target):
        pass

class PhysicalAtk(Ability):
    def __init__(self):
        super().__init__(can_affect_allies=False, can_affect_caster=False)
        self.dmg = 0

    def exec(self, caster, target):
        dmg = caster.weapon_dmg - target.armor
        if dmg < 0:
            dmg = 0
        target.health -= dmg
        if target.health < 0:
            target.health = 0
        self.dmg = dmg


class Spell(Ability):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int,  can_affect_allies: bool, can_affect_caster: bool, can_affect_enemy: bool):
        super().__init__(can_affect_allies=can_affect_allies, can_affect_caster=can_affect_caster)
        self.can_affect_enemy = can_affect_enemy
        self.mana_cost = mana_cost
        self.effect_points = effect_points
        self.name = name
        self.description = description

    def decrease_mana_from_caster(self, charCaster):
        charCaster.mana -= self.mana_cost

    def exec(self, caster, target):
        self.decrease_mana_from_caster(caster)


class DmgSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int):
        super().__init__(name, description, effect_points, mana_cost, can_affect_allies=False, can_affect_caster=False, can_affect_enemy=True)

    def exec(self, caster, target):
        super(DmgSpell, self).exec(caster, target)
        target.health -= self.effect_points
        if target.health < 0:
            target.health = 0


class HealingSpell(Spell):
    def __init__(self, name: str, description: str, effect_points: int, mana_cost: int, can_affect_allies: bool, can_affect_caster: bool):
        super().__init__(name, description, effect_points, mana_cost, can_affect_allies=can_affect_allies, can_affect_caster=can_affect_caster, can_affect_enemy=False)

    def exec(self, caster, target):
        super(HealingSpell, self).exec(caster, target)
        target.health += self.effect_points


# ACTUALLY USED IN GAME
# ====================================================================================================================

class RushDown(DmgSpell):
    def __init__(self):
        super().__init__("RushDown", "dgm (ATK dmg + D4)", 0, 5)

    def exec(self, caster, target):
        dmg = caster.weapon_dmg + randrange(1, 4)
        self.effect_points = dmg
        super(RushDown, self).exec(caster, target)


class ArmorCracker(DmgSpell):
    def __init__(self):
        super().__init__("ArmorCracker", "ATK dmg + (destroys enemy armor)", 0, 5)

    def exec(self, caster, target):
        dmg = caster.weapon_dmg
        self.effect_points = dmg
        target.armor = 0
        super(ArmorCracker, self).exec(caster, target)


class Exorcism(DmgSpell):
    def __init__(self):
        super().__init__("Exorcism", "dmg (2 * D4)", 0, 5)

    def exec(self, caster, target):
        dmg = 2 * randrange(1, 2)
        self.effect_points = dmg
        super(Exorcism, self).exec(caster, target)


class Mend(HealingSpell):
    def __init__(self):
        super().__init__("Mend", "heal (ATK + D6)", 0, 5, can_affect_allies=True, can_affect_caster=True)

    def exec(self, caster, target):
        heal = caster.weapon_dmg + randrange(1, 6)
        self.effect_points = heal
        super(HealingSpell, self).exec(caster, target)
