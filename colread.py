import csv
filename = input("Enter the csv file name(with .csv extension):")
colread = input("Enter column indicates to read(cooma-seperated,startinf from 0):")
colread = [int(x.strip()) for x in colread.split(",")]
with open(filename,'r') as csvfile1:
           csvreader = csv.reader(csvfile1)
           for row in csvreader:
               selectcol=[row[col] for col in colread if col<len(row)]
               print(selectcol)
