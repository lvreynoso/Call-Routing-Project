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

# find the longest prefix, smallest price in solutions array
# return that price
# input: (prefix, price)
def findBestSolution(solutions):
    longestString = ''
    bestPrice = ''
    for i, rc in enumerate(solutions):
        route = rc[0]
        cost = rc[1]
        # print(route, cost)
        # find longer prefix
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
   # get all phone numbers -> dict
#    phoneDict = parsePhoneNumbers(phonePath)
   
    with open(routePath, 'r') as f:
        content = f.read()

    solutions = []
    for line in content.split('\n'):
        if (len(line) == 0):
            break
        data = line.split(",")
        # print(data)
        if (isPrefix(phoneNumber, data[0])):
            solutions.append((data[0], data[1]))
    
    return findBestSolution(solutions)

def writeToFile(solution):
    path = 'scenario2_solution.txt'
    with open(path, 'w') as f:
        f.write(str(solution))

def main(routePath, phonePath):
    with open(phonePath, 'r') as f:
        content = f.read()
    numbers = content.split('\n')
    
    solution = ''
    for number in numbers:
        if (len(number) == 0):
            break
        # print("Find cost for {number}: ".format(number = number))
        # start = time.time()
        cost = findCost(routePath, number)
        # end = time.time()
        # print("COST = {cost}".format(cost = cost))
        # print("Found cost in {time} seconds".format(time = end-start))

        solution += "{number}: {cost}\n".format(number = number, cost = cost)
    
    writeToFile(solution)

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
    # routePath = 'data/route-costs-100.txt'
    # routePath = 'data/route-costs-600.txt'
    routePath = 'data/route-costs-35000.txt'
    # routePath = 'data/route-costs-106000.txt'
    # routePath = 'data/route-costs-1000000.txt'
    # routePath = 'data/route-costs-1000000.txt'

    # phone paths to true
    # phonePath = 'data/phone-numbers-3.txt'
    # phonePath = 'data/phone-numbers-10.txt'
    phonePath = 'data/phone-numbers-100.txt'
    # phonePath = 'data/phone-numbers-10000.txt'


    start = time.time()
    main(routePath, phonePath)
    end = time.time()
    print("It took {time} seconds".format(time = end-start))
    print("Memory used: {mem} mb".format(mem = get_mem()))
