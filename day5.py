test_data = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

fileObject = open("data/day5.txt", "r")
data = fileObject.read().splitlines()


def get_stacks_and_instructions(_data):
    _stacks = []
    i = 0
    row = _data[i]
    while row != "":
        _stacks.append(row)
        i += 1
        row = _data[i]

    _n_stacks = max([int(i) for i in _stacks[-1].strip().split("  ")])
    _stacks = [stack[1:-1:4] for stack in _stacks[:-1]]

    stacks = [[] for _ in range(_n_stacks)]
    for row in _stacks:
        i = 0
        for char in row:
            if char != ' ':
                stacks[i].append(char)
            i += 1

    stacks = [stack[::-1] for stack in stacks]

    _instructions = _data[i + 1:]

    instructions = []
    for instruction in _instructions:
        a, b, c = [int(i) for i in
                   instruction.replace("move", "").replace("from", "").replace("to", "").strip().split("  ")]
        instructions.append([a, b, c])
    return stacks, instructions


def move_elements_in_stacks(stacks, instructions):

    for n in instructions:
        for el in range(0, n[0]):
            stacks[n[-1]-1].append(stacks[n[1]-1].pop())

    return stacks


def move_elements_in_stacks_2(stacks, instructions):

    for n in instructions:
        removed = []
        for el in range(0, n[0]):
            removed.append(stacks[n[1]-1].pop())
        stacks[n[-1] - 1].extend(removed[::-1])

    return stacks


stacks, instructions = get_stacks_and_instructions(data)
final_stacks_1 = move_elements_in_stacks(stacks, instructions)
print("".join([stack.pop() for stack in final_stacks_1]))

stacks, instructions = get_stacks_and_instructions(data)
final_stacks_2 = move_elements_in_stacks_2(stacks, instructions)
print("".join([stack.pop() for stack in final_stacks_2]))
