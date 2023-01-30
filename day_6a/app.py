def main():
    with open("./input.txt", "r") as f:
        marker = ""
        index = 0
        for line in f:
            for character in line:
                i = marker.find(character)
                if i >= 0:
                    marker = marker[i+1:]
                marker += character
                index += 1
                if len(marker) == 4:
                    break
        print(index)

if __name__ == '__main__':
    main()