import csv
import fileinput
import sys
from collections import defaultdict

nick_to_team = defaultdict(set)

f = open('nicks.csv', 'r')
reader = csv.reader(f)
for line in reader:
    group = line[-1]
    for nick in line[:-1]:
        if '@' in nick:
            nick = nick.split('@')[0]
        elif '_' in nick:
            nick = nick.split('_')[0]

        if nick:
            nick_to_team[nick.lower()].add(group.lower())

def lookup(nick):
    if nick in nick_to_team:
        return nick_to_team[nick]
    else:
        if '_' in nick:
            nick = nick.split('_')[0]
            if len(nick) > 0:
                return lookup(nick)
        sys.stderr.write("Unfound: %s\n" % nick)
        return set()

for line in fileinput.input():
    (pluser,plusee) = line.rstrip().split('\t')
    for team_pluser in lookup(pluser):
        for team_plusee in lookup(plusee):
            print "%s\t%s" % (team_pluser, team_plusee)
