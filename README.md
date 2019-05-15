# Call-Routing-Project
Final project for CS 1.3

Note: Data files are not included in github due to file size restrictions. Add your own to see the magic, and change the file names at the bottom of the file.

## Scenario 1: One Time Route Cost Check
File: scenario1.py

Method: Find all possible route matches in the given routes file and return the best cost of the longest found route.

Run python3 scenario1.py. 

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

The cost gets way slower for larger files!

## Scenario 2: A list of Route Costs to check
File: scenario2.py

Method: Repeat scenario 1 on all given phone numbers. Write solutions to scenario2_solution.txt file.

Run python3 scenario2.py. (Note: Uncomment tests to try different file sizes at the end of file.)

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
The cost gets way slower for larger files! This is not a great method :(

But, it gets better ...

## Scenario 3: Multiple Long Carier Route Lists
File: radix.py

Method: Store routes and costs in a Radix Tree. Search for the longest route prefix that matches phone number, and return the cost.

TODO: running/testing instructions



## Scenario 4: High-throughout pricing API
File: hashtable.py

Method: Store routes and costs in a Python dictionary. Trim the phone number until a matching route is found, and return the cost.

TODO: running/testing instructions