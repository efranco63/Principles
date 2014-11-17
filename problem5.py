import csv
import sys
from itertools import islice
from time import strftime
from dateutil import parser

def main(filename):
    with open(filename,'rb') as prob5:
        reader = csv.reader(prob5)
        weekdays = {}
        day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        for row in islice(reader,1,None):
            weekday = parser.parse(row[1]).strftime('%A')
            if weekday in weekdays.keys():
                weekdays[weekday] += 1
            else:
                weekdays[weekday] = 1
        for i in day_names:
            if i in weekdays.keys():
                print str(i) + " == " + str(weekdays[i])
            else:
                print str(i) + " == 0"

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)