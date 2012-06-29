import csv
#f = csv.reader(open('iso3166.csv'), delimiter=';')

#f = f.delete(f,0,2)

#for row in f:
#	print row


with open('iso3166.csv', 'rb') as countries:
        data = [(row['Code'], row['English']) for row in csv.DictReader(countries)]

        print data
        print type(data)