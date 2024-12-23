import time
import re
from typing import List, Any


# Press the green button in the gutter to run the script.
def score(c):
    value = ord(c) - 96
    if value < 0:
        value = ord(c) - ord('A') + 27
    return value


def common(rucksacks):
    return list(filter(lambda x: x in rucksacks[0], rucksacks[1]))[0]


def commonSet(r1, r2):
    return set(filter(lambda x: x in r1, r2))


def splitLine(line=None):
    return [line[0:int(len(line) / 2)], line[int(len(line) / 2):]]


def part1(data):
    part_a = []
    part_b = []
    sum1 = 0
    for line in data:
        pattern = '(?P<o>[\d]*)\D*(?P<t>[\d]*)'
        match = re.search(pattern, line)
        part_a.append(int(match.group('o')))
        part_b.append(int(match.group('t')))


    part_a.sort()
    part_b.sort()

    for i in range(len(part_a)):
        sum1 = sum1 + abs(part_a[i] - part_b[i])

    return sum1

def part2(data):
    part_a = []
    part_b = []
    sum2 = 0
    for line in data:
        pattern = '(?P<o>[\d]*)\D*(?P<t>\d*)'
        match = re.search(pattern, line)
        part_a.append(int(match.group('o')))
        part_b.append(int(match.group('t')))



    for i in range(len(part_a)):

        n = part_b.count(part_a[i])

        sum2 += n * part_a[i]


    return sum2




def test_part1():
    data = '''3   4
4   3
2   5
1   3
3   9
3   3'''

    data = [line for line in data.strip().split('\n')]

    assert part1(data) == 11
    assert part2(data) == 31


if __name__ == '__main__':

    # get input
    # data = [line for line in open('../../input/day03/test.txt').read().strip().split('\n')]
    data = [line for line in open('../../input/day01/input').read().strip().split('\n')]



    print('\n')
    print('Part 1: ', part1(data))

    print('Part 2', part2(data))

    t = time.perf_counter()
    print(t)

