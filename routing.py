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
    tree = RadixTree()

    # load call routing data into Radix Tree
    # 1,000,000 routes uses 522 MiB
    spinner = itertools.cycle('-\\|/')
    print('Loading call routing data...', end='')
    with open(dataPath) as datafile:
        for line in datafile:
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            entry = line.split(',')
            tree.insert(entry[0], entry[1])
            sys.stdout.write('\b')
    sys.stdout.write('Done.\n')
    sys.stdout.flush()
    print('Memory usage: {} MiB'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >> 20))
