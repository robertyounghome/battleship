import random
from tkinter import *
from tkinter import font
from tkinter import messagebox
from functools import partial

class Player:
	def __init__(self, name, text = ''):
		self.name = name
		self.text = text
		self.wins = 0
		self.losses = 0
		self.ties = 0

	def win(self):
		self.wins += 1

	def loss(self):
		self.losses += 1

	def tie(self):
		self.ties += 1

	def stats(self):
		return [self.wins, self.ties, self.losses]

class Ship:
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.position = {}
		self.sunk = False

class Game:
	def reset(self):
		self.initShips()
		self.sunk = 0
		self.board = [[' ' for _ in range(8)] for _ in range(8)]
		self.valid = []
		for i in range(8):
			for j in range(8):
				self.valid += [[i, j]]
		self.turn = 0
		self.initShipPositions()

	def __init__(self):
		self.reset()
		self.hit = PhotoImage(file="hit.gif").subsample(4, 4)
		self.miss = PhotoImage(file="miss.gif").subsample(4, 4)
		self.blank = PhotoImage(file="blank.gif").subsample(4, 4)

	def initShips(self):
		self.ships = []
		self.ships += [Ship("Carrier", 5)]
		self.ships += [Ship("Battleship", 4)]
		self.ships += [Ship("Submarine", 3)]
		self.ships += [Ship("Cruiser", 3)]
		self.ships += [Ship("Destroyer", 2)]

	# Randomly place the ships on the board.  Searches for a valid location.
	# A valid location is a location where the ship fits completely on the board.
	# Also the ship must be in a location that is not already occupied by another ship
	def initShipPositions(self):
		for currentShip, ship in enumerate(self.ships):
			found = False
			while found == False:
				ship.position = {}
				i = random.randint(0, len(self.valid) - 1)
				t = self.valid[i]
				x = t[0]
				y = t[1]
				# Try to place the ship horizontally or vertically
				# Trying horizontal or vertical placement first is random
				j = random.randint(0, 1)
				for k in range(2):
					count = 1
					x1 = x
					y1 = y
					ship.position = {}
					found = True
					for i in range(ship.size):
						if j % 2 == 0:
							x1 = x + i
						else:
							y1 = y + i
						if [x1, y1] not in self.valid:
							found = False
							break
						# Check to see if a ship already exists in this position
						for foundShips in range(currentShip):
							if (x1, y1) in self.ships[foundShips].position:
								found = False
								break
						if found == False:
							break
						ship.position[(x1, y1)] = 1
					if found == True:
						break
					j += 1
			print(f"{ship.name} is in {ship.position}")

	def printBoard(self):
		for i in range(8):
			print(self.board[i])

	# Check our list of valid remaining moves to see if the move is valid
	def checkMove(self, x, y):
		if [x,y] in self.valid:
			return True
		return False

	# Resets the GUI board
	def boardReset(self):
		for x in range(8):
			for y in range(8):
				game.buttons[x][y].configure(image=self.blank, compound="left")

    # Prompts user in the GUI.  Returns True if the user wants to play again, otherwise False
	def playAgain(self):
		return messagebox.askyesno("Game Over", f"All ships sunk in {game.turn} turns!!  Would you like to play again?")

	def isSunk(self, ship):
		if ship.sunk:
			return True
		for k in ship.position.keys():
			if list(k) in self.valid:
				return False
		ship.sunk = True
		game.sunk += 1
		print(f"{ship.name} was sunk!!")
		if game.sunk == 5:
			if self.playAgain():
				self.reset()
				self.boardReset()
			else:
				root.destroy()
		else:
			messagebox.showinfo("Ship Sunk", f"{ship.name} was sunk!!")
		return True

	def move(self, x, y, s):
		self.board[x][y] = s
		self.valid.pop(self.valid.index([x,y]))
		self.turn += 1
		foundHit = False
		for ship in self.ships:
			if ship.sunk == False and (x, y) in ship.position:
				self.buttons[x][y].configure(image=self.hit, compound="left")
				foundHit = True
				self.isSunk(ship)
				break
		if not foundHit:
			self.buttons[x][y].configure(image=self.miss, compound="left")
		print(self.board)

    # A move was made from our GUI
	def tkmove(self, x, y, player, computer, root):
		print(self.turn, player.text, x, y)	
		if self.checkMove(x, y):
			self.move(x, y, 'X')

if __name__ == '__main__':
	player = Player("Player")
	computer = Player("Computer")
	root = Tk()
	root.title("Bob's Battleship Game")
	game = Game()
	game.buttons = []
	for x in range(8):
		game.buttons += [[]]
		for y in range(8):
			game.buttons[x] += [Button(root, text="", image=game.blank, borderwidth=1, command=partial(game.tkmove, x, y, player, computer, root))]
			game.buttons[x][y].grid(row=x,column=y)
	root.mainloop()
