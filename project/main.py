import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE, ROWS, COLS
from chess.board import Board
from chess.piece import Piece

FPS = 60

IMGS = {}

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('5d Chess')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    pieces = Piece(ROWS, COLS)

    pieces.loadImages()


    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(WIN)
        pieces.drawPieces(WIN, board.board, )
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()



