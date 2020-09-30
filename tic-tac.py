
import re
#Greet
print('''
                                                        Welcome to Tic Tac Toe Game
                                                                        -By TECH_TEJAS
Select Player:''')
player1=input("For X Enter Your Name: ").capitalize()
player2=input("For O Enter Your Name: ").capitalize()
print()
print('GAME BEGINS!')
print()
count=0
#Designing Board
board={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
def showboard():
	print(f'''
| {board[1]} | {board[2]} | {board[3]} |	| 1 | 2 | 3 |
| {board[4]} | {board[5]} | {board[6]} |	| 4 | 5 | 6 |
| {board[7]} | {board[8]} | {board[9]} |	| 7 | 8 | 9 |
''')

#Createing Players
def player_1():
	global count
	try:
		inp_player1=int(input(f"{player1}'s Turn: "))
		if board[inp_player1]=='_':
			board[inp_player1]='X'
			count=count+1
			return showboard()
		else:
			print(f"{player1} can't overwrite!")
			return player_1()
	except:
		print("!!!Invalid Input!!!")
		return player_1()
def player_2():
	global count
	try:
		inp_player2=int(input(f"{player2}'s Turn: "))
		if board[inp_player2]=='_':
			board[inp_player2]='O'
			#count=count+1
			return showboard()
		else:
			print(f"{player2} can't overwrite!")
			return player_2()
	except:
		print("!!!Invalid Input!!!")
		return player_2()
#Winner Decider
def decider():
	if count==9:
		print('!TIE!')
		restart()
	elif count!=9:
#For X
		if board[1]==board[2]==board[3]=='X': #Row 1
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[4]==board[5]==board[6]=='X': #Row 2
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[7]==board[8]==board[9]=='X': #Row 3
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[1]==board[4]==board[7]=='X': #Coloumn 1
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[2]==board[5]==board[8]=='X': #Coloumn 2
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[3]==board[6]==board[9]=='X': #Coloumn 3
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[1]==board[5]==board[9]=='X': #Diagonal 1
			print(f"!!!{player1} Won!!!")
			restart()
		elif board[3]==board[5]==board[7]=='X': #Diagonal 2
			print(f"!!!{player1} Won!!!")
			restart()
#For O
		if board[1]==board[2]==board[3]=='O': #Row 1
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[4]==board[5]==board[6]=='O': #Row 2
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[7]==board[8]==board[9]=='O': #Row 3
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[1]==board[4]==board[7]=='O': #Coloumn 1
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[2]==board[5]==board[8]=='O': #Coloumn 2
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[3]==board[6]==board[9]=='O': #Coloumn 3
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[1]==board[5]==board[9]=='O': #Diagonal 1
			print(f"!!!{player2} Won!!!")
			restart()
		elif board[3]==board[5]==board[7]=='O': #Diagonal 2
			print(f"!!!{player2} Won!!!")
			restart()
		else:
			pass

#Starting The Game
def play():
	showboard()
	while True:
		player_1()
		decider()
		player_2()
# For restarting the game if user wish to play again 
def restart():
	inpusr=input(" Enter E To Exit: ")
	inpusr=inpusr.upper()
	if not re.match("^[E]*$",inpusr):
		print("!!!Invalid Input!!!")
		return restart()
	elif inpusr=='E':
		exit()
	else:
		exit()
play()
