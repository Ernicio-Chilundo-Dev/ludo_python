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