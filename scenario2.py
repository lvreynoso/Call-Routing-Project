import time
import resource
import platform

# check if prefix is a valid prefix for phoneNumber
def isPrefix(phoneNumber, prefix):
    if len(prefix) > len(phoneNumber):
        return False
    
    for i in range(len(prefix)):
        if (phoneNumber[i] != prefix[i]):
            return False
    
    return True

# find the price for the longest route with smallest price 
# in input array containing tuples: (prefix, price)
def findBestSolution(solutions):
    longestString = ''
    bestPrice = ''
    for i, rc in enumerate(solutions):
        route = rc[0]
        cost = rc[1]
        # found longer matching route
        if (len(route) > len(longestString)):
            longestString = route
            bestPrice = cost
        # found better price for same length route
        elif (len(route) == len(longestString) and bestPrice < cost):
            longestString = route
            bestPrice = cost

    if (len(bestPrice) == 0):
        return None
    return bestPrice

# finds the cost for one phone number
def findCost(routePath, phoneNumber):
    with open(routePath, 'r') as f:
        content = f.read()

    solutions = []
    # loop through all routes data
    for line in content.split('\n'):
        if (len(line) == 0):
            break
        data = line.split(",")# split line into [route, cost]
        # check if the route is a prefix for our phone number
        if (isPrefix(phoneNumber, data[0])):
            solutions.append((data[0], data[1]))
    
    return findBestSolution(solutions)

# writes all solutions to solution file
def writeToFile(solution):
    path = 'scenario2_solution.txt'
    with open(path, 'w') as f:
        f.write(str(solution))

# find costs for all phone numbers
def main(routePath, phonePath):
    with open(phonePath, 'r') as f:
        content = f.read()
    numbers = content.split('\n')
    
    solution = ''
    # loop over all phone numbers
    for number in numbers:
        if (len(number) == 0):
            break
        # find its best cost
        cost = findCost(routePath, number)
        # add it to the solution string
        solution += "{number}: {cost}\n".format(number = number, cost = cost)
    
    writeToFile(solution)

# Cite: get_mem from KJ's code
def get_mem():
    """
    returns current memory usage in mb.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        return round(usage/float(1 << 10), 2)
    return round(usage/float(1 << 20), 2)

if __name__ == '__main__':
    # route paths to try
    # routePath = 'data/route-costs-10.txt'
    routePath = 'data/route-costs-100.txt'
    # routePath = 'data/route-costs-600.txt'
    # routePath = 'data/route-costs-35000.txt'
    # routePath = 'data/route-costs-106000.txt'
    # routePath = 'data/route-costs-1000000.txt'
    # routePath = 'data/route-costs-1000000.txt'

    # phone paths to true
    # phonePath = 'data/phone-numbers-3.txt'
    phonePath = 'data/phone-numbers-10.txt'
    # phonePath = 'data/phone-numbers-100.txt'
    # phonePath = 'data/phone-numbers-10000.txt'

    print("Find cost for {phonePath}: in {path}".format(phonePath = phonePath, path = routePath))
    start = time.time()
    main(routePath, phonePath)
    end = time.time()
    print("Found costs in {time} seconds".format(time = end-start))
    print("Memory used: {mem} mb".format(mem = get_mem()))
