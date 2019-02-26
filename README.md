# battleship
Author: Bob Young
Battleship game written in Python 3 with Tkinter GUI

Play the battleship game vs. the computer taking turns.  The GUI makes playing the game easy.
The player must set up his / her board with their chosen ship placement.  
The placement of ships on the computer's board is randomly generated.

Issues:
1. There is currently no intelligence behind the moves made by the computer.  It is random.  I plan to change this.
2. Test cases will be added to several function calls, and many of these functions will then be refactored, and easily tested.
3. The code will be cleaned up a bit more, according to DRY and OOP principles, and more comments will be added.
4. Upon completing a game, the initalization of a new game needs to be cleaned up, some one time calls are unnecessarily called again.
5. Statistics - wins, losses, ties will be added.  This will be saved to a text file in json format, and imported at the program start.
6. A problem whereby the player can overlap ships on their board must be fixed.  This will begin with adding unit tests, checking the board to ensure that it is valid.
