import csv

from collections import defaultdict
from stemming.porter2 import stem

words = defaultdict(int)

with open('results.csv') as results:
    resultcsv = csv.reader(results)
    next(resultcsv)
    for row in resultcsv:
        word = row[1].lower()
        words[word] += 1

for k in words:
    print ','.join([k, str(words[k])])
