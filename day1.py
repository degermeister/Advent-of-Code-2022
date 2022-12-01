#!/bin/python
# coding=utf8

def read_input():
    elf = []
    elves = []

    with open('input.txt', 'rb') as f:
        for line in f:
            line = line.strip()

            if not line:
                elves.append(elf)
                elf = []
                continue

            elf.append(int(line))

    return elves


def get_top_three(calories, top_three):
    top_three.append(calories)
    top_three.sort(reverse=True)
    top_three.pop()
    return top_three


if __name__ == '__main__':
    top_three = [0, 0, 0]

    elves = read_input()

    for elf in elves:
        calories = sum(elf)
        top_three = get_top_three(calories, top_three)

    print sum(top_three)