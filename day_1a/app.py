def main():
    input = open("./input.txt", "r").read()
    inventories = [[int(calories) for calories in groups.splitlines()] for groups in input.split('\n\n')]
    calories_per_inventories = [sum(calories) for calories in inventories]
    print(max(calories_per_inventories))

if __name__ == '__main__':
    main()