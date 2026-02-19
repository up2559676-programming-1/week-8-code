import math
from random import random
import time
from graphix import Window, Line, Point, Circle

def get_inputs() -> tuple[int, int]:
    # Get the number of walks and steps from the user.
    num_walks = int(input("How many random walks to take? "))
    max_dist = int(input("How far from centre should each walk be? "))
    return num_walks, max_dist


def take_a_walk(win: Window, max_dist: int):
    # Simulate a single random walk of `num_steps` steps.
    
    centre = Point(win.width // 2, win.height // 2)
    cursor = centre
    end = cursor
    dist = 0
    while dist < max_dist:
        # North
        if random() < 0.25:
            end = Point(cursor.x, cursor.y - 5)
        # East
        elif random() < 0.5:
            end = Point(cursor.x + 5, cursor.y)
        # South
        elif random() < 0.75:
            end = Point(cursor.x, cursor.y + 5)
        # West
        else:
            end = Point(cursor.x - 5, cursor.y)

        line = Line(cursor, end)
        line.draw(win)
        cursor = end
        dist = distance(centre, cursor)   
        time.sleep(0.1)


def take_walks(win: Window, num_walks: int, num_steps: int):
    # Simulate `num_walks` random walks of `num_steps` steps each.
    for _ in range(num_walks):
        take_a_walk(win, num_steps)

def distance(pos1: Point, pos2: Point) -> float:
    
    return math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)



def main():
    # Main function to execute the random walk simulation.
    num_walks, max_dist = get_inputs()

    win = Window()
    circle = Circle(Point(win.width//2, win.height//2), max_dist)
    circle.draw(win)
    take_walks(win, num_walks, max_dist)
    win.get_mouse()

main()
