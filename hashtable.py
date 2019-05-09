#!python

class RoutingTable(object):
    """docstring for RoutingTable"""
    def __init__(self):
        self.table = {}
        self.size = 0

    def __str__(self):
        return str(self.table)

    def __repr__(self):
        return 'RoutingTable({} entries)'.format(self.size)

    def insert(self, key, data=None):
        if key in self.table:
            entry = list(self.table[key])
            if data is not None:
                entry.append(data)
            self.table[key] = tuple(entry)
        else:
            self.table[key] = (data,)
            self.size += 1

    def lookup(self, key):
        result = '0'
        for index in range(len(key)):
            truncated = key[:len(key) - index]
            if truncated in self.table:
                costs = list(self.table[truncated])
                sortedCosts = sorted(costs)
                result = sortedCosts[0]
                break
        return result




