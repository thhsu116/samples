# https://stackoverflow.com/questions/46126082/how-to-update-rows-in-a-csv-file

from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'my.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['ID', 'Name', 'Course', 'Year']

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        if row['ID'] == str(stud_ID):
            print('updating row', row['ID'])
            row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
        row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
        writer.writerow(row)

shutil.move(tempfile.name, filename)
