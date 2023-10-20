  import random
import sys
import time
import copy

coin_flip = random.randint(0,1)
if coin_flip == 0:
  print("The coin flip has decided that player X will go first")
else:
  print("The coin flip has decided that player O will go first")

board_list = []

for i in range(3):
  row_list = []
  for i in range(3):
    row_list.append(" ")
  board_list.append(row_list)

def print_full_board(board_list):
  print_board = f" {board_list[0][0]} | {board_list[0][1]} | {board_list[0][2]} \n --+---+---\n {board_list[1][0]} | {board_list[1][1]} | {board_list[1][2]} \n --+---+--- \n {board_list[2][0]} | {board_list[2][1]} | {board_list[2][2]}"
  print(print_board)
  


def user_turn(board_list):
  print("\033c",end="")
  print_full_board(board_list)
  row = int(input("row to add X: "))
  column = int(input("column to add X: "))
  if row > 2 or column > 2:
    print("Please enter numbers between 0-2\nTry Again")
    time.sleep(1.75)
    return user_turn(board_list)
  elif board_list[row][column] == " ":
    board_list[row][column] = "X"
    return board_list
  else: 
    print("That spot is aready occupied\nTry Again")
    time.sleep(1.75)
    return user_turn(board_list)
    
def random_computer_turn(board_list):
  row = random.randint(0,2)
  column = random.randint(0,2)
  if board_list[row][column] == " ":
    board_list[row][column] = "O"
  else: 
    random_computer_turn(board_list)
  return board_list

def win_check(board_list, x):
  if board_list[0][0] == x and board_list[0][1] == x and board_list[0][2] == x:
    return True
  elif board_list[1][0] == x and board_list[1][1] == x and board_list[1][2] == x:
    return True
  elif board_list[2][0] == x and board_list[2][1] == x and board_list[2][2] == x:
    return True
  elif board_list[0][0] == x and board_list[1][0] == x and board_list[2][0] == x:
    return True
  elif board_list[0][1] == x and board_list[1][1] == x and board_list[2][1] == x:
    return True
  elif board_list[0][2] == x and board_list[1][2] == x and board_list[2][2] == x:
    return True
  elif board_list[0][0] == x and board_list[1][1] == x and board_list[2][2] == x:
    return True
  elif board_list[0][2] == x and board_list[1][1] == x and board_list[2][0] == x:
    return True
  # checking for tie
  
def new_win_check(board_list, x):
  double_wins = 0
  if board_list[0][0] == x and board_list[0][1] == x and board_list[0][2] == x:
    double_wins += 1
  if board_list[1][0] == x and board_list[1][1] == x and board_list[1][2] == x:
    double_wins += 1
  if board_list[2][0] == x and board_list[2][1] == x and board_list[2][2] == x:
    double_wins += 1
  if board_list[0][0] == x and board_list[1][0] == x and board_list[2][0] == x:
    double_wins += 1
  if board_list[0][1] == x and board_list[1][1] == x and board_list[2][1] == x:
    double_wins += 1
  if board_list[0][2] == x and board_list[1][2] == x and board_list[2][2] == x:
    double_wins += 1
  if board_list[0][0] == x and board_list[1][1] == x and board_list[2][2] == x:
    double_wins += 1
  if board_list[0][2] == x and board_list[1][1] == x and board_list[2][0] == x:
    double_wins += 1
  return double_wins  

def computer_win_check(board_list):
  fake_board = copy.deepcopy(board_list)
  for i in range(len(fake_board)):
    for a in range(len(fake_board[i])):
      if fake_board[i][a] == " ":
        fake_board[i][a] = "O"
        if win_check(fake_board, "O") == True:
          board_list[i][a] = "O"
          return board_list
      fake_board = copy.deepcopy(board_list)  
  for i in range(len(fake_board)):
    for a in range(len(fake_board[i])):
      if fake_board[i][a] == " ":
        fake_board[i][a] = "X"
        if win_check(fake_board, "X") == True:
          board_list[i][a] = "O"
          return board_list
      fake_board = copy.deepcopy(board_list)
  ###########################
  for i in range(len(fake_board)):
    for a in range(len(fake_board[i])):
      if fake_board[i][a] == " ":
        fake_board[i][a] = "X"
        fake_fake_board = copy.deepcopy(fake_board)
        double_wins = 0
        for b in range(len(fake_board)):
          for z in range(len(fake_board[b])):
            if fake_fake_board[b][z] == " ":
              fake_fake_board[b][z] = "X"
            if new_win_check(fake_fake_board, "X") == 1:
              double_wins += 1
            fake_fake_board = copy.deepcopy(fake_board)
        if double_wins >= 2:
          board_list[i][a] = "O"
          print("stop the fork")
          time.sleep(2)
          return board_list
      fake_board = copy.deepcopy(board_list)
  ###########################
  for i in range(len(fake_board)):
    for a in range(len(fake_board[i])):
      if fake_board[i][a] == " ":
        fake_board[i][a] = "O"
        fake_fake_board = copy.deepcopy(fake_board)
        double_wins = 0
        for b in range(len(fake_board)):
          for z in range(len(fake_board[b])):
            if fake_fake_board[b][z] == " ":
              fake_fake_board[b][z] = "O"
            if new_win_check(fake_fake_board, "O") == 1:
              double_wins += 1
            fake_fake_board = copy.deepcopy(fake_board)
        if double_wins >= 2:
          board_list[i][a] = "O"
          print("make the fork")
          time.sleep(2)
          return board_list
      fake_board = copy.deepcopy(board_list)
  ###########################
  if board_list[1][1] == " ":
    board_list[1][1] = "O"
    return board_list
  ###########################
  open_corner = []    
  if board_list[0][2] == " ":
    open_corner.append([0,2]) 
  if board_list[0][0] == " ":
    open_corner.append([0,0])
  if board_list[2][0] == " ":
    open_corner.append([2,0])
  if board_list[2][2] == " ":
    open_corner.append([2,2])
  if len(open_corner) != 0:  
    temp = open_corner[random.randint(0,len(open_corner)-1)]
    board_list[temp[0]][temp[1]] = "O"
    return board_list
  ###########################
  open_side = []
  if board_list[0][1] == " ":
    open_side.append([0,1])
  if board_list[1][2] == " ":
    open_side.append([1,2])
  if board_list[2][1] == " ":
    open_side.append([2,1])
  if board_list[1][0] == " ":
    open_side.append([1,0])
  if len(open_side) != 0:  
    temp = open_side[random.randint(0,len(open_side)-1)]
    board_list[temp[0]][temp[1]] = "O"
    return board_list
  ###########################
  print("Random")

while True:
  print_full_board(board_list)
  if coin_flip == 0:
    board_list = user_turn(board_list)
    if win_check(board_list, "X") == True:
      time.sleep(1)
      print_full_board(board_list)
      print("Player X won!")
      sys.exit()
    coin_flip += 1
  else:
    board_list = computer_win_check(board_list)
    coin_flip -= 1
    if win_check(board_list, "O") == True:
      print_full_board(board_list)
      print("Player O won!")
      sys.exit()
  num_spaces = 0
  for i in board_list:
    for a in i:
      if a == " ":
        num_spaces += 1
  if num_spaces == 0:
    print_full_board(board_list)
    print("There was a tie!")
    sys.exit()
  
  

    
    










