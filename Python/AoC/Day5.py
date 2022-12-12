
def solve1():
    f = open('input.txt', 'r')
    num_boxes = 9
    stacks = [[] for _ in range(num_boxes + 1)]
    # Get crates
    while True:
        line = f.readline().strip('\n')
        boxes = list(map(lambda x: x.strip().strip(']').strip('['), [line[i:i + 4] for i in range(0, len(line), 4)]))
        if boxes[0] == '1':
            break
        for i in range(len(boxes)):
            if boxes[i] != '':
                stacks[i + 1].append(boxes[i])
    for i in range(num_boxes + 1):
        stacks[i].reverse()

    f.readline()
    # Execute commands
    for line in f:
        commands = line.strip().split(' ')
        count, start, end = map(int, [commands[1], commands[3], commands[5]])
        for _ in range(count):
            stacks[end].append(stacks[start].pop())

    top_boxes = []
    for stack in stacks:
        if len(stack) > 0:
            top_boxes.append(stack[-1])
    print(''.join(top_boxes))


def solve2():
    f = open('input.txt', 'r')
    num_boxes = 9
    stacks = [[] for _ in range(num_boxes + 1)]
    # Get crates
    while True:
        line = f.readline().strip('\n')
        boxes = list(map(lambda x: x.strip().strip(']').strip('['), [line[i:i + 4] for i in range(0, len(line), 4)]))
        if boxes[0] == '1':
            break
        for i in range(len(boxes)):
            if boxes[i] != '':
                stacks[i + 1].append(boxes[i])
    for i in range(num_boxes + 1):
        stacks[i].reverse()

    f.readline()
    # Execute commands
    for line in f:
        commands = line.strip().split(' ')
        count, start, end = map(int, [commands[1], commands[3], commands[5]])
        stacks[end] = stacks[end] + stacks[start][-1 * count:]
        stacks[start] = stacks[start][:len(stacks[start]) - count]

    top_boxes = []
    for stack in stacks:
        if len(stack) > 0:
            top_boxes.append(stack[-1])
    print(''.join(top_boxes))

if __name__ == '__main__':
    solve1()
    solve2()
