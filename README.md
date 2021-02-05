# Puzzle game
Check if game board n\*n is *ready to game*

Game board should meets the following *rules*:
* colored cells in each *row* should contains numbers from 1 to n without repetitions
* colored cells in each *column* should contains numbers from 1 to n without repetitions
* colored cells in *area* of each color should contains numbers from 1 to n without repetitions

*Example* of ready game board:
```
**** ****
***1 ****
**  3****
* 4  ****
     9 5 
 6  83  *
3   1  **
  8  2***
  2  ****
```

*Using* program

To use this program you should run function *validate_board* with game board as list of strings
