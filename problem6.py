import csv
import sys
from itertools import islice

def main(filename):
    with open(filename,'rb') as prob6:
        reader = csv.reader(prob6)
        depts_d = {}
        depts_l = []
        #for each key 'row[3]', append to the corresponding list
        # e.g. depts_d.setdefault('test',[]).append(3) yields {'test': [3]}
        # this loop creates a dictionary where departments are keys and values are lists of zipcodes
        for row in islice(reader,1,None):
            if not row[3] == '' and not row[7] == '':
                depts_d.setdefault(row[3],[]).append(row[7])
                if not row[3] in depts_l:
                    depts_l.append(row[3])
        depts_l = sorted(depts_l)
        for dept in depts_l:
            #create a dictionary where zip codes are keys and values are their counts in the depts_d dictionary
            counts = {}
            for zip in depts_d[dept]:
                if zip in counts:
                    counts[zip] += 1
                else:
                    counts[zip] = 1
            #create a list of the zips that have the highest values
            #this is a list because there could be multiple zips tied with the highest value
            high = []
            for zip in counts:
                high_val = 0
                if high_val == 0:
                    high.append(zip)
                    high_val = counts[zip]
                elif counts[zip] > high_val:
                    high_val = counts[zip]
                    high = []
                    high.append(zip)
                elif counts[zip] == high_val:
                    high.append(zip)
                high = sorted(high)
            print dept + " " + " ".join(high) + " " + str(high_val)

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)