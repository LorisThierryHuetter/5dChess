import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS

class Piece:
    def __init__(self, row, col):
        self.row = row 
        self.col = col 
        
        self.x = 0
        self.y = 0
    
    def loadImages(self):
        pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
        for piece in pieces:
            IMGS[piece] = pygame.transform.scale(pygame.image.load("imgs/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        pygame.draw.circle()
    
    def drawPieces(board):
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece != "--":
                    WIN.blit(IMGS[piece], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))