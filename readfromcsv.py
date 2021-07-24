import dropbox
import csv

dbx = dropbox.Dropbox('HXbs__9V2IEAAAAAAAAAAUT_tdP51a21_yiGysC-MixwNyxqrWHqO1AajNbdO1lV')

metadata, f = dbx.files_download('/superlucky/TRVa/READY/settings.csv')

csv_reader = csv.reader(f.content.decode().splitlines(), delimiter=',')

line_count = 0
for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(row)
        line_count += 1

print(f'Processed {line_count} lines.')