#!python

from hashtable import RoutingTable
import sys, itertools, resource, csv

def loadRoutes(path, datastore):
    # load call routing data into hashtable-based Routing Table
    # 1,000,000 routes now only uses 203 MiB!
    spinner = itertools.cycle('-\\|/')
    print('Loading call routing data...', end='')
    count = 0
    with open(path) as datafile:
        reader = csv.reader(datafile, delimiter=',')
        for row in reader:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            datastore.insert(row[0], row[1])
            count += 1
            sys.stdout.write('\b')
    sys.stdout.write('Done.\n')
    sys.stdout.flush()
    print('{} routes processed'.format(count))
    print('Memory usage: {} MiB'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >> 20))

def shell(data):
    # start a shell
    print('\nInteractive call routing shell.\nType a standardized phone number, beginning with \'+\' to lookup its routing cost.\nType \'exit\' to end the session.')
    call = ''
    while call != 'exit':
        call = input(">>> ")
        if call == 'exit':
            break
        else:
            print(call, data.lookup(call))

if __name__ == '__main__':
    costsPath = sys.argv[1]
    table = RoutingTable()
    loadRoutes(costsPath, table)
    shell(table)