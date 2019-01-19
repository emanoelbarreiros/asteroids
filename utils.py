import math
from pathlib import Path

def check_bounds(position, limit, buffer):
    if position < 0 - buffer:
        return limit + buffer
    elif position > limit + buffer:
        return -buffer
    else:
        return position


def rotate_around_origin(xy, radians):
    """Rotate the point around the origin.

    Taken from https://ls3.io/post/rotate_a_2d_coordinate_around_a_point_in_python/"""
    x, y = xy
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)
    return xx, yy



def center_text(text, page_width, char_width):
    """Helper function for calcuating the start x value for centered text."""

    text_width = len(text) * char_width
    return (page_width - text_width) // 2


def get_highscore(filename):
    file = Path(__file__).parent / filename
    try:
        high_score = int(file.read_text())
    except FileNotFoundError:
        high_score = 0
    except ValueError:
        raise ValueError("File contents does not evaluate to string – highscore file corrupted.")
    return high_score

def save_highscore(filename, high_score):
    file = Path(__file__).parent / filename
    file.write_text(str(high_score))


class Point:
    """Class to capture points in an entity with the rotate helper method included."""

    def __init__(self, x, y):
        """Initiate variables."""
        self.x = x
        self.y = y

    def rotate_point(self, radians):
        """Rotate the point around the origin."""
        self.x, self.y = rotate_around_origin((self.x, self.y), radians)
