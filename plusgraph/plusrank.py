import fileinput
import json
import operator
import re
from collections import defaultdict

matcher = re.compile('(\w+): \[(#?\w+)\] <([a-zA-Z_0-9]+)> \?\+\+ ([a-zA-Z_0-9]+).*')

nodes = set()
edges = defaultdict(set)

for line in fileinput.input():
    match = matcher.match(line)
    if match:
        (source, group, pluser, plusee) = [x.lower() for x in match.groups()]
        if pluser != plusee:
            nodes.add(pluser)
            nodes.add(plusee)
            edges[pluser].add(plusee)

node_values = {}
for node in nodes:
    node_values[node] = 1.0

for i in range(0,10):
    new_node_values = defaultdict(float)
    for edge in edges:
        value = node_values[edge]
        value_per_node = value / float(len(edges[edge]))
        for plusee in edges[edge]:
            new_node_values[plusee] += value_per_node

    node_values = new_node_values.copy()

distinct_edges = []
for source in edges:
    for target in edges[source]:
        distinct_edges.append({'source': source,
                               'target': target});

for node in node_values:
    node_values[node] = int(node_values[node] * 10000)

print "var links = " + json.dumps(distinct_edges,
                                  indent=4, separators=(',', ': ')) + ";";

print "var ranks = " + json.dumps(node_values, indent=4, separators=(',', ': ')) + ";"
