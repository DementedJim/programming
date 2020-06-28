'''
Иванов Дмитрий, ИВТ3
'''

import csv

def read(text):
    with open("data.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in text:
            writer.writerow(line.replace('"', '').replace('\n', '').replace('[','').replace(']','').replace('{','').replace('}','').split(','))
            
if __name__ == "__main__":
    with open("data.txt") as data_log:
        read(data_log)
        print("Файл создан: data.csv")