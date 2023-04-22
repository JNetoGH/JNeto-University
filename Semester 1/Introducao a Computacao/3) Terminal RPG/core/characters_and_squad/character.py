from utilities.jneto_string_builder import StringBuilder

NULL_ACTION_PHASE_ORDER: int = 0


class Character:

    _currentActionPhaseOrder: int = NULL_ACTION_PHASE_ORDER

    def __init__(self, name: str, hp: int, mana: int, armor, weapon_dmg: int, initiative: int):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.weapon_dmg = weapon_dmg
        self.initiative = initiative

    def to_string(self) -> str:
        str_builder: StringBuilder = StringBuilder()
        str_builder.append("Name: " + str(self.name))
        str_builder.append(" | HP: " + str(self.hp))
        str_builder.append(" | Mana: " + str(self.mana))
        str_builder.append(" | Armor: " + str(self.armor))
        str_builder.append(" | Weapon Dmg: " + str(self.weapon_dmg))
        str_builder.append(" | Initiative: " + str(self.initiative))
        return str_builder.to_string()

    def get_if_is_alive_and_update_char_action_phase_order(self):
        is_it_alive = self.hp > 0
        if not is_it_alive:
            self._currentActionPhaseOrder = NULL_ACTION_PHASE_ORDER
        return is_it_alive

    def get_char_currentActionPhaseOrder(self) -> int:
        return self._currentActionPhaseOrder

    def set_currentActionPhaseOrder(self, value: int):
        self._currentActionPhaseOrder = value