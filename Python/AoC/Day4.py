
def solve1():
    f = open('input.txt', 'r')
    sum = 0
    for line in f:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
            sum += 1
    print(sum)


def solve2():
    f = open('input.txt', 'r')
    sum = 0
    for line in f:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if (a1 <= b1 <= a2) or (b1 <= a1 <= b2) or (a1 <= b2 <= a2) or (b1 <= a2 <= b2):
            sum += 1
    print(sum)

if __name__ == '__main__':
    solve1()
    solve2()
