import math as mth

from .objects.Circle import Circle
from .objects.Rect import Rect


def distance_to(p1: tuple, p2: tuple):
    k1 = p1[0] - p2[0]
    k2 = p1[1] - p2[1]
    return mth.sqrt((k1 * k1) + (k2 * k2))


def is_point_inside_circle(point: tuple, circle: Circle):
    return distance_to(point, circle.position) < circle.radius


def is_point_inside_rect(point: tuple, rect: Rect):
    px, py = point
    rx, ry = rect.position
    rw, rh = rect.size

    return rx <= px <= rx + rw and ry <= py <= ry + rh


def invert_color(color):
    return 255 - color[0], 255 - color[1], 255 - color[2]