
def solve1():
    f = open('input.txt', 'r')
    sum = 0
    for line in f:
        chars = list(line)
        arr1 = set(chars[:len(chars) // 2])
        arr2 = set(chars[len(chars) // 2:])
        char = arr1.intersection(arr2).__iter__().__next__()
        if char.isupper():
            sum += ord(char) - 38
        else:
            sum += ord(char) - 96
    print(sum)


def solve2():
    f = open('input.txt', 'r')
    sum = 0
    group = []
    for line in f:
        group.append(set(line.strip()))
        if len(group) == 3:
            remaining = group[0].intersection(group[1]).intersection(group[2])
            char = remaining.__iter__().__next__()
            if char.isupper():
                sum += ord(char) - 38
            else:
                sum += ord(char) - 96
            group = []
    print(sum)


if __name__ == '__main__':
    solve1()
    solve2()
