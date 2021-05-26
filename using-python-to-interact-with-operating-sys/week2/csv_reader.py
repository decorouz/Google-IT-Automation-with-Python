import csv

with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        firstname, lastname, street, city, state, zipcode = row
        print("Name: {} {}, Address: {}, city: {}, state: {}, zipcode: {}".format(
            firstname, lastname, street, city, state, zipcode))
