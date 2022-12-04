def is_fully_contained(elf_1, elf_2):
    return elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]

def is_overlapping(elf_1, elf_2):
    return elf_1[0] in range(elf_2[0], elf_2[1]+1) or elf_1[1] in range(elf_2[0], elf_2[1]+1)

if __name__ == '__main__':
    contained_counter = 0
    overlapping_counter = 0
    with open('input04.txt', 'rb') as f:
        for line in f.readlines():
            line = line.strip()
            first_elf = [int(s) for s in line.split(',')[0].split('-')]
            second_elf = [int(s) for s in line.split(',')[1].split('-')]

            if is_fully_contained(first_elf, second_elf) or is_fully_contained(second_elf, first_elf):
                contained_counter += 1

            if is_overlapping(first_elf, second_elf) or is_overlapping(second_elf, first_elf):
                overlapping_counter += 1

    print '{} areas are fully contained.'.format(contained_counter)
    print '{} ranges are overlapping.'.format(overlapping_counter)

