"""
The program returns the instructions to complete
the Hanoi Tower game.
"""
counter_list = []


def move(from_pole, to_pole):
    print(f"move a disk from {from_pole} to {to_pole}")


def hanoi(disks_num, position_1, position_2, position_3):
    if disks_num == 0:
        pass
    else:
        hanoi(disks_num - 1, position_1, position_3, position_2)
        move(position_1, position_3)
        counter_list.append(1)
        hanoi(disks_num - 1, position_2, position_1, position_3)


def validate_input(msg):
    while True:
        try:
            user_input = int(input(msg))
        except ValueError:
            print("The program only accepts integer numbers.")
        else:
            return user_input


if __name__ == "__main__":
    disks_number = validate_input("Please enter the number of disks: ")
    print(f"Instructions to solve an Hanoi tower with {disks_number} disks: ")
    hanoi(disks_number, 'A', 'B', 'C')
    print(f"Number of moves: {len(counter_list)}")
