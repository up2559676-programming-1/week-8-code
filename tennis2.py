# Lecture 8 - an example of top-down design
from random import random


def get_inputs() -> tuple[float, int]:
    point_win_probability = float(input("Probability of winning each point: "))
    number_of_sets = int(input("Sets to simulate: "))
    return point_win_probability, number_of_sets


def simulate_games(point_win_probability: float) -> tuple[int, int]:
    min_game_wins = 6

    player_wins = 0
    opponent_wins = 0
    while (player_wins < min_game_wins or opponent_wins < min_game_wins) and abs(player_wins - opponent_wins) < 2:
        points_player, points_opponent = simulate_game(point_win_probability)
        if points_player > points_opponent:
            player_wins += 1
        else:
            opponent_wins += 1
    return player_wins, opponent_wins


def simulate_game(point_win_probability: float) -> tuple[int, int]:
    points_player, points_opponent = (0, 0)
    while not game_over(points_player, points_opponent):
        if random() < point_win_probability:
            points_player = points_player + 1
        else:
            points_opponent = points_opponent + 1
    return points_player, points_opponent

def simulate_set(point_win_prob: float) -> bool:
    player_wins, opponent_wins = simulate_games(point_win_prob)
    return player_wins > opponent_wins

def simulate_sets(point_win_prob: float, num_of_sets: int) -> int:
    return sum(simulate_set(point_win_prob) for _ in range(num_of_sets))

def game_over(points_player: int, points_opponent: int) -> bool:
    return (points_player >= 4 or points_opponent >= 4) and \
        abs(points_player - points_opponent) >= 2


def print_summary(wins: int, number_of_sets: int):
    proportion = wins / number_of_sets
    print(f"Wins: {wins}, proportion: {proportion:.2f}")


def main():
    point_win_probability, number_of_sets = get_inputs()
    wins = simulate_sets(point_win_probability, number_of_sets)
    print_summary(wins, number_of_sets)


main()
