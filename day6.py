test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

fileObject = open("data/day6.txt", "r")
data = fileObject.read().splitlines()[0]


def find_signal(data):
    for char in range(len(data)-14):
        if len(set(data[char:char+14])) == 14:
            return char + 14

print(find_signal(data))