# NAO PODE SER IMPAR
GENERAL_CARD_LENGTH = 24
GENERAL_CARD_PADDING = 3

# DOUBLE LINES
GENERAL_WALL = "║"
GENERAL_LINE = "═"
GENERAL_UP_LEFT_CORNER = "╔"
GENERAL_BOTTOM_LEFT_CORNER = "╚"
GENERAL_UP_RIGHT_CORNER = "╗"
GENERAL_BOTTOM_RIGHT_CORNER = "╝"

# LIGHT SINGLE LINES
GENERAL_LIGHT_LINE = "─"
GENERAL_LIGHT_LEFT_CONNECTOR = "╟"
GENERAL_LIGHT_RIGHT_CONNECTOR = "╢"

# USER ONLY IN: get_battle_current_state()
GENERAL_SEPARATORS_LENGTH: int = 78

GRAY = "\033[90m"
CLEAR = "\033[0m"
BOLD = '\33[1m'


def get_char_card(char, line_length: int = GENERAL_CARD_LENGTH) -> str:
    # used to print the card as red
    code1 = ""
    code2 = CLEAR
    if char.is_dead():
        code1 = GRAY
    card = code1

    card += f"{GENERAL_UP_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_UP_RIGHT_CORNER}\n"
    card += get_centralized_txt_in_line(line_length, char.name, GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}\n"
    card += get_centralized_txt_in_line(line_length, f"HP: {char.health}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_txt_in_line(line_length, f"Attack: {char.weapon_dmg}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_txt_in_line(line_length, f"Mana: {char.mana}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_txt_in_line(line_length, f"Armor: {char.armor}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += get_centralized_txt_in_line(line_length, f"Initiative: {char.initiative}", GENERAL_WALL, GENERAL_WALL) + "\n"

    if char.have_spells():
        card += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}\n"
        card += get_centralized_txt_in_line(line_length, "SPELLS", GENERAL_WALL, GENERAL_WALL) + "\n"
        for spell in char.spells:
            card += get_centralized_txt_in_line(line_length, f"{spell.name}", GENERAL_WALL, GENERAL_WALL) + "\n"
    card += f"{GENERAL_BOTTOM_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_BOTTOM_RIGHT_CORNER}"

    # used to print the card as red
    card += code2
    return card


def get_squad_char_cards_inline(squad, line_length: int = GENERAL_CARD_LENGTH, padding: int = GENERAL_SEPARATORS_LENGTH) -> str:
    squad_char_cards_inline = ""
    tot_lines = 9
    for i in range(0, tot_lines):
        add_line_break = i != tot_lines-1
        squad_char_cards_inline += _get_char_card_squad_line(squad, i, line_length, padding, add_line_break)
    return squad_char_cards_inline


# concatenates the all the chars cards (x line) into one single line, separated with a padding
def _get_char_card_squad_line(squad, line_index, line_length, padding, add_line_break: bool) -> str:
    line = ""
    for char in squad.list_of_char:

        # used to print the card as gray
        code1 = ""
        code2 = CLEAR
        if char.is_dead():
            code1 = GRAY
        line += code1

        if line_index == 0:
            line += f"{GENERAL_UP_LEFT_CORNER}{(GENERAL_LINE * (line_length - 2))}{GENERAL_UP_RIGHT_CORNER}" + " " * padding
        elif line_index == 1:
            line += get_centralized_txt_in_line(line_length, char.name, GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 2:
            line += f"{GENERAL_LIGHT_LEFT_CONNECTOR}{GENERAL_LIGHT_LINE * (line_length - 2)}{GENERAL_LIGHT_RIGHT_CONNECTOR}" + " " * padding
        elif line_index == 3:
            line += get_centralized_txt_in_line(line_length, f"HP: {char.health}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 4:
            line += get_centralized_txt_in_line(line_length, f"Attack: {char.weapon_dmg}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 5:
            line += get_centralized_txt_in_line(line_length, f"Mana: {char.mana}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 6:
            line += get_centralized_txt_in_line(line_length, f"Armor: {char.armor}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 7:
            line += get_centralized_txt_in_line(line_length, f"Initiative: {char.initiative}", GENERAL_WALL, GENERAL_WALL) + " " * padding
        elif line_index == 8:
            line += f"{GENERAL_BOTTOM_LEFT_CORNER}{GENERAL_LINE * (line_length - 2)}{GENERAL_BOTTOM_RIGHT_CORNER}" + " " * padding

        # used to print the card as red
        line += code2

    if add_line_break:
        line += "\n"
    return line


def get_centralized_txt_in_line(card_width: int, msg: str = "Default", wall1: str = " ", wall2: str = " ") -> str:
    # tem q ser medido antes dos códigos de stilo entrar, se n eles contam pro tamanhaho
    msg_len = len(msg)

    if card_width % 2 != 0:
        raise Exception("cards can't be set with an odd width, only even")

    is_msg_length_even = msg_len % 2 == 0
    if is_msg_length_even:
        return wall1 + " " * (int((card_width / 2 - msg_len / 2)) - 1) + msg + " " * (int((card_width / 2 - msg_len / 2)) - 1) + wall2
    # Adds an extra space "|" -> " |", e.g. len(msg) = 11, the division per 2 would be 5, not 5.5,
    # therefore, it would be, (line_length - 5) + msg + (line_length - 5), being discounted 10 for the msg instead o 11
    else:
        return wall1 + " " * (int((card_width / 2 - msg_len / 2)) - 1) + msg + " " * (int((card_width / 2 - msg_len / 2)) - 1) + " " + wall2


def get_battle_current_state(initiative_phase) -> str:
    separators_length = len(initiative_phase.to_string())
    spaces_margin = 4
    is_margin_even = spaces_margin % 2 == 0
    if not(is_margin_even):
        spaces_margin += 1


    WHITE_BG = "\033[107m"
    CBLACK = '\33[30m'
    state = ""
    state += initiative_phase.squad1.to_string() + "\n"
    state += get_centralized_txt_in_line(78, "«VS»") + "\n"
    state += initiative_phase.squad2.to_string() + "\n\n"
    state += CBLACK + WHITE_BG + "┏" + "━" * (separators_length+spaces_margin) + "┓" + CLEAR + "\n"
    state += CBLACK + WHITE_BG + "┃" + " " * int(spaces_margin/2) + initiative_phase.to_string() + " " * int(spaces_margin/2) + "┃" + CLEAR + "\n"
    state += CBLACK + WHITE_BG + "┗" + "━" * (separators_length+spaces_margin) + "┛" + CLEAR + "\n"
    return state


# prints the spells of a char as a list, with name + mana cost + description
def display_char_spells(current_char) -> None:
    print(f"\n{current_char.name} Spells")
    print("--------------------------------------")
    count = 0
    for spell in current_char.spells:
        print(f"[{count}]{spell.name} (mana:{spell.mana_cost}): {spell.description}")
        count += 1
    print("--------------------------------------")