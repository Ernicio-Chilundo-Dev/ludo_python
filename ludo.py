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


# Mover peça
def move_piece(player):
    global current_positions
    new_position = current_positions[player] + dice_roll
    if new_position >= len(positions[player]):  # Se chegar ao fim do tabuleiro
        print(f"{player} wins!")
        pygame.quit()
        sys.exit()
    current_positions[player] = new_position

# Desenhar as peças
def draw_pieces():
    for player, pos_list in positions.items():
        for pos in pos_list:
            row, col = pos
            color = RED if player == 'player1' else BLUE
            pygame.draw.circle(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)

# Alternar jogadores
def switch_player():
    global current_player
    current_player = 'player1' if current_player == 'player2' else 'player2'

# Loop principal do jogo
running = True
while running:
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Rola o dado ao apertar a tecla ESPAÇO
                roll_dice()
                move_piece(current_player)
                switch_player()

    pygame.display.flip()
    