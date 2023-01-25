def main():
    input = open("./input.txt", "r").read()
    inventories = [[int(calories) for calories in groups.splitlines()] for groups in input.split('\n\n')]
    calories_per_inventories = [sum(calories) for calories in inventories]
    top_three = sorted(calories_per_inventories)[-3:]
    print(sum(top_three))

if __name__ == '__main__':
    main()