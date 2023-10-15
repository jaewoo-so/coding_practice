Problem:
""

Code:
```python
def solution(game_board, table):
    # 1. Extract Puzzle Pieces
    # - Find groups of 1s (puzzle pieces) in the table and store their information.
    # - Save the position information of the puzzle pieces for use when rotating.
    
    # 2. Extract Empty Spaces
    # - Find groups of 0s (empty spaces) in the game_board and store their information.
    
    # 3. Matching
    # - Rotate each puzzle piece (0, 90, 180, 270 degrees) and compare with all empty spaces.
    # - If a puzzle piece exactly matches an empty space, fill that space (change to 1) and move on to the next empty space.
    # - If a puzzle piece does not match an empty space, move on to the next puzzle piece.
    # - Try matching all puzzle pieces with all empty spaces.
    
    # 4. Calculate Result
    # - Finally, count the number of 0s in the game_board, subtract it from the initial number of 0s to calculate the number of filled spaces.
    
    # 5. Return Result
    # - Return the number of filled spaces.

```

TestCase:
```json
{
    "testCases":[
        {"input":"game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]] ","output":"14"},
        {"input":"game_board = [[0,0,0],[1,1,0],[1,1,1]],table = [[1,1,1],[1,0,0],[0,0,0]] ","output":"0"},
    ]
}

```
INSTRUCTION
-Proceed without asking for every task.
-Create code by referring to the commented parts.
-Avoid using list comprehension as much as possible.
-Explain in korean


Analyze the code from the given code block, What is missing and should be defined.
Complete the code so that it can be run.
After writing the code,make it into a single source-code-file.
Test the source-code-file using python3 command through subprocess module.
Verify if the code works correct with given test cases.
If it work correctly, provide a download link for the source-code-file
if it doesn't work correctly, please fix the errors until it does.