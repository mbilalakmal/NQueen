# NQueen

NQueen is a python module for solving the famous [N-Queen problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle).


## Installation

Copy the `nqueen.py` file to your project directory. NQueen is a single file namespace module so no setup is required.


## Usage

```python
import nqueen

size = 8 # size of the board
board = nqueen.Board(size) # creates a [size*size] board

is_solved = nqueen.place_queen(board) # returns True if solved.
if is_solved == True:
    board.describe() # prints the board to console
```


## Authors
* Muhammad Bilal Akmal


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgments
* [Abdul Bari](https://www.youtube.com/watch?v=xFv_Hl4B83A)
