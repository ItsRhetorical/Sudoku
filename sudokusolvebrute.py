import numpy,copy,sys

grid = [[0] * 9, # Collapsing this to [[0]*9]*9 will make all the lists point to the same list object
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9]
solutions = []
backtrace = 0

def parse_file(path_to_file):
    global grid
    with open(path_to_file) as f:
        count_lines = 0
        for line in f:
            count_items = 0
            if count_lines > 8:
                return False
            for item in line:
                if item.isdigit():
                    if count_items > 8:
                        return False
                    grid[count_lines][count_items] = int(item)
                    count_items += 1
            count_lines += 1
    return True

def check_valid(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid [i][x] == n:
            return False
    block_start_x = (x // 3) * 3
    block_start_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[block_start_y+i][block_start_x+j] == n:
                return False
    return True

def solve(solution_count):
    global grid,backtrace
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if check_valid(y,x,n) and len(solutions)<solution_count:
                        grid[y][x] = n
                        solve(solution_count)
                        grid[y][x] = 0
                        backtrace += 1
                return False

    solutions.append((copy.deepcopy(grid),backtrace))


def main():
    parse_result = parse_file(sys.argv[1])

    solve_depth = int(sys.argv[2])

    if parse_result:
        print(numpy.matrix(grid))
    else:
        print('Parse Error')

    solve(solve_depth)

    print(len(solutions), ' solutions found!', 'stopped looking at ',solve_depth,' solutions.')

    for i in solutions:
        print('Solution #', solutions.index(i)+1, 'Backtraces: ',i[1])
        print(numpy.matrix(i[0]))
    print('Done.')

if __name__ == "__main__":
    main()


