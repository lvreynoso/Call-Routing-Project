#!python

# from radix import RadixTree
from hashtable import RoutingTable
import sys, itertools, resource, csv, pickle

def loadRoutes(path, datastore):
    try:
        count = 0
        with open(path) as datafile:
            reader = csv.reader(datafile, delimiter=',')
            for row in reader:
                datastore.insert(row[0], row[1])
                count += 1
                print(f'\rLoading call routing data...{count} routes processed.', end='')
        sys.stdout.write('\n')
        sys.stdout.flush()
        print('Routing table entries: {}'.format(datastore.size))
        print('Memory usage: {} MiB'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >> 20))
    except Exception as e:
        print('Unable to load routes from {}: {}'.format(path, e))
        return Error('loadRouteError')

def priceRoutes(path, datastore):
    try:
        count = 0
        results = []
        with open(path) as datafile:
            reader = csv.reader(datafile, delimiter=',')
            for row in reader:
                price = datastore.lookup(row[0])
                results.append((row[0], price))
                count += 1
                print(f'\rPricing phone numbers...{count} processed.', end='')
        sys.stdout.write('\nWriting to file...')
        savePath = ''.join([path[:len(path) - 4], '-priced.txt'])
        with open(savePath, 'w') as printfile:
            writer = csv.writer(printfile)
            writer.writerows(results)
        sys.stdout.flush()
        print('wrote {} prices to {}'.format(count, savePath))
    except Exception as e:
        print('Unable to price routes to {}: {}'.format(path, e))

def shell(data):
    # start a shell
    instructions = """
    Interactive call routing shell.
    Type a standardized phone number, beginning with \'+\' to lookup its routing cost.
    'load path/to/routing/costs' to load a CSV table of routing costs into memory.
    'price path/to/phone/numbers' to price a CSV table of phone numbers.
    'save' to save the current routing table to disk. 
    'exit' to end the session.
    """
    print(instructions)
    command = ''
    while command != 'exit':
        command = input(">>> ")
        commands = command.rstrip('\n').split(' ')
        if commands[0] == 'exit':
            print('Cleaning up...')
            break
        elif commands[0] == 'load':
            for path in commands[1:]:
                loadRoutes(path, data)
        elif commands[0] == 'price':
            for path in commands[1:]:
                priceRoutes(path, data)
        elif commands[0] == 'save':
            saveCache(data)
        else:
            print(commands[0], data.lookup(commands[0]))

def loadCache():
    print('\rLoading routing table from disk...', end='')
    try:
        with open('__pycache__/routingcache', 'rb') as cachefile:
            data = pickle.load(cachefile)
            print('Done.')
            print('Routing table entries: {}'.format(data.size))
            print('Memory usage: {} MiB'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >> 20))
            return data
    except Exception as e:
        print('No saved routing table found')
        return None

def saveCache(data):
    print('\rSaving routing table to disk...', end='')
    try:
        with open('__pycache__/routingcache', 'wb') as cachefile:
            pickle.dump(data, cachefile)
            print('Routing table saved successfully!')
    except Exception as e:
        print('Unable to save routing table: {}'.format(e))
    return

if __name__ == '__main__':
    # Load from cache
    table = loadCache()
    if table is None:
        table = RoutingTable()
        # table = RadixTree()
    # Clean load
    # table = RadixTree()
    # table = RoutingTable()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            loadRoutes(arg, table)
    shell(table)