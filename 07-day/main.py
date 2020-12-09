import re

raw = open('input.txt', 'r').readlines()

def bag_to_color(s):
    return ' '.join(s.split(' ')[:2])

def process_child_string(s):
    n, bag = re.findall("(\d+) (.*)", s.strip().replace('.', ''))[0]
    bag = bag_to_color(bag)
    return {"count": int(n), "color": bag}

class Bag:
    def __init__(self, parent, children):
        self.name = parent
        if children.lower().strip() == "no other bags.":
            self.children = []
        else:
            self.children = [process_child_string(child) for child in children.split(', ')]

    def can_hold_gold(self):
        child_colors = [bag["color"] for bag in self.children]
        return ("shiny gold" in child_colors) or any([bags[color].can_hold_gold() for color in child_colors])

    def n_children(self):
        return 1 + sum(bag['count']*bags[bag['color']].n_children() for bag in self.children)

bags = {}
for line in raw:
    parent, children = line.split(' contain ')
    parent = bag_to_color(parent)
    bags[parent] = Bag(parent, children)

has_gold = [bag.can_hold_gold() for name, bag in bags.items()]
n_gold = sum(has_gold)
print(f"Number of bags which can eventually hold gold: {n_gold}")

n_sub_bags = bags['shiny gold'].n_children() - 1
print(f"Number of bags required in my shiny gold bag: {n_sub_bags}")
