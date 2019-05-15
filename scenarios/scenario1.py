
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
    for route, cost in enumerate(solutions):
        # find longer prefix
        if (len(route) > len(longestString)):
            longestString = route
            bestPrice = cost
        # found better price for same length
        elif (len(route) == len(longestString) and bestPrice < cost):
            longestString = route
            bestPrice = cost

    return cost


def main(routePath, phoneNumber):
   # get all phone numbers -> dict
#    phoneDict = parsePhoneNumbers(phonePath)
   
    with open(routePath, 'r') as f:
        content = f.read()

    solutions = []
    for line in content.split('\n'):
        data = line.split(",")
        if (isPrefix(phoneNumber, data[0])):
            solutions.append((data[0], data[1]))
    
    return findBestSolution(solutions)



if __name__ == '__main__':
    main()