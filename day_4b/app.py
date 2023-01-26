def main():
    overlaps = 0
    with open("./input.txt", "r") as f:
        for line in f:
            a, b = tuple(line.split(',')) # tuple of string pairs
            a, b = pairs_to_set(a), pairs_to_set(b)
            if any(element in b for element in a):
                overlaps += 1
    print(overlaps)

def pairs_to_set(element: list[str]) -> set:
    x, y = tuple([int(x) for x in element.split('-')])
    return set([i for i in range(x, y + 1)])

if __name__ == '__main__':
    main()