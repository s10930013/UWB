import csv

def calculate_accuracy(csv_file):
    total_count = 0
    inside_range_count = 0
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            total_count += 1
            x, y, _, _ = row  
            x = float(x)
            y = float(y)
            if 460 < x < 540 and 460 < y < 540:  
                inside_range_count += 1

    if total_count == 0:
        return 0
    else:
        return inside_range_count / total_count

csv_file = 'C:/Users/20171226/Desktop/UWB/測量結果/C2.csv'
accuracy = calculate_accuracy(csv_file)
print(f"B1.csv 文件中tag的準確率: {accuracy}")
