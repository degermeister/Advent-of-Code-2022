from copy import deepcopy


def make_a_move(move, stacks):
    for i in xrange(move[0]):
        stacks[move[2]-1].insert(0, stacks[move[1]-1].pop(0))
    return stacks

def make_a_stack_move(move, stacks):
    crane_stack = []
    for i in xrange(move[0]):
        crane_stack.append(stacks[move[1]-1].pop(0))
    
    crane_stack.extend(stacks[move[2]-1])
    stacks[move[2]-1] = crane_stack
    return stacks



if __name__ == '__main__':
    stacks = []
    rows = []
    moves = []
    with open('input05.txt', 'rb') as f:
        get_initial_state = True
        for line in f.readlines():
            if line.startswith(' 1'):
                get_initial_state = False
                continue

            if get_initial_state:
                crate_row = []
                index = 1
                while index < len(line) - 1:
                    crate_row.append(line[index])
                    index += 4
                rows.append(crate_row)

            else:
                line = line.strip()
                if not line:
                    continue
                else:
                    line = line.split()
                    moves.append([ int(line[1]), int(line[3]), int(line[5]) ])

    for row in rows:
        if len(stacks) < len(row):
            for i in xrange(len(row)):
                stacks.append([])
        for stack, crate in enumerate(row):
            if crate != ' ':
                stacks[stack].append(crate)

    cratemover9000 = deepcopy(stacks)
    cratemover9001 = deepcopy(stacks)
    
    for move in moves:
        cratemover9000 = make_a_move(move, cratemover9000)
        cratemover9001 = make_a_stack_move(move, cratemover9001)

    s = ''
    for stack in cratemover9000:
        s += stack[0]
    print 'CrateMover 9000: ', s

    s = ''
    for stack in cratemover9001:
        s += stack[0]
    print 'CrateMover 9001: ', s
