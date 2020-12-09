raw = open('input.txt', 'r').readlines()

data = [(line.split()[0], int(line.split()[1])) for line in raw]

accumulator = 0
pointer = 0
cache = []

while pointer not in cache:
    ins, val = data[pointer]
    cache.append(pointer)
    if ins == 'nop':
        pointer += 1
    elif ins == 'acc':
        pointer += 1
        accumulator += val
    elif ins == 'jmp':
        pointer += val

print(f"Value of accumulator = {accumulator}")

def run_sim(data):
    accumulator = 0
    pointer = 0
    cache = []

    # Swap value at pointer
    ins, val = data[pointer]
    if ins == 'nop':
        data[pointer] = ('jmp', val)
    elif ins == 'jmp':
        data[pointer] = ('nop', val)

    while pointer not in cache:
        ins, val = data[pointer]
        cache.append(pointer)
        if ins == 'nop':
            pointer += 1
        elif ins == 'acc':
            pointer += 1
            accumulator += val
        elif ins == 'jmp':
            pointer += val

        if pointer == len(data):
            return True, accumulator            

    return False, 0

for pointer, (ins, val) in enumerate(data):
    datac = data.copy()
    if ins == 'nop':
        datac[pointer] = ('jmp', val)
    elif ins == 'jmp':
        datac[pointer] = ('nop', val)

    res, accumulator = run_sim(datac)
    if res:
        break

print(f"Swapping the instruction at pointer {pointer} gets accumulator {accumulator}")
