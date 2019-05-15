#!python

class RoutingTable(object):
    """RoutingTable is a simple dictionary-based data structure that
    stores keys and an associated tuple of data. For the project, this
    is enough. It's fast, easy, and cheap enough."""
    def __init__(self):
        self.table = {}
        self.size = 0

    def __str__(self):
        return str(self.table)

    def __repr__(self):
        return 'RoutingTable({} entries)'.format(self.size)

    # insert() inserts a key into the hashtable and updates
    # its associated value, storing any new data in a tuple.
    def insert(self, key, data=None):
        if key in self.table:
            if data is not None:
                entry = list(self.table[key])
                entry.append(data)
                self.table[key] = tuple(entry)
        else:
            self.table[key] = (data,)
            self.size += 1

    # lookup finds the longest entry in the hash table that
    # matches a given key and returns the lowest value
    # stored in that entry.
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




