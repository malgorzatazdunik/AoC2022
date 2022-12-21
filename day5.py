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

    _instructions = _data[i + 1:]
    return _n_stacks, _stacks, _instructions


def move_elements_in_stacks(_n_stacks, _stacks, _instructions):
    # n_stacks = max([int(i) for i in _stacks[-1].strip().split("  ")]) - 1

    l_stacks = [[] for _ in range(_n_stacks)]
    for row in _stacks:
        i = 0
        for char in row:
            if char != ' ':
                l_stacks[i].append(char)
            i += 1

    l_stacks = [stack[::-1] for stack in l_stacks]

    nums = []
    for instruction in _instructions:
        a, b, c = [int(i) for i in instruction.replace("move", "").replace("from", "").replace("to", "").strip().split("  ")]
        nums.append([a, b, c])

    for n in nums:
        for el in range(0, n[0]):
            l_stacks[n[-1]-1].append(l_stacks[n[1]-1].pop())

    return l_stacks


n_stacks, stacks, instructions = get_stacks_and_instructions(data)
final_stacks = move_elements_in_stacks(n_stacks, stacks, instructions)
print("".join([stack.pop() for stack in final_stacks]))
