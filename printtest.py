#!python

import routing
import timeit, csv, time

table = routing.loadCache()
path = 'data/phone-numbers-10000.txt'

def tenThousand():
    count = 0
    with open(path) as datafile:
            reader = csv.reader(datafile, delimiter=',')
            for row in reader:
                price = table.lookup(row[0])
                print('Cost to call {}: {}'.format(row[0], price))
                count += 1

if __name__ == '__main__':
    statement = 'tenThousand()'
    result = timeit.timeit(statement, setup='from __main__ import tenThousand', number=100)
    print('Average time to print 10,000 numbers: {} seconds'.format(result / 100))