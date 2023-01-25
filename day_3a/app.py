def main():
    input = open("./input.txt", "r").read()
    rucksacks = input.splitlines()
    priorities = 0
    for rucksack in rucksacks:
        a, b = get_compartments(rucksack)
        for c in a:
            if c in b:
                priorities += get_priority(c)
                break
    print(priorities)
        
def get_priority(character: str) -> int:
    ascii_value = ord(character)
    return ascii_value - 96 if character.islower() else ascii_value - 38

def get_compartments(rucksack):
    half_length =  int(len(rucksack) // 2)
    return set(rucksack[:half_length]), set(rucksack[-half_length:])

if __name__ == '__main__':
    main()