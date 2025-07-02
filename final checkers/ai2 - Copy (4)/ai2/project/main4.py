import pygame
import pickle
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from reinforcement.algorithm3 import QLearningAgent

FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers AI")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    agent = QLearningAgent()
    agent.epsilon = 0  # Deterministic policy


    if not agent.q_table:
        print("Q-table is empty. Train the agent first.")
        return

    run = True
    while run:
        clock.tick(FPS)

        # AI's turn (WHITE)
        if game.turn == WHITE:
            state = agent.encode(game.get_board(), WHITE)
            actions = agent.get_valid_actions(game.get_board(), WHITE)
            if actions:
                piece, move = agent.choose_action(state, actions, WHITE)
                if piece and move:
                    if game.select(piece.row, piece.col):
                        game._move(move[0], move[1])

        # Handle user input (RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and game.turn == RED:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        if game.winner():
            print(f"{game.winner()} wins!")
            pygame.time.delay(3000)
            run = False

        elif game.check_no_moves(game.turn):
            print(f"No moves left for {game.turn}. Game over.")
            pygame.time.delay(3000)
            run = False

        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
