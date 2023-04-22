from utilities.jneto_string_builder import StringBuilder
import random


def draw_squad_separator():
    print("\n" + "-" * 80 + "\n")


def draw_round_separator():
    print("\n" + "=" * 80 + "\n")


def roll_dice(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def list_to_str(s):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))


def actionPhaseOrder_to_string(actionPhaseOrder_list: list) -> str:
    str_builder: StringBuilder = StringBuilder()
    for char in actionPhaseOrder_list:
        str_builder.append(" | " + char.name)
    str_builder.append(" | ")
    return str_builder.to_string()
