import fileinput
import re
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-g', '--group', dest='group_filter', default='')
parser.add_option('-f', '--file', dest='file')
(options, args) = parser.parse_args()

f = open(options.file, 'r')

matcher = re.compile('(\w+): \[(#?\w+)\] <([a-zA-Z_0-9]+)> \?\+\+ ([a-zA-Z_0-9]+).*')

for line in f:
    match = matcher.match(line.lower())
    if match:
        (source, group, pluser, plusee) = match.groups()
        if options.group_filter == '' or options.group_filter == group:
            print "%s\t%s" % (pluser,plusee)
