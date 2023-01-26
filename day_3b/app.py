from itertools import islice
def main():
    total_priority = 0
    with open("./input.txt", "r") as f:
        for head_line in f:
            elf_A, elf_B, elf_C = set(head_line[:-1]), set(next(f)[:-1]), set(next(f)[:-1])
            for item in elf_A:
                if item in elf_B and item in elf_C:
                    total_priority += get_priority(item)
                    break
    print(total_priority)
               
def get_priority(item: str) -> int:
    ascii_value = ord(item)
    return ascii_value - 96 if item.islower() else ascii_value - 38

if __name__ == '__main__':
    main()
