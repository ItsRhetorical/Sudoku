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

`sudokusolvesmart.py PathToFolder NumberOfSolutions'`

example: `sudokusolvesmart.py ./input/ 1`

Note: The smart version consumes a whole folder of files to solve.

Note: NumberOfSolutions defaults to 1 and can be left out in the smart solver.

*NumberOfSolutions* is the number of solutions the program will try to find, if they exist.

