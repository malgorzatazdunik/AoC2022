fileObject = open("data/day1.txt", "r")
data = fileObject.read().splitlines()


def count_max_calories_elf(data):
    max_sum = 0
    sum = 0
    for line in data:
        try:
            sum += int(line)
        except ValueError:
            if sum > max_sum:
                max_sum = sum
            sum = 0

    if sum > max_sum:
        max_sum = sum
    return max_sum


def count_max_calories_elf_2(data):
    calories_by_elf = []
    total = 0
    for line in data:
        try:
            total += int(line)
        except ValueError:
            calories_by_elf += [total]
            total = 0

    return sum(sorted(calories_by_elf)[-3:])


def test_count_max_calories_elf():
    data = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '',
            '7000', '8000', '9000', '', '10000']
    assert count_max_calories_elf(data) == 24000

test_count_max_calories_elf()
print(count_max_calories_elf(data))
print(count_max_calories_elf_2(data))

