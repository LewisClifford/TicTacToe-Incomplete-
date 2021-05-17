#import libraries
import random

#Tic Tac Toe Board
line1 = ['.','.','.']
line2 = ['.','.','.']
line3 = ['.','.','.']

board = [line1,line2,line3]

#count
MP1turn = 0
SP1turn = 0
Bturn = 0


#Mode
mode = input("Singleplayer or Multiplayer \n") #Asks how many players are gonna play
if mode == "Multiplayer":
	MP1 = input("Enter P1 name! \n")
	MP2 = input("Enter P2 name! \n")
	print("\n", "The names are:",MP1, "which is X", "and", MP2, "which is O")
	#Multiplayer Game
	while True:
		#1 Player
		print("\n", board[0], "\n", board[1], "\n", board[2])
		print("\n", MP1 , "turn! \n")
		MP1L = input("Enter a line \n")
		MP1C = input("Enter a column \n")
		if MP1L == "1":
			if MP1C == "1":
				if line1[0] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line1[0] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "1":
			if MP1C == "2":
				if line1[1] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line1[1] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "1":
			if MP1C == "3":
				if line1[2] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line1[2] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "2":
			if MP1C == "1":
				if line2[0] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line2[0] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "2":
			if MP1C == "2":
				if line2[1] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line2[1] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "2":
			if MP1C == "3":
				if line2[2] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line2[2] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "3":
			if MP1C == "1":
				if line3[0] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line3[0] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "3":
			if MP1C == "2":
				if line3[1] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line3[1] = "X"
					MP1turn = MP1turn + 1
		if MP1L == "3":
			if MP1C == "3":
				if line3[2] == "0":
					print("Choose another spot")
					MP1L = input("Enter a line \n")
					MP1C = input("Enter a column \n")
				else:
					line3[2] = "X"
					MP1turn = MP1turn + 1
		#Win
		#Row Win
		if line1[0] == line1[1] == line1[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if line2[0] == line2[1] == line2[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if line3[0] == line3[1] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		#Straight Win
		if line1[0] == line2[0] == line3[0] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if line1[1] == line2[1] == line3[1] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if line1[2] == line2[2] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		#Diagonal Win
		if line1[0] == line2[1] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if line1[2] == line2[1] == line3[0] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP1,"has won")
			break
		if MP1turn == 5:
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n It's a Tie!")
			break
		#2 Player
		print("\n", board[0], "\n", board[1], "\n", board[2])
		print("\n", MP2 , "turn! \n")
		MP2L = input("Enter a line \n")
		MP2C = input("Enter a column \n")
		if MP2L >= "4":
			print("No line/column 4 or more!")
			MP2L = input("Enter a line \n")
			MP2C = input("Enter a column \n")
		if MP2L == "1":
			if MP2C == "1":
				if line1[0] == "X":
					print("Already filled, Pick another")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line1[0] = "O"

		if MP2L == "1":
			if MP2C == "2":
				if line1[1] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line1[1] = "0"

		if MP2L == "1":
			if MP2C == "3":
				if line1[2] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line1[2] = "0"

		if MP2L == "2":
			if MP2C == "1":
				if line2[0] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line2[0] = "0"

		if MP2L == "2":
			if MP2C == "2":
				if line2[1] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line2[1] = "0"

		if MP2L == "2":
			if MP2C == "3":
				if line2[2] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line2[2] = "0"

		if MP2L == "3":
			if MP2C == "1":
				if line3[0] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line3[0] = "0"
			if MP2L == "3":
				if MP2C == "2":
					if line3[1] == "X":
						print("Choose another spot")
						MP2L = input("Enter a line \n")
						MP2C = input("Enter a column \n")
					else:
						line3[1] = "0"
					
		if MP2L == "3":
			if MP2C == "3":
				if line3[2] == "X":
					print("Choose another spot")
					MP2L = input("Enter a line \n")
					MP2C = input("Enter a column \n")
				else:
					line3[2] = "0"
		#Win
		#Row Win
		if line1[0] == line1[1] == line1[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		if line2[0] == line2[1] == line2[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		if line3[0] == line3[1] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		#Straight Win
		if line1[0] == line2[0] == line3[0] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		if line1[1] == line2[1] == line3[1] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		if line1[2] == line2[2] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", MP2,"has won")
			break
		#Diagonal Win
		if line1[0] == line2[1] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n",MP2,"has won")
			break
		if line1[2] == line2[1] == line3[0] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n",MP2,"has won")
			break

elif mode == "Singleplayer":
	SP1 = input("Enter P1 name! \n")
	print("The name that is playing is:", SP1, "which is X")

	#SinglePlayer
	while True:
		#Player
		print("\n", board[0], "\n", board[1], "\n", board[2])
		print("\n", SP1 , "turn! \n")
		SP1L = input("Enter a line \n")
		SP1C = input("Enter a column \n")
		if SP1L == "1":
			if SP1C == "1":
				if line1[0] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line1[0] = "X"
		if SP1L == "1":
			if SP1C == "2":
				if line1[1] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line1[1] = "X"
		if SP1L == "1":
			if SP1C == "3":
				if line1[2] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line1[2] = "X"
		if SP1L == "2":
			if SP1C == "1":
				if line2[0] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line2[0] = "X"
		if SP1L == "2":
			if SP1C == "2":
				if line2[1] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line2[1] = "X"
		if SP1L == "2":
			if SP1C == "3":
				if line2[2] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line")
					SP1C = input("Enter a column")
				else:
					line2[2] = "X"
		if SP1L == "3":
			if SP1C == "1":
				if line3[0] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line3[0] = "X"
		if SP1L == "3":
			if SP1C == "2":
				if line3[1] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line3[1] = "X"
		if SP1L == "3":
			if SP1C == "3":
				if line3[2] == "0":
					print("Choose another spot")
					SP1L = input("Enter a line \n")
					SP1C = input("Enter a column \n")
				else:
					line3[2] = "X"
		#Win
		#Row Win
		if line1[0] == line1[1] == line1[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if line2[0] == line2[1] == line2[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if line3[0] == line3[1] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		#Straight Win
		if line1[0] == line2[0] == line3[0] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if line1[1] == line2[1] == line3[1] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if line1[2] == line2[2] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		#Diagonal Win
		if line1[0] == line2[1] == line3[2] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if line1[2] == line2[1] == line3[0] == "X":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n", SP1,"has won")
			break
		if SP1turn == 5:
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("\n It's a Tie!")
			break
		#Bot
		print("\n", board[0], "\n", board[1], "\n", board[2])
		print("\n", "Bot turn! \n")
		BL = random.randint(1,3)
		print(BL)
		BC = random.randint(1,3)
		print(BC)
		if BL == 1:
			if BC == 1:
				if line1[0] == "X":
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line1[0] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line1[0] = "O"
		if BL == 1:
			if BC == 2:
				if line1[1] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line1[1] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line1[1] = "0"
		if BL == 1:
			if BC == 3:
				if line1[2] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line1[2] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line1[2] = "0"
		if BL == 2:
			if BC == 1:
				if line2[0] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line2[0] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line2[0] = "0"
		if BL == 2:
				if BC == 2:
					if line2[1] == "X":
						print("Choose another spot")
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
						if line2[1] == "0":
							BL = random.randint(1, 3)
							print(BL)
							BC = random.randint(1, 3)
							print(BC)
							continue
					else:
						line2[1] = "0"
		if BL == 2:
			if BC == 3:
				if line2[2] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line2[2] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line2[2] = "0"
		if BL == 3:
			if BC == 1:
				if line3[0] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line3[0] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line3[0] = "0"
		if BL == 3:
			if BC == 2:
				if line3[1] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line3[1] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line3[1] = "0"
		if BL == 3:
			if BC == 3:
				if line3[2] == "X":
					print("Choose another spot")
					BL = random.randint(1,3)
					print(BL)
					BC = random.randint(1,3)
					print(BC)
					continue
					if line3[2] == "0":
						BL = random.randint(1,3)
						print(BL)
						BC = random.randint(1,3)
						print(BC)
						continue
				else:
					line3[2] = "0"
		#Win
		#Row Win
		if line1[0] == line1[1] == line1[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		if line2[0] == line2[1] == line2[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		if line3[0] == line3[1] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		#Straight Win
		if line1[0] == line2[0] == line3[0] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		if line1[1] == line2[1] == line3[1] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		if line1[2] == line2[2] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		#Diagonal Win
		if line1[0] == line2[1] == line3[2] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break
		if line1[2] == line2[1] == line3[0] == "0":
			print("\n", board[0], "\n", board[1], "\n", board[2])
			print("Bot has won")
			break