import csv
import sys
from itertools import islice

def main(filename,k):
    with open(filename,'rb') as prob4:
        reader = csv.reader(prob4)
        complaints = {}
        for row in islice(reader,1,None):
            if row[5] in complaints.keys():
                complaints[row[5]] += 1
            else:
                complaints[row[5]] = 1
        complaints_sort = sorted(complaints.items(), key=lambda x: (-x[1], x[0]))
        k = int(k)
        for i in complaints_sort:
            if k == 0:
                break
            else: 
                print i[0] + ' with ' + str(i[1]) + ' complaints'
                k -= 1

if __name__ == "__main__":
    filename = sys.argv[1]
    k = sys.argv[2]
    main(filename,k)