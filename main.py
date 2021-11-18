import pygame
from checkers import board
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import board

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    Board = board()
    


    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get.pos()
            row, col = get_row_col_from_mois==use(pos)
            piece = board.get.piese(row, col)
            board.move(piece, (4, 3)
        
    board.pygame.sprite.draw(surface, bgd=None)(WIN)
    pygame.display.update()
                
pygame.quit()

main()