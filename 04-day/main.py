import re
from functools import reduce

raw = open('input.txt', 'r').read().split('\n\n')

class Passport:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, entry):
        fields = re.split('\s', entry.strip())
        self.fields = {field.split(':')[0]:field.split(':')[1] for field in fields}

    def is_valid_a(self):
        return all(req in self.fields for req in self.required_fields)

    def is_valid_b(self):
        return self.is_valid_a() and reduce(
            lambda a, b: a and b, 
            [
                self.is_valid_byr(),
                self.is_valid_iyr(),
                self.is_valid_eyr(),
                self.is_valid_hgt(),
                self.is_valid_hcl(),
                self.is_valid_ecl(),
                self.is_valid_pid()
            ]
        )

    def is_valid_byr(self):
        byr = self.fields['byr']
        return re.match('\d{4}', byr) and (1920 <= int(byr) <= 2002)

    def is_valid_iyr(self):
        iyr = self.fields['iyr']
        return re.match('\d{4}', iyr) and (2010 <= int(iyr) <= 2020)

    def is_valid_eyr(self):
        eyr = self.fields['eyr']
        return re.match('\d{4}', eyr) and (2020 <= int(eyr) <= 2030)

    def is_valid_hgt(self):
        hgt = self.fields['hgt'][:-2]
        unit = self.fields['hgt'][-2:]

        if unit == 'cm':
            return re.match('\d+', hgt) and (150 <= int(hgt) <= 193)
        elif unit == 'in':
            return re.match('\d+', hgt) and (59 <= int(hgt) <= 76)
        else:
            return False

    def is_valid_hcl(self):
        hcl = self.fields['hcl']
        return bool(re.match('#[0-9a-f]{6}', hcl))

    def is_valid_ecl(self):
        return self.fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_valid_pid(self):
        return bool(re.match('^\d{9}$', self.fields['pid']))

passports = [Passport(line) for line in raw]
n_valid = sum(ppt.is_valid_a() for ppt in passports)
print(f"A :: Number of valid passports: {n_valid}")

# 199 too high
n_valid = sum(ppt.is_valid_b() for ppt in passports)
print(f"B :: Number of valid passports: {n_valid}")
