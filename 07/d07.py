from collections import defaultdict
import re

print("Day 7 of Advent of Code!")

def make_graph(rules):
    bags_graph = defaultdict(dict)
    for line in rules.split('\n'):
        line = line.split("contain")
        out_bag = re.findall(r'\w+ \w+ bag', line[0])[0] 
        in_bags = re.findall(r'(\d+) (\w+ \w+ bag)', line[1])
        counts = {}
        for bag in in_bags:
            counts[bag[1]] = int(bag[0])
        bags_graph[out_bag] = counts
    return bags_graph

def count_bags(G, my):
    bags_count = 0
    stack = [my]
    while stack:
        current = stack.pop()
        in_bags = G[current]
        for bag in in_bags:
            count = in_bags[bag]
            bags_count += count
            stack.extend([bag] * count)
    return bags_count

def DFS(G, start, discovered = set()):
    discovered.add(start)
    for node in G[start]:
        if node not in discovered:
            DFS(G, node, discovered)
    return discovered

rules = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

print("Tests...")
G = make_graph(rules)
print("Number of paths:", sum(1 for node in G if node != 'shiny gold bag' and 'shiny gold bag' in DFS(G, node, set())) == 4)
print("Number of bags", count_bags(G, 'shiny gold bag') == 32)
print("---------------------")

with open("input", mode = 'r') as inp:
    rules = inp.read()
    G = make_graph(rules)
    print("Number of paths:", sum(1 for node in G if node != 'shiny gold bag' and 'shiny gold bag' in DFS(G, node, set())))
    print("Number of bags:", count_bags(G, 'shiny gold bag'))
