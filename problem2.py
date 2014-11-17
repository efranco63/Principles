import csv
import sys
from itertools import islice

def main(filename):
    with open(filename,'rb') as prob2:
        reader = csv.reader(prob2)
        complaints = {}
        for row in islice(reader,1,None):
            if row[5] in complaints.keys():
                complaints[row[5]] += 1
            else:
                complaints[row[5]] = 1
        for key in complaints:
            print str(key) + ' with ' + str(complaints[key]) + ' complaints'

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)