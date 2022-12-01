def read_input():
    elf = []
    elves = []

    with open('input01.txt', 'rb') as f:
        for line in f:
            line = line.strip()

            if not line:
                elves.append(elf)
                elf = []
                continue

            elf.append(int(line))

    return elves


if __name__ == '__main__':
    elves = read_input()

    sum_of_calories = sorted([sum(elf) for elf in elves])

    print sum(sum_of_calories[-1:])
    print sum(sum_of_calories[-3:])
