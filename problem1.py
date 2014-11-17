import csv
import sys
from itertools import islice
from time import strftime
from dateutil import parser

def main(filename):
    with open(filename,'rb') as prob1:
        reader = csv.reader(prob1)
        rownum = 0
        min_time = '01/20/2050 12:00:00 AM'
        max_time = '01/20/1950 12:00:00 AM'
        # islice allows you to skip the first row
        for row in islice(reader,1,None):
            rownum += 1
            min_time = min(min_time,row[1])
            max_time = max(max_time,row[2])
        #convert the min_time and max_time to datetime format and then to military times with strftime
        min_time = parser.parse(min_time).strftime('%m/%d/%Y %H:%M:%S')
        max_time = parser.parse(max_time).strftime('%m/%d/%Y %H:%M:%S')
        print str(rownum)+' complaints between '+str(min_time)+' and '+str(max_time)

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)