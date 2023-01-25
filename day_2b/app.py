winning_table = {
    1: 3,
    2: 1,
    3: 2
}
losing_table = {
    1: 2,
    2: 3,
    3: 1
}
shape_table = {
    'A': 1,
    'B': 2,
    'C': 3
}

def main():
    input = open("./input.txt", "r").read()
    rounds = input.splitlines()
    total_score = 0
    for r in rounds:
        left_column, right_column = r.split()
        total_score += get_round_score(left_column, right_column)
    print(total_score)
    
def get_round_score(shape, outcome) -> int:
    score = shape_table[shape]
    match outcome:
        case 'X': # Opponent needs to win
            return winning_table[score] + 0
        case 'Y': # Draw
            return score + 3
        case 'Z': # Opponent needs to lose
            return losing_table[score] + 6
        case _:
            raise           

if __name__ == '__main__':
    main()