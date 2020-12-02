import re

def extract_data(line):
    return re.findall('(\d+)-(\d+) (\w){1}: (.*)', line)[0]

def xor(a, b):
    return (a and not b) or (b and not a)

data = [extract_data(line.strip()) for line in open('input.txt', 'r')]

class Password:
    def __init__(self, lb, ub, char, pwd):
        self.lb = int(lb)
        self.ub = int(ub)
        self.char = char
        self.pwd = pwd

    def is_ok_1(self):
        return self.lb <= self.pwd.count(self.char) <= self.ub

    def is_ok_2(self):
        return xor(self.pwd[self.lb - 1] == self.char, self.pwd[self.ub - 1] == self.char)

pwds = [Password(*datum) for datum in data]

num_ok = sum(pwd.is_ok_1() for pwd in pwds)
print(f"A :: The number of legal passwords: {num_ok}")

num_ok = sum(pwd.is_ok_2() for pwd in pwds)
print(f"B :: The number of legal passwords: {num_ok}")
