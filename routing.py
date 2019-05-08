#!python

from radix import RadixTree
import sys, itertools, resource

def routeCall(number, data):
    result = []
    for index in range(len(number)):
        truncated = number[:len(number) - index]
        try:
            result = data.lookup(truncated)
        except KeyError:
            break
        if result != []:
            break
    if result != []:
        result.sort()
        return (number, result[0])
    else:
        return (number, 0)

def loadRoutes(path):
    tree = RadixTree()
    # load call routing data into Radix Tree
    # 1,000,000 routes uses 522 MiB
    spinner = itertools.cycle('-\\|/')
    print('Loading call routing data...', end='')
    count = 0
    with open(dataPath) as datafile:
        for line in datafile:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            entry = line.rstrip('\n').split(',')
            tree.insert(entry[0], entry[1])
            count += 1
            sys.stdout.write('\b')
    sys.stdout.write('Done.\n')
    sys.stdout.flush()
    print('{} routes processed'.format(count))
    print('Memory usage: {} MiB'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >> 20))
    return tree

def shell(data):
    # start a shell
    print('\nInteractive call routing shell.\nType a standardized phone number, beginning with \'+\' to lookup its routing cost.\nType \'exit\' to end the session.')
    call = ''
    while call != 'exit':
        call = input(">>> ")
        if call == 'exit':
            break
        else:
            print(routeCall(call, data))

def usage():
    helpString = """
    Usage: python3 radix.py path/to/routing/data path/to/call/data
    """
    print(helpString)
    exit()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    dataPath = sys.argv[1]
    # callPath = sys.argv[2]
    routes = loadRoutes(dataPath)
    shell(routes)
    