"""
Takes some edges and produces output in the format:

var links = [{'node1','node2'}, ...];
var ranks = {'node1' => rank, ...};

Options
  -n, --nodefilter Maximum number of nodes to emit.
  -d, --delimiter  Delimiter for input file
"""
import csv
import fileinput
import json
import operator
import sys
from collections import defaultdict
from optparse import OptionParser

damping_factor = 0.85
min_delta=0.00001

nodes = set()
edges = defaultdict(set)
inbound_edges = defaultdict(set)

parser = OptionParser()
parser.add_option('-n', '--nodefilter', dest='nodefilter', default=0, type="int")
parser.add_option('-d', '--delimiter', dest='delimiter', default='\t')
(options, args) = parser.parse_args()

reader = csv.reader(sys.stdin, delimiter=options.delimiter)

for line in reader:
    (n1, n2) = line
    nodes.add(n1)
    nodes.add(n2)
    edges[n1].add(n2)
    inbound_edges[n2].add(n1)

node_values = dict.fromkeys(nodes, 1.0/len(nodes))
min_value = (1.0-damping_factor)/len(nodes)

for i in range(100):
    diff = 0
    for node in nodes:
        rank = min_value
        for inbound in inbound_edges[node]:
            rank += damping_factor * node_values[inbound] / len(edges[inbound])

        diff += abs(node_values[node] - rank)
        node_values[node] = rank
    if diff < min_delta:
        break

original_node_values = node_values.copy()

if options.nodefilter > 0:
    sorted_nodes = sorted_nodes = sorted(node_values.iteritems(), key=operator.itemgetter(1))
    node_values = dict(sorted_nodes[:options.nodefilter])

distinct_edges = []
to_add = set()
for source in edges:
    for target in edges[source]:
        if source in node_values or target in node_values:
            distinct_edges.append({'source': source,
                                   'target': target});
            to_add.add(source)
            to_add.add(target)

for add in to_add:
    node_values[add] = original_node_values[add]

multiplier = 25.0 / float(max(node_values.values()))
node_values = {k:v * multiplier for k,v in node_values.items()}

print "var links = " + json.dumps(distinct_edges,
                                  indent=4, separators=(',', ': ')) + ";";

print "var ranks = " + json.dumps(node_values, indent=4, separators=(',', ': ')) + ";"
