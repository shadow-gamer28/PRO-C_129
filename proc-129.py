import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'
d1 = []
d2 = []
with open(file1,'r') as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        d1.append(i)   
with open(file2,'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d2.append(i)
h1 = d1[0]
h2 = d2[0]
p_d1 = d1[1:]
p_d2 = d2[1:]
h = h1+h2
p_d =[]
for index , data_row in enumerate(p_d1):
    p_d.append(p_d1[index]+p_d2[index])
with open("total_stars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
df = pd.read_csv('total_stars.csv')
df.tail(8)