import re
def main():
    with open("./input.txt", "r") as f:
        drawing = []
        for line in f:
            if line in ['\n', '\r\n']:
                break
            drawing.append(line[:-1])
        stacks = create_stacks(drawing)
        for line in f:
            size, src, dst = create_procedure(line)
            leading, trailing = stacks[src][:-size], stacks[src][-size:]
            stacks[dst] += trailing[::-1]
            stacks[src] = leading
        print("".join([head[-1] for head in stacks])) # Fugly way of joining list of strings

def create_procedure(raw):
    str_size, str_src, str_dst = tuple(re.findall(r'[\d]+', raw))
    return int(str_size), int(str_src) - 1, int(str_dst) - 1

def create_stacks(raw):
    n = int(raw.pop()[-2])
    m = len(raw)
    stacks = [''] * n
    for i in range(n):
        for j in range(m):
            c = raw[m-j-1][i*4+1]
            if c in [' ']:
                break
            stacks[i] += c
    return stacks

if __name__ == '__main__':
    main()