import re
from itertools import product

raw = open('input.txt', 'r').readlines()

class Decoder:
    def __init__(self, mask, mem):
        self.mask = mask.split()[2]
        self.loc, self.val = re.findall('mem\[(\d+)\] = (.*)', mem)[0]

    def eval(self):
        val_bin = bin(int(self.val))[2:].zfill(36)
        val_masked = [
            v if m == 'X' else m
            for v, m in zip(val_bin, self.mask)
        ]
        val_int = int('0b' + ''.join(val_masked), 2)
        return self.loc, val_int

class MemoryBank:
    def __init__(self):
        self.bank = {}

    @property
    def sum(self):
        return sum(v for k, v in self.bank.items())

    def add(self, ins):
        loc, val = ins.eval()
        self.bank[loc] = val

    def add_n(self, ins):
        for addr in ins.addrs:
            self.bank[addr] = int(ins.val)

# PART A ======================================================================

instructions = []
mask = ''
for line in raw:
    if re.search('mask', line):
        mask = line
    elif re.search('mem', line):
        instructions.append(Decoder(mask, line))

memory_bank = MemoryBank()
for ins in instructions:
    memory_bank.add(ins)

total = memory_bank.sum
print(f"A :: Sum of all memory bank values: {total}")

# PART B ======================================================================

class DecoderB:
    def __init__(self, mask, mem):
        self.mask = mask.split()[2]
        self.loc, self.val = re.findall('mem\[(\d+)\] = (.*)', mem)[0]

        self.loc_bin = bin(int(self.loc))[2:].zfill(36)
        self.loc_masked = ''.join([
            m if m == 'X' else str(int(bool(int(l)) | bool(int(m))))
            for l, m in zip(self.loc_bin, self.mask)
        ])

    @property
    def addrs(self):
        nx = self.loc_masked.count('X')

        def mask_to_bin(s, coord):
            return int('0b' + (s.replace('X', '%d') % coord), 2)

        return [
            mask_to_bin(self.loc_masked, coord)
            for coord in product([0, 1], repeat=nx)
        ]

instructions = []
mask = ''
for line in raw:
    if re.search('mask', line):
        mask = line
    elif re.search('mem', line):
        instructions.append(DecoderB(mask, line))

memory_bank = MemoryBank()
for ins in instructions:
    memory_bank.add_n(ins)

total = memory_bank.sum
print(f"B :: Sum of all memory bank values: {total}")
