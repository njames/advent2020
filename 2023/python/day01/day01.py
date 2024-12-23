import re

testData = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

testData2 = """
twone∂1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

searchFor = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def calibrate1(data):
    sum = 0
    for line in data:
        match  = re.findall(r'\d', line)
        sum = sum + int(match[0] + match[-1])
        # sums.append(sum(intLine))

    return sum

# def findNumber(data, )
def calibrate2(data):
def calibrate2(data):
    sum = 0
    for line in data:
        for word in searchFor:
            match = re.search( r'('.join(word) + r'\d', line)
            print('woah')



    return sum

# Create a regular expression pattern using the | operator


if __name__ == '__main__':
    # get input
    assert calibrate1(testData.strip().split('\n')) == 142, "the sum of the test data is 142"
    assert calibrate2(testData2.strip().split('\n')) == 281, "test second part adds to 281"

    data = open('../../input/day01/input01').read().strip().split('\n')

    # part one
    print( ' Part 1 ', calibrate1(data))
    print( ' Part 2 ', calibrate2(data))