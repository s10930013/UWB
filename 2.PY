import csv
with open("xy.csv",mode="w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([1,2,3])