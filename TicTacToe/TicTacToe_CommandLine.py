#/usr/bin/env python3
# -*- coding: utf-8 -*-

def draw_board(board):
    for line in board:
        print(line)

def ask_position(board, turn):
    print(turn + " turn :")
    pos_x = int(input("Please enter x position: "))
    pos_y = int(input("Please enter y position: "))
    if turn == "Player1" and board[pos_y][pos_x] == ' ':
        board[pos_y][pos_x] = 'x'
        turn = "Player2"
    elif turn == "Player2" and board[pos_y][pos_x] == ' ':
        board[pos_y][pos_x] = 'o'
        turn = "Player1"
    return turn

def end_game(board):
    for p in ['x', 'o']:
        if board[0][0] == p and board[0][1] == p and board[0][2] == p:
            return True
        if board[1][0] == p and board[1][1] == p and board[1][2] == p:
            return True
        if board[2][0] == p and board[2][1] == p and board[2][2] == p:
            return True
        if board[0][0] == p and board[1][0] == p and board[2][0] == p:
            return True
        if board[0][1] == p and board[1][1] == p and board[2][1] == p:
            return True
        if board[0][2] == p and board[1][2] == p and board[2][2] == p:
            return True
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            return True
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            return True
    return False


turn = "Player1"
board = [[' '] * 3 for _ in range(0, 3)]
end = False

while not end:
    draw_board(board)
    turn = ask_position(board, turn)
    end = end_game(board)

if turn == "Player1":
    print("Player 2 won !")
else:
    print("Player 1 won !")
