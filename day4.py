fileObject = open("data/day4.txt", "r")
data = fileObject.read().splitlines()


test_data = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def pair_contains_other(data):
    number_of_pairs = 0
    for row in data:
        x, y = [[x for x in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1)] for i in row.split(",")]
        if set(x).issubset(set(y)) or set(y).issubset(set(x)):
            number_of_pairs += 1
    return number_of_pairs


def pair_contains_other_2(data):
    number_of_pairs = 0
    for row in data:
        x, y = [[x for x in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1)] for i in row.split(",")]
        if any([{i}.issubset(set(y)) for i in x]) or any([{i}.issubset(set(x)) for i in y]):
            number_of_pairs += 1
    return number_of_pairs


print(pair_contains_other(data))
print(pair_contains_other_2(data))

