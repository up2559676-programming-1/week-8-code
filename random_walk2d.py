import math
from random import random


def get_inputs() -> tuple[int, int]:
    # Get the number of walks and steps from the user.
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps


def take_a_walk(num_steps: int) -> list[int]:
    # Simulate a single random walk of `num_steps` steps.
    steps_from_start = [0, 0]
    for _ in range(num_steps):
        if random() < 0.25:
            steps_from_start[0] += 1
        elif random() < 0.5:
            steps_from_start[1] += 1
        elif random() < 0.75:
            steps_from_start[0] -= 1
        else:
            steps_from_start[1] -= 1
    return steps_from_start


def take_walks(num_walks: int, num_steps: int) -> tuple[float, float]:
    # Simulate `num_walks` random walks of `num_steps` steps each.
    total_steps = [0, 0]
    for _ in range(num_walks):
        steps_away = take_a_walk(num_steps)
        total_steps[0] += abs(steps_away[0])
        total_steps[1] += abs(steps_away[1])
    return (total_steps[0] / num_walks, total_steps[1] / num_walks)

def distance_from_centre(pos: tuple[float, float]) -> float:
    return math.sqrt(pos[0]**2 + pos[1]**2)

def print_expected_distance(average_steps: float):
    # Print the `average_steps` value.
    print(f"The expected number of steps away from the start point is {average_steps:.2f}")


def main():
    # Main function to execute the random walk simulation.
    num_walks, num_steps = get_inputs()
    steps = take_walks(num_walks, num_steps)
    dist = distance_from_centre(steps)
    print_expected_distance(dist)


main()
