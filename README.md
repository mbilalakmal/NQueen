# NQueen

NQueen is a python module for solving the famous [N-Queen problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle).


## Installation

Copy the `queen.py` file to your project directory. NQueen is a single file namespace module so no setup is required.
To install dependencies(numpy) from `requirements.txt` run ```pip install -r requirements.txt```.


## Usage

```python
import queen

size = 8 # size of the board
board = queen.Board(size) # creates a [size*size] board

is_solved = queen.place_queen(board) # returns True if solved.
if is_solved == True:
    board.describe() # prints the board to console
```


## Authors
* Muhammad Bilal Akmal


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgments
* [Abdul Bari](https://www.youtube.com/watch?v=xFv_Hl4B83A)
