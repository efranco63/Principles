import csv
import sys
from itertools import islice

def main(filename):
    with open(filename,'rb') as prob3:
        reader = csv.reader(prob3)
        complaints = {}
        for row in islice(reader,1,None):
            if row[5] in complaints.keys():
                complaints[row[5]] += 1
            else:
                complaints[row[5]] = 1
        complaints_sort = sorted(complaints.items(), key=lambda x: (-x[1], x[0]))
        for i in complaints_sort:
            print i[0] + ' with ' + str(i[1]) + ' complaints'

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)