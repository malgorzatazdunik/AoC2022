fileObject = open("data/day2.txt", "r")
data = fileObject.read().splitlines()


def count_score(data):
    choice = {
        "X": {
            "points": 1,
            "wins": "C",
            "equals": "A"
        },
        "Y": {
            "points": 2,
            "wins": "A",
            "equals": "B"
        },
        "Z": {
            "points": 3,
            "wins": "B",
            "equals": "C"
        }
    }

    total = 0
    for line in data:
        opponent = line.split(' ')[0]
        you = line.split(' ')[1]

        total += choice[you]["points"]
        if choice[you]["wins"] == opponent:
            total += 6
        elif opponent == choice[you]["equals"]:
            total += 3

    return total


def count_score_2(data):
    choice = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    wins = {
        "A": "B",
        "B": "C",
        "C": "A"
    }

    total = 0
    for line in data:
        opponent = line.split(' ')[0]
        you = line.split(' ')[1]

        if you == "Y":
            total += 3
            total += choice[opponent]
        if you == "Z":
            total += 6
            total += choice[wins[opponent]]
        if you == "X":
            total += [choice[i] for i in ["A", "B", "C"] if i != opponent and i != wins[opponent]][0]


    return total

print(count_score(['A Y', 'B X', 'C Z']))
print(count_score(data))
print(count_score_2(['A Y', 'B X', 'C Z']))
print(count_score_2(data))