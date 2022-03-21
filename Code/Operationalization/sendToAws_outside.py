from csv import reader
from time import sleep
# skip first line i.e. read header first and then iterate over each row od csv as a list
url_inside = '../../Data/Processed/out.csv'

with open(url_inside, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row)
            sleep(4)

