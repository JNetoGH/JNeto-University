map = [["a", "b", "c"],
       ["d", "e", "f"],
       ["g", "h", "i"]]


def print_map() -> None:
    print("MAP (Collect G, C, I in this order)", end="")
    for i in range(0, len(map)):
        print("\n|", end="")
        for j in range(0, len(map[0])):
            print(f" {map[i][j]}", end=" |")
    print()


class Axis:
    HORIZONTAL: int = 1
    VERTICAL: int = 0


class Player:

    def __init__(self, initial_pos: list[int]):
        self.pos: list[int] = initial_pos
        self.pointsCollected: list = []
        self.won = False
        print("initial ", end="")
        self.print_pos_status()

    def move(self, code) -> None:
        print_map()
        print("You tried to move: " + code)

        is_code_valid = False
        if code == "EAST" and self.pos[Axis.HORIZONTAL] + 1 < len(map[0]):
            self.pos[Axis.HORIZONTAL] += 1
            is_code_valid = True
        elif code == "WEST" and self.pos[1] - 1 >= 0:
            self.pos[Axis.HORIZONTAL] -= 1
            is_code_valid = True
        elif code == "SOUTH" and self.pos[Axis.VERTICAL] + 1 < len(map):
            self.pos[Axis.VERTICAL] += 1
            is_code_valid = True
        elif code == "NORTH" and self.pos[Axis.VERTICAL] - 1 >= 0:
            self.pos[Axis.VERTICAL] -= 1
            is_code_valid = True

        self.update_collectable_winning_condition()

        if not is_code_valid:
            print(f"ERROR: \"{code}\" (passes a boundary or is not valid)")
        self.print_pos_status()

    def print_pos_status(self) -> None:
        print("pos: " + map[self.pos[Axis.VERTICAL]][self.pos[Axis.HORIZONTAL]])
        print(f"current index: [{self.pos[Axis.VERTICAL]}][{self.pos[Axis.HORIZONTAL]}]\n")
        str = ""
        for collected in self.pointsCollected:
            str = str + f", {collected}"
        print(f"collected: {str}")

    def is_there_any_in_collected(self, string:str) -> bool:
        for i in range(0, len(self.pointsCollected)):
            if self.pointsCollected[i] == string:
                return True
        return False

    def update_collectable_winning_condition(self) -> None:
        if self.pos[Axis.VERTICAL] == 2 and self.pos[Axis.HORIZONTAL] == 0 and (not self.is_there_any_in_collected("G")):
            self.pointsCollected.append("G")
        elif self.pos[Axis.VERTICAL] == 0 and self.pos[Axis.HORIZONTAL] == 2 and (not self.is_there_any_in_collected("C")) and self.is_there_any_in_collected("G"):
            self.pointsCollected.append("C")
        elif self.pos[Axis.VERTICAL] == 2 and self.pos[Axis.HORIZONTAL] == 2 and (not self.is_there_any_in_collected("I")) and self.is_there_any_in_collected("C") and self.is_there_any_in_collected("G"):
            self.pointsCollected.append("I")
            self.won = True


print("COMMANDS: quit, north, south, east, west\n")
print_map()
joao = Player([1, 1])  # x, y initial

while not joao.won:
    value = input("choose a direction: ").upper()
    if value == "QUIT":
        break
    print()
    joao.move(value)

print("YOU WIN")