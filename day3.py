# lowercase item types have priorities 1 - 26
# uppercase 27 - 52

fileObject = open("data/day3.txt", "r")
data = fileObject.read().splitlines()

a = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
alphabet = {
    a[i]: i + 1 for i in range(len(a))
}


def count_letters(data):
    x = []
    for row in data:
        item_per_row = []
        first = row[:int(len(row) / 2)]
        for item in row[int(len(row) / 2):]:
            if item in first:
                if item not in item_per_row:
                    item_per_row += [item]
        x += item_per_row

    return count_priorities(x)


def count_priorities(x):
    sum = 0
    for i in x:
        if i in alphabet:
            sum += alphabet[i]
        else:
            sum += alphabet[i.lower()] + 26

    return sum


test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
print(count_letters(data))


def count_letters_2(data):
    groups = [data[i:i + 3] for i in range(0, len(data), 3)]

    x = []
    for group in groups:
        elf_1 = [l for l in group[0]]
        repeats = []
        for l in group[1]:
            if l in elf_1:
                repeats += [l]
        for l in group[2]:
            if l in repeats:
                x += [l]
                break

    return count_priorities(x)

print(count_letters_2(data))