def main():
    n = 0
    with open("./input.txt", "r") as f:
        for line in f:
            a, b = tuple(line.split(','))
            a, b = pairs_to_set(a), pairs_to_set(b)
            if a <= b or b <= a:
                n += 1
    print(n)

def pairs_to_set(element: list[str]) -> set:
    x, y = tuple([int(x) for x in element.split('-')])
    return set([i for i in range(x, y + 1)])

if __name__ == '__main__':
    main()