python plusedges.py -f irccat_nohup.log |sort |uniq |python edges_to_groups.py |sort |uniq |python rank.py >plusgraph.js
