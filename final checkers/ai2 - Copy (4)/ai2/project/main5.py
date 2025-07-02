import pygame
from checkers.constants import WIDTH, HEIGHT, RED, WHITE
from checkers.game import Game
from reinforcement.algorithm3 import QLearningAgent
from copy import deepcopy

# -------- Alpha-Beta Functions --------
def alpha_beta(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            eval_score, _ = alpha_beta(move, depth - 1, alpha, beta, False, game)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            eval_score, _ = alpha_beta(move, depth - 1, alpha, beta, True, game)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    return moves

# -------- Game Loop --------
FPS = 60
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alpha-Beta (WHITE) vs Q-Learning (RED)")
clock = pygame.time.Clock()

def main():
    game = Game(SCREEN)
    agent = QLearningAgent(alpha=0.5, gamma=0.3)
    agent.load_q_table()  # Ensure qtable.pkl is in the correct path

    run = True
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            _, new_board = alpha_beta(
                game.get_board(), depth=3, alpha=float('-inf'), beta=float('inf'),
                max_player=True, game=game
            )
            game.ai_move(new_board)

        elif game.turn == RED:
            state_key = agent.encode(game.get_board(), RED)
            valid_moves = agent.get_valid_actions(game.get_board(), RED)

            if not valid_moves:
                print("RED (Q Agent) has no valid moves. WHITE wins!")
                run = False
                continue

            piece, move = agent.choose_action(state_key, valid_moves, RED)

            if piece is None or move is None:
                print("RED (Q Agent) failed to select a move.")
                run = False
                continue

            if not game.select(piece.row, piece.col):
                continue
            if not game._move(move[0], move[1]):
                continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if game.winner():
            print(f"{game.winner()} wins!")
            run = False

        if game.check_no_moves(game.turn):
            print(f"No moves left for {game.turn}")
            run = False

        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
