from typing import List, Tuple
import math


Point = Tuple[float, float]


def distance(a: Point, b: Point):
    '''Finds the distance between two points'''
    return math.hypot(a[0] - b[0], a[1] - b[1])


def closest_pair_of_points(points: List[Point]) \
        -> Tuple[float, Point, Point]:
    '''Finds the closest pair of points in the list'''
    min_distance = distance(points[1], points[0])
    return (min_distance, points[0], points[1])
