# Call-Routing-Project
###By Lucia Reynoso and Anisha Jain 

###Final project for Make School's Data Structures and Algorithms Class


Note: Data files are not included in github due to file size restrictions. Add your own to see the magic, and change the file names at the bottom of the file.

## Scenario 1: One Time Route Cost Check
File: scenario1.py

Method: Find all possible route matches in the given routes file and return the best cost of the longest found route.

### How to Test:
Run python3 scenario1.py. 

### Cost and Memory usage examples
```
Find cost for +449275049230: in data/route-costs-10.txt
COST = 0.49
Found cost in 0.00012683868408203125 seconds
Memory used: 10.79 mb


Find cost for +449275049230: in data/route-costs-35000.txt
COST = None
Found cost in 0.04637885093688965 seconds
Memory used: 14.3 mb


Find cost for +449275049230: in data/route-costs-106000.txt
COST = None
Found cost in 0.1418302059173584 seconds
Memory used: 21.14 mb


Find cost for +449275049230: in data/route-costs-10000000.txt
COST = 0.44
Found cost in 13.056149005889893 seconds
Memory used: 855.34 mb
```

The cost gets too expensive for larger files!

## Scenario 2: A list of Route Costs to check
File: scenario2.py

Method: Repeat scenario 1 on all given phone numbers. Write solutions to scenario2_solution.txt file.

### How to Test:
Run python3 scenario2.py. (Note: Uncomment tests to try different file sizes at the end of file.)

### Cost and Memory usage examples
```
Find cost for data/phone-numbers-10.txt: in data/route-costs-600.txt
Found costs in 0.01481008529663086 seconds
Memory used: 10.65 mb

Find cost for data/phone-numbers-100.txt: in data/route-costs-35000.txt
Found costs in 4.037954092025757 seconds
Memory used: 15.52 mb

Find cost for data/phone-numbers-100.txt: in data/route-costs-1000000.txt
Found costs in 126.59851789474487 seconds
Memory used: 119.3 mb

```
The cost is way too expensive for larger files! This is not a great method :(

Potential improvement for this method: Instead of looping over the file multiple times, add all potential solutions for each phone number to a dictionary when it is found. Then find the best solution for each phone number and return that. This will be faster because it would only loop over the file once.

But, it gets better ...

### Testing Instructions for the upcoming BETTER solutions:


## Scenario 3: Multiple Long Carier Route Lists
File: radix.py

Method: Store routes and costs in a Radix Tree. Search for the longest route prefix that matches phone number, and return the cost.

### How to Test:
In routing.py, look at the bottom of the file. Make the changes shown below, so that you are using RadixTree as the table.
```
if table is None:
    # table = RoutingTable()
    table = RadixTree()
```

Run python3 routing.py
Follow terminal instructions

### Cost and Memory usage examples


## Scenario 4: High-throughout pricing API
File: hashtable.py

Method: Store routes and costs in a Python dictionary. Trim the phone number until a matching route is found, and return the cost.

### How to Test:
In routing.py, look at the bottom of the file. Make the changes shown below, so that you are using RoutingTable as the table. Routing Table is the hashtable implementation shown in hashtable.py. It simply uses the python dictionary.

```
if table is None:
    table = RoutingTable()
    # table = RadixTree()
```

Run python3 routing.py
Follow terminal instructions

### Cost and Memory usage examples