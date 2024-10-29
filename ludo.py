import pygame
import random
import sys

# Inicializar pygane
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0, 0, 255)


# Tamanho da tela e do tabulerio
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15 # Ludo e um jogo com 15x15 (neste exemplo)
SQUARE_SIZE = WIDTH // COLS

# Inicializar tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

# Posicionamento inicial das peças
positions = {
    'player1': [(1, 1)],  # Posição inicial para o player 1
    'player2': [(13, 13)]  # Posição inicial para o player 2
}
current_positions = {'player1': 0, 'player2': 0}

# Variáveis de jogo
dice_roll = 0
current_player = 'player1'

# Desenhar o tabuleiro
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.update()

# Rolar o dado
def roll_dice():
    global dice_roll
    dice_roll = random.randint(1, 6)
    print(f"Dice rolled: {dice_roll}")