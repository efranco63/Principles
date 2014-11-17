import csv
import sys
from itertools import islice

def main(filename,zipboro):
    zips = []
    boros = ['BROOKLYN','QUEENS','BRONX','MANHATTAN','STATEN ISLAND']
    boro_count = {}
    zipmap = {}
    for i in boros:
        boro_count[i] = 0
    with open(filename,'rb') as prob7:
        reader = csv.reader(prob7)
        for row in islice(reader,1,None):
            zips.append(row[7])
    with open(zipboro,'rb') as prob7:
        reader = csv.reader(prob7)
        for row in islice(reader,1,None):
            zipmap[row[0]] = row[1]
    for i in zips:
        if i in zipmap:
            boro_count[zipmap[i]] += 1
    for key in boro_count:
        print key.lower().title() + ' with ' + str(boro_count[key]) + ' complaints'

if __name__ == "__main__":
    filename = sys.argv[1]
    zipboro = sys.argv[2]
    main(filename,zipboro)