import time

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


def main(routePath, number):
    print("Find cost for {number}: ".format(number = number))
    start = time.time()
    cost = findCost(routePath, number)
    end = time.time()
    print("COST = {cost}".format(cost = cost))
    print("Found cost in {time} seconds".format(time = end-start))

if __name__ == '__main__':
    routePath = 'data/route-costs-10.txt'
    phoneNumber = '+449275049230'
    
    main(routePath, phoneNumber)
