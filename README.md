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

The file extension doesn't matter.

The output will display each found solution as well as the number ok "backtracks" taken (number of incorrect guesses made).
