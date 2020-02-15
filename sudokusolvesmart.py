import copy,sys,os

solutions = []
sector_map = [(0, 3, 0, 3), (3, 6, 0, 3), (6, 9, 0, 3), (0, 3, 3, 6), (3, 6, 3, 6), (6, 9, 3, 6), (0, 3, 6, 9),
              (3, 6, 6, 9), (6, 9, 6, 9)]
backtrace = 0


def parse_file(file):
    grid = [[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9]
    with open(file) as f:
        for line_num,line in enumerate(f):
            for item_num,item in enumerate(line):
                if item.isdigit():
                    grid[line_num][item_num] = int(item)
    return grid

def check_valid(grid,y,x,n):
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid [i][x] == n:
            return False

    block_start_x, block_start_y = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[block_start_y+i][block_start_x+j] == n:
                return False
    return True

def resolve_implications(grid):
    global sector_map

    sectors = []
    implications = []
    possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    temp_grid = [[possible_values.copy() for y in range(9)] for x in range(9)]

    # build set of used values in each sector
    for sector in sector_map:
        sector_values = set()
        for y in range(sector[2],sector[3]):
            for x in range(sector[0],sector[1]):
                if grid[y][x] != 0:
                    sector_values.add(grid[y][x])
        sectors.append(sector_values.copy())

    # loop each cell
    for y in range(9):
        for x in range(9):
            if grid[y][x] != 0:
                temp_grid[y][x] = None
            else:
                # figure out which sector this cell is
                this_sector = -1
                for sector in sector_map:
                    if sector[0] <= x < sector[1] and sector[2] <= y < sector[3]:
                        this_sector = sector_map.index(sector)

                # find all values used in this row
                row_values = {i for i in grid[y]}
                # find all values used in this column
                col_values = {i[x] for i in grid}
                # Subtract values used in rows and columns and sector from this cell's options
                i = temp_grid[y][x] - sectors[this_sector] - row_values - col_values
                # if that is only one item (not None) then save it and move on
                if i and len(i) == 1:
                    implications.append((y, x, i))
                    grid[y][x] = i.pop()

    if len(implications) > 0:
        implications += resolve_implications(grid)

    return implications

def reset_implication(grid,implications):
    for i in implications:
        grid[i[0]][i[1]] = 0

def solve(grid,solution_count):
    global backtrace
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if check_valid(grid,y,x,n) and len(solutions)<solution_count:
                        impl = resolve_implications(grid)
                        grid[y][x] = n
                        if solve(grid,solution_count):
                            return True
                        reset_implication(grid,impl)
                        grid[y][x] = 0
                        backtrace += 1
                return False

    solutions.append((copy.deepcopy(grid),backtrace))

def print_grid(grid):
    line_num = 0
    for line in grid:
        p_line = '| '
        char_num = 0
        for char in line:
            p_line += str(char) + ' '
            char_num += 1
            if char_num % 3 == 0:
                p_line += '| '
        if line_num % 3 == 0:
            print('|───────+───────+───────|')
        print(p_line)
        line_num += 1
    print('|───────+───────+───────|')

def main():
    path_to_dir = sys.argv[1]
    for file in os.listdir(path_to_dir):
        grid = parse_file(path_to_dir + file)
        try:
            solve_depth = int(sys.argv[2])
        except IndexError:
            solve_depth = 1

        print('Input:', path_to_dir + file)

        solve(grid,solve_depth)
        for i in solutions:
            print('Solution #', solutions.index(i)+1, 'Backtraces: ',i[1])
            print_grid(i[0])
        print('Stopped looking at',solve_depth,'solution(s).')

        print('')
    print('Done.')

if __name__ == "__main__":
    main()


