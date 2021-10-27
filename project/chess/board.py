import pygame
from .constants import BAIGE, ROWS, BROWN, BLACK, WHITE, SQUARE_SIZE

class Board:
    def __init__(self):
        # Board is an 8x8 2d list, each element of the list has 2 characters.
        # First character represents color of piece, Second character represents type of piece
        # K King, Q Queen, R Rook, B Bishop, N kNight (K already taken by King), P Pawn
        # "--" represents an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", ],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp", ],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", ]]
        self.whiteToMove = True
        self.moveLog = []
        
        self.selected_piece = None
        self.black_left = self.white_left = 16
        
    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BAIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass
