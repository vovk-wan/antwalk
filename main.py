# -*- coding=utf-8 -*-
"""Ant walk"""

import argparse
import logging.config
from time import time

from logging_config import config

logging.config.dictConfig(config)
logger = logging.getLogger("ant_logger")
logger.setLevel(logging.INFO)


def get_argument():
    parser = argparse.ArgumentParser(description='Ant`s walk')
    parser.add_argument('--x', type=int, default=1000, help='ant x-position')
    parser.add_argument('--y', type=int, default=1000, help='ant y-position')
    parser.add_argument('--limit', type=int, default=25, help='point limit')
    parser.add_argument(
        '--debug',
        type=int,
        default=0,
        help='debug regime (1 on 0 off, default=off)'
    )
    return parser.parse_args()


def extract_number(number):
    """
    The function receives the given number and returns a list of digits that
    make up the number

    :param number: int
    :return: list of digit
    """
    number = abs(number)
    digit_list = []
    if number == 0:
        return [0]
    while number:
        digit_list.append(number % 10)
        number = number // 10
    return digit_list


def check_point(point, limit=25):
    """
    The function receives the coordinates of the point and returns the result
    of the check.
    True is returned if the sum of the digits in the X coordinate plus the sum
    of the digits in the Y coordinate is less than or equal to the limit.

    :param point: tuple[int, int]
    :param limit: int - default 25
    :return: bool
    """
    return sum(extract_number(point[0]) + extract_number(point[1])) <= limit


def get_neighboring_points(point):
    """
    The function receives the coordinate of a point and returns the coordinates
    of neighboring points vertically and horizontally.

    :param point: tuple[int, int]
    :return: set[tuple[int, int]]
    """
    x, y = point
    return {(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)}


def get_all_point(point, limit):
    """
    The function receives the coordinates of the point where the ant is
    located, generates and returns a set of coordinates of points that the ant
    can visit starting from the starting position.
    The starting position is always included in the set even if it does not
    meet the condition.

    :param point: tuple[int, int]
    :param limit: int
    :return: set[tuple[int, int]]
    """
    start = time()
    all_points = {point, }
    neighboring_points = get_neighboring_points(point)
    while neighboring_points:
        p = neighboring_points.pop()
        if check_point(p, limit) and p not in all_points:
            logger.debug('visited point {}'.format(p))
            all_points.add(p)
            neighboring_points.update(get_neighboring_points(p))

    logger.info('walking time = {}'.format(time() - start))
    return all_points


def main():
    args = get_argument()
    if args.debug:
        logger.setLevel(logging.DEBUG)
    all_points = get_all_point((args.x, args.y), args.limit)
    logger.info('count:  %s' % len(all_points))


if __name__ == '__main__':
    main()
