
ITEMS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(item):
    return ITEMS.index(item) + 1

if __name__ == '__main__':
    score = 0
    compartments = []

    with open('input03.txt', 'rb') as f:
        i = 0
        group = []
        groups = []
        for line in f.readlines():
            line = line.strip()
            if i < 2:
                group.append(line)
                i += 1
                continue
            else:
                group.append(line)
                groups.append(group)
                group = []
                i = 0

        for group in groups:
            for item in ITEMS:
                if item in group[0] and item in group[1] and item in group[2]:
                    score += get_priority(item)
        print score
