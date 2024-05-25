import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set custom screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

# Set up the screen with custom dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Define the Tic Tac Toe board
board = [['' for _ in range(3)] for _ in range(3)]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the main game loop
def main():
    global board

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // (SCREEN_HEIGHT // 3)
                col = event.pos[0] // (SCREEN_WIDTH // 3)

                if board[row][col] == '':
                    board[row][col] = 'X'
                    if check_winner('X'):
                        print("Player X wins!")
                        running = False
                    elif check_tie():
                        print("It's a tie!")
                        running = False
                    else:
                        computer_move()

        screen.fill(WHITE)

        # Draw Tic Tac Toe grid
        cell_width = SCREEN_WIDTH // 3
        cell_height = SCREEN_HEIGHT // 3
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(screen, BLACK, (col * cell_width, row * cell_height, cell_width, cell_height), 2)
                if board[row][col] == 'X':
                    pygame.draw.line(screen, BLACK, (col * cell_width + 20, row * cell_height + 20), 
                                     ((col + 1) * cell_width - 20, (row + 1) * cell_height - 20), 5)
                    pygame.draw.line(screen, BLACK, ((col + 1) * cell_width - 20, row * cell_height + 20), 
                                     (col * cell_width + 20, (row + 1) * cell_height - 20), 5)
                elif board[row][col] == 'O':
                    pygame.draw.circle(screen, BLACK, (col * cell_width + cell_width // 2, row * cell_height + cell_height // 2), cell_width // 2 - 20, 5)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Check if the given player has won
def check_winner(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the game is a tie
def check_tie():
    return all(board[row][col] != '' for row in range(3) for col in range(3))

# Implement computer move
def computer_move():
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        if check_winner('O'):
            print("Player O wins!")
            return
        elif check_tie():
            print("It's a tie!")
            return

# Start the game
if __name__ == "__main__":
    main()
