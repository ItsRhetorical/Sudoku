# Sudoku
Solves Sudoku!

### sudokusolvebrute.py 
Solves using a brute force recursion. Guessing at every cell and backtracking if it finds a cell with no viable solution.

Command line inputs:

`sudokusolvebrute.py PathToFile NumberOfSolutions'`

example: `sudokusolvebrute.py ./input/hard.txt 1`


### sudokusolvesmart.py
Solves bye looking at "first order" obvious implications. When there is only one possible answer for a particurlar cell because all other numbers are not possible for that cell.

When it exhausts this pattern then it reverts to doing a guess and backtrack pattern.

Command line inputs:

`sudokusolvesmart.py PathToFolder NumberOfSolutions'`

example: `sudokusolvesmart.py ./input/ 1`

Note: The smart version consumes a whole folder of files to solve.

Note: NumberOfSolutions defaults to 1 and can be left out in the smart solver.

*NumberOfSolutions* is the number of solutions the program will try to find, if they exist.


The input files should contain a 9x9 grid of numbers with 0's for the missing digits.

Example:
The file `/inputs/diff` has the contents:
```
005300000
800000020
070010500
400005300
010070006
003200080
060500009
004000030
000009700
```

Produces the result:

```
Input: .\input\diff
Solution # 1 Backtraces:  8
|───────+───────+───────|
| 5 1 7 | 6 9 8 | 2 3 4 |
| 2 8 9 | 1 3 4 | 7 5 6 |
| 3 4 6 | 2 7 5 | 8 9 1 |
|───────+───────+───────|
| 6 7 2 | 8 4 9 | 3 1 5 |
| 1 3 8 | 5 2 6 | 9 4 7 |
| 9 5 4 | 7 1 3 | 6 8 2 |
|───────+───────+───────|
| 4 9 5 | 3 6 2 | 1 7 8 |
| 7 2 3 | 4 8 1 | 5 6 9 |
| 8 6 1 | 9 5 7 | 4 2 3 |
|───────+───────+───────|
Stopped looking at 1 solution(s).
```

The file extension doesn't matter.

The output will display each found solution as well as the number ok "backtracks" taken (number of incorrect guesses made).
