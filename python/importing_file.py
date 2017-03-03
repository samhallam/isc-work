import csv

with open('/tmp/serial-temperature.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print row
