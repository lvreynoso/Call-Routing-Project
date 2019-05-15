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
    longestString = '' # track longest matching route
    bestPrice = '' # track best price for longest matching route
    
    # loop through all potential cost solutions
    for i, rc in enumerate(solutions):
        route = rc[0]
        cost = rc[1]
        # found longest matching route
        if (len(route) > len(longestString)):
            longestString = route
            bestPrice = cost
        # found better price for same length
        elif (len(route) == len(longestString) and bestPrice < cost):
            longestString = route
            bestPrice = cost

    if (len(bestPrice) == 0):
        return None
    return bestPrice


def findCost(routePath, phoneNumber):
    # open routes file
    with open(routePath, 'r') as f:
        content = f.read()

    solutions = []
    # loop through all routes data
    for line in content.split('\n'):
        if (len(line) == 0):
            break
        data = line.split(",") # split line into [route, cost]
        # check if the route is a prefix for our phone number
        if (isPrefix(phoneNumber, data[0])):
            solutions.append((data[0], data[1]))
    
    return findBestSolution(solutions)

# test our search for time and memory
def main(routePath, number):
    print("Find cost for {number}: in {path}".format(number = number, path = routePath))
    start = time.time()
    cost = findCost(routePath, number)
    end = time.time()
    print("COST = {cost}".format(cost = cost))
    print("Found cost in {time} seconds".format(time = end-start))
    print("Memory used: {mem} mb".format(mem = get_mem()))

#Cite: get_mem from KJ's code
def get_mem():
    """
    returns current memory usage in mb.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        return round(usage/float(1 << 10), 2)
    return round(usage/float(1 << 20), 2)

if __name__ == '__main__':
    routePath = 'data/route-costs-10.txt'
    phoneNumber = '+449275049230'
    main(routePath, phoneNumber)
    print('\n')
    
    routePath = 'data/route-costs-106000.txt'
    phoneNumber = '+449275049230'
    main(routePath, phoneNumber)
    print('\n')

    routePath = 'data/route-costs-10000000.txt'
    phoneNumber = '+449275049230'
    main(routePath, phoneNumber)
    print('\n')
