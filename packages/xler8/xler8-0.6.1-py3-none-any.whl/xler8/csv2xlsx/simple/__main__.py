import xler8
import sys
import csv
import copy



infile = sys.argv[1]
sheetname = sys.argv[2]
outfile = sys.argv[3]

print("Reading %s into sheet %s in file %s" % (infile, sheetname, outfile))

data = []

with open(infile, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')


    hdrs=[]
    h_mode=True
    for row in csvreader:
        if h_mode:
            h_mode = False
            hdrs = copy.deepcopy(row)
            data.append(hdrs)
            continue

        data.append(row)
        # rd = dict(zip(hdrs, row))
        # print(rd)

xler8.xlsx_out(filename=outfile, sheets={
    sheetname: {
        'data': data
    }
})
