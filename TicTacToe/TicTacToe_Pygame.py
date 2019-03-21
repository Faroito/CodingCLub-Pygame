#/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

def draw_board(window, board, win):
    text_turn = font.render(turn + " turn!", 3, (255, 255, 255))
    text_win = font.render(win, 3, (255, 255, 255))
    window.fill([127, 114, 100])
    window.blit(background, (0, 0))
    window.blit(text_turn, (20, 630))
    window.blit(text_win, (300, 630))
    for y in range(0, 3):
        for x in range(0, 3):
            if board[y][x] == 'x':
                window.blit(cross, (x * 200 + 50, y * 200 + 50))
            elif board[y][x] == 'o':
                window.blit(round, (x * 200 + 50, y * 200 + 50))
    pygame.display.update()

def ask_position(board, turn):
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pos_x = int(mouse_x / 200)
        pos_y = int(mouse_y / 200)
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

pygame.init()

font = pygame.font.SysFont("arial", 32)
background = pygame.image.load("Image/Background.png")
cross = pygame.image.load("Image/Cross.png")
round = pygame.image.load("Image/Round.png")

width = 600
height = 700
leave = False
turn = "Player1"
win = ""
board = [[' '] * 3 for _ in range(0, 3)]
end = False

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mon super TicTacTO")

while not leave:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
    if not end:
        turn = ask_position(board, turn)
    draw_board(window, board, win)
    end = end_game(board)
    if end:
        if turn == "Player1":
            win = "Player 2 won !"
        else:
            win = "Player 1 won !"


pygame.quit()
quit()
