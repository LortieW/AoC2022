winning_table = {
    1: 3,
    2: 1,
    3: 2
}

def main():
    input = open("./input.txt", "r").read()
    rounds = input.splitlines()
    total_score = 0
    for r in rounds:
        opponent, player = r.split()
        score_opponent = get_shape_score(opponent)
        score_player = get_shape_score(player)
        outcome_score = get_outcome_score(score_opponent, score_player)
        total_score = total_score + outcome_score + score_player
    print(total_score)
    
def get_outcome_score(score_a, score_b) -> int:
    if score_a == score_b:
        return 3
    elif winning_table[score_b] == score_a:
        return 6
    else:
        return 0
    
def get_shape_score(move: str) -> int:
    match move:
        case 'A' | 'X':
            return 1
        case 'B' | 'Y':
            return 2
        case 'C' | 'Z':
            return 3
        case _:
            raise

if __name__ == '__main__':
    main()