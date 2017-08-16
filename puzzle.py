#!/usr/bin/env python

# Puzzle challenge
# Input: File with number o puzzle pieces, number of moves and list of movements
# Output: Number of pieces without any connection and the ammount of different groups

# File containing input
with open("input/06530702528071") as f:
    content = f.readlines()

content = [x.strip() for x in content]
pieces, moves = content.pop(0).split();


# Go through the list of moves connecting pieces
clusters = []
for line in content:
    a, b = line.split();

    found = []
    i=0
    for cluster in clusters:
        if (a in cluster) or (b in cluster):
            cluster[a]=1
            cluster[b]=1
            found.append(i)
        i = i+1

    # Piece does not belongs to any cluster
    if len(found) == 0:
        c = {}
        c[a] = 1
        c[b] = 1
        clusters.append(c.copy())
    #Piece found in multiple clesters
    if len(found) >= 2:
        original = found.pop(0)
        for f in found:
            for newkey in clusters[f]:
                clusters[original][newkey] = 1
        for f in found:
            del clusters[f]

# Different pieces that belongs to a cluster
unique = {}
for cluster in clusters:
    for k in cluster.keys():
        unique[k]=1

print (str(int(pieces)-len(unique)) +" Alone")
print (str(len(clusters)) +" Groups")
