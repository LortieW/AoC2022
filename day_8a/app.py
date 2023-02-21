def main():
    grid = []
    n = 0
    with open("./input.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            n = len(line)
            for h in line:
                grid.append(int(h))
    rows = [[grid[i * n + j] for j in range(n)] for i in range(n)]
    rows_lw, rows_rw = parse(rows), reversed_parse(rows)
    
    cols = [[grid[j * n + i] for j in range(n)] for i in range(n)]
    cols_lw, cols_rw = parse(cols), reversed_parse(cols)
    
    visibles = get_visible(rows_lw, rows_rw, cols_lw, cols_rw)
    print(visibles)
    
def parse(block):
    n = len(block)
    results = [[True for x in range(n)] for y in range(n)]
    for i in range(1, n - 1):
        max_value = block[i][0]
        for j in range(1, n - 1): 
            if block[i][j] <= max_value:
                results[i][j] = False
            max_value = max(block[i][j], max_value)
    return results

def reversed_parse(block):
    n = len(block)
    results = [[True for x in range(n)] for y in range(n)]
    for i in range(1, n - 1):
        max_value = block[i][n - 1]
        for j in reversed(range(1, n - 1)): 
            if block[i][j] <= max_value:
                results[i][j] = False
            max_value = max(block[i][j], max_value)
    return results
    
def get_visible(rows_lw, rows_rw, cols_lw, cols_rw):
    n = len(rows_lw)
    visibles = 0
    for i in range(n):
        for j in range(n):
            if rows_lw[i][j] or rows_rw[i][j] or cols_lw[j][i] or cols_rw[j][i]:
                visibles += 1
    return visibles
    
if __name__ == '__main__':
    main()