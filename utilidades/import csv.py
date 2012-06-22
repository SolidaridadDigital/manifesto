import csv
f = csv.reader(open('iso3166.csv'), delimiter=';')

result = {}

for row in f:
	print row

'''for code, english, spanish in f:
    result[code] = english, spanish

# pretty-prints the result:
from pprint import pprint
pprint(result)
'''