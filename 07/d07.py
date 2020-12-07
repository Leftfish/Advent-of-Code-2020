import networkx as nx
import re

print("Day 7 of Advent of Code!")

def make_graph(rules):
    G = nx.DiGraph()
    for r in rules:
        all_bags = re.findall(r'\w+ \w+ bag', r)
        for bag in all_bags:
            if bag != 'no other bag':
                G.add_node(bag)
        r = r.split("contain")
        out_bag = re.findall(r'\w+ \w+ bag', r[0])[0] 
        in_bags = re.findall(r'(\d+) (\w+ \w+ bag)', r[1])
        for bag in in_bags:
            G.add_edge(out_bag, bag[1], weight = int(bag[0]))
    return G

def count_paths(G, my):
    res = set()
    for n in G.nodes():
        if n != my:
            try:
                res.update(nx.shortest_path(G, n, my))
            except:
                pass
    return len(res) - 1

def count_bags(G, my):
    bags_count = 0
    stack = [my]
    while stack:
        current = stack.pop()
        in_bags = G[current]
        for bag in in_bags:
            count = in_bags[bag]['weight']
            bags_count += count
            stack.extend([bag] * count)
    return bags_count

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
my = 'shiny gold bag'
G = make_graph(rules.split('\n'))
print("Number of paths:", count_paths(G, 'shiny gold bag') == 4)
print("Number of bags", count_bags(G, 'shiny gold bag') == 32)
print("---------------------")

with open("input", mode = 'r') as inp:
    rules = [r.strip() for r in inp.readlines()]
    G = make_graph(rules)
    print("Number of paths:", count_paths(G, 'shiny gold bag'))
    print("Number of bags:", count_bags(G, 'shiny gold bag'))
