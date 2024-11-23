from random import randint

N = 8 #number of queens/size of board (8x8)
H = 0 #heuristic value (goal value based on number of queens attacking each other on the board)

#runs program
def run():	
	queenPositions = [0] * N #row positions of queens for each column.
	board = [[0] * N for i in range(N)] #init board

	#starting state
	randomizeBoard(board, queenPositions)

	#print init state
	printBoard(board, 0)
	
	#start algo
	hillClimbingAlgo(board, queenPositions)

#generate new boards
def generateBoard(board, queenPositions):
	for row in board:
		for j in range(N):
			row[j] = 0

	for i in range(N):
		board[queenPositions[i]][i] = 1

#randomizes board for init state
def randomizeBoard(board, queenPositions):
	for i in range(N):
		queenPositions[i] = randint(0, N-1)
		board[queenPositions[i]][i] = 1
	
#check if board has reached global H
def checkIfSolved(position1, position2):
	for i in range(N):
		if (position1[i] != position2[i]):
			return False
	
	return True
		
#gets the heuristic value of the board
def getH(board, queenPositions):
	H = 0 #heuristic value H
	
	# Search left in the current row for a Queen
	for i in range(N):
		row = queenPositions[i]
		col = i - 1
		while col >= 0:
			if board[row][col] == 1:
				H += 1
				break
			col -= 1

		
		# Search right in the current row for a Queen
		row = queenPositions[i]
		col = i + 1
		while col < N:
			if board[row][col] == 1:
				H += 1
				break
			col += 1
		
		# Search diagonally up-left for a Queen
		row = queenPositions[i] - 1
		col = i - 1
		while col >= 0 and row >= 0:
			if board[row][col] == 1:
				H += 1
				break
			col -= 1
			row -= 1
		
		# Search diagonally down-right for a Queen
		row = queenPositions[i] + 1
		col = i + 1
		while col < N and row < N:
			if board[row][col] == 1:
				H += 1
				break
			col += 1
			row += 1
		
		# Search diagonally down-left for a Queen
		row = queenPositions[i] + 1
		col = i - 1
		while col >= 0 and row < N:
			if board[row][col] == 1:
				H += 1
				break
			col -= 1
			row += 1
		
		# Search diagonally up-right for a Queen
		row = queenPositions[i] - 1
		col = i + 1
		while col < N and row >= 0:
			if board[row][col] == 1:
				H += 1
				break
			col += 1
			row -= 1
	
	return int(H / 2)  #return heuristic value H
	
#get neighbor of current state
def getNeighbor(board, queenPositions):

	#init current board as min H
	minBoard = [[0] * N for i in range(N)]
	bestQueenPositions = [0] * N

	#make board and save queen positions
	bestQueenPositions = queenPositions.copy()
	generateBoard(minBoard, bestQueenPositions)

	#calculate heuristic
	H = getH(minBoard, bestQueenPositions)

	#temp board to get H from neighbors
	tempBoard = [[0] * N for i in range(N)]
	tempQueenPositions = [0] * N

	#make board and save queen positions
	tempQueenPositions = queenPositions.copy()
	generateBoard(tempBoard, tempQueenPositions)

	#loop through to find optimal H
	for i in range(N):
		for j in range(N):
			#do not check current state
			if (j != queenPositions[i]) :
				# Move queen's position on board
				tempQueenPositions[i] = j
				tempBoard[j][i] = 1
				tempBoard[queenPositions[i]][i] = 0

				# Calculating H for new position
				temp = getH(tempBoard, tempQueenPositions)

				#check if temp H is smaller than current H
				#if true then update H
				if (temp <= H) :
					H = temp
					bestQueenPositions = tempQueenPositions.copy()
					generateBoard(minBoard, bestQueenPositions)
				
				#reset back to current
				tempBoard[tempQueenPositions[i]][i] = 0
				tempQueenPositions[i] = queenPositions[i]
				tempBoard[queenPositions[i]][i] = 1
			
	#copy board with best H
	for i in range(N):
		queenPositions[i] = bestQueenPositions[i]

	#generate board with best H
	generateBoard(board, queenPositions)

def hillClimbingAlgo(board, queenPositions):

	neighbourQueenPositions = [0] * N #init neighbourQueenPositions
	neighbourBoard = [[0] * N for i in range(N)] #init neighbour of current state
	
	while True:
		queenPositions = neighbourQueenPositions.copy()
		generateBoard(board, queenPositions)

		#find neighbors of current state
		getNeighbor(neighbourBoard, neighbourQueenPositions)

		#State has hit global min
		if (checkIfSolved(queenPositions, neighbourQueenPositions)):
			printBoard(board, 1)
			print("H:", H)
			break	
		#State has hit local min
		#Randomize state to get out of it
		elif (getH(board, queenPositions) == getH( neighbourBoard,neighbourQueenPositions)):
			neighbourQueenPositions[randint(0, N-1)] = randint(0, N-1)
			generateBoard(neighbourBoard, neighbourQueenPositions)

#prints board
def printBoard(board, val):
	
	#if val is 0 then board is not solved
	if (val == 0):
		print("\n")
		print("Unsolved Board")
	#if val is 1 then board is solved
	else:
		print("\n")
		print("Solved Board")

	for i in range(N):
		print(*board[i])

run()
