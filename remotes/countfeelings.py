import csv
import json
import operator

from collections import defaultdict
from collections import OrderedDict
from json import JSONEncoder

feelings = [
    'feelings',
    0,
    defaultdict(lambda : ['', 0, defaultdict(lambda : ['', 0, {}])])
]

uf = defaultdict(lambda : defaultdict(int))

class feelingMap:
    def __init__(self, name):
        self.name = name
        self.children = [] # list of feelingMaps

fm = feelingMap('feelings')


with open('feelings.csv') as feelingsfile:
    feelingscsv = csv.reader(feelingsfile)
    next(feelingscsv)
    for row in feelingscsv:
        (word, c, feeling) = (row[0], int(row[1]), row[2])

        subsubfm = feelingMap(word)
        subsubfm.size = c;

        subfm = feelingMap(feeling)
        subfm.children.append(subsubfm)

        fm.children.append(subfm)

        uf[feeling][word] += c

        feelings[2][feeling][0] = feeling
        feelings[2][feeling][1] += c
        feelings[2][feeling][2][word][0] = word
        feelings[2][feeling][2][word][1] += c
        feelings[1] += c

sorted_feelings = [(a[0], sorted(a[1].items(), key=operator.itemgetter(1))) for a in uf.items()]
feeling_totals = {}
feeling_dicts = {}
for feeling in sorted_feelings:
    feeling_totals[feeling[0]] = reduce(lambda x,y: x + y[1], feeling[1], 0)
    feeling_dicts[feeling[0]] = feeling[1]

new_feelings = [
    'feelings',
    0,
    OrderedDict()
]
sorted_feeling_totals = sorted(feeling_totals.items(), key=operator.itemgetter(1))
for feeling in sorted_feeling_totals:
    fd = OrderedDict()
    for word,total in feeling_dicts[feeling[0]]:
        fd[word] = [word, total, {}]
        new_feelings[1] += total
    new_feelings[2][feeling[0]] = [
        feeling[0],
        feeling[1],
        fd
    ]
print "code_hierarchy_data =";
print json.dumps(new_feelings, indent=4, separators=(',', ': '))
print ";\n";
