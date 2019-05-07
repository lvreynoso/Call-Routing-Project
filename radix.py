#!python

class RadixNode(object):
    """docstring for RadixNode"""
    def __init__(self):
        self.data = []
        self.edges = []

    def isLeaf(self):
        return len(self.edges) == 0


class RadixEdge(object):
    """docstring for RadixEdge"""
    def __init__(self, label):
        self.label = label
        self.node = RadixNode()

 
class RadixTree(object):
    """docstring for RadixTree"""
    def __init__(self, items=None):
        self.root = RadixNode()
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __str__(self):
        pass

    def __repr__(self):
        return 'RadixTree({} nodes)'.format(self.size)

    def _findNodeIterative(self, key):
        pass

    def _isPrefix(self, first, second):
        isPrefix = True 
        for index, character in enumerate(second):
            if index >= len(first):
                isPrefix = False
                break
            if character != first[index]:
                isPrefix = False
        return isPrefix

    def empty(self):
        return self.size == 0

    def contains(self, key):
        # start at root, keep track of the number of characters matched / elements found
        # make sure we only go as far as the key length
        node = self.root
        elementsFound = 0
        keyLength = len(key)

        # traverse through the tree. find edge, find next edge, rinse, repeat
        while node.isLeaf() == False and elementsFound < keyLength:
            nextEdge = None
            # match only the relevant parts of the key
            suffix = key[elementsFound:]
            # look through all the node's edges for a prefix match
            for edge in node.edges:
                if self._isPrefix(suffix, edge.label):
                    nextEdge = edge 
                    break

            if nextEdge is None:
                break 
            else:
                node = nextEdge.node
                elementsFound += len(nextEdge.label)

        return elementsFound == keyLength

    def lookup(self, key):
        pass

    def insert(self, key, data=None):
        node = self.root
        elementsFound = 0
        keyLength = len(key)

        # traverse through the tree and find the most appropriate node
        while node.isLeaf() == False and elementsFound < keyLength:
            nextEdge = None
            # match only the relevant parts of the key
            suffix = key[elementsFound:]
            # look through all the node's edges for a prefix match
            for edge in node.edges:
                if self._isPrefix(suffix, edge.label):
                    nextEdge = edge 
                    break

            if nextEdge is None:
                break 
            else:
                node = nextEdge.node
                elementsFound += len(nextEdge.label)

        # Case 1: We hit an exact node!
        if elementsFound == keyLength:
            if data is not None:
                node.data.append(data)
            return

        # look for a candidateEdge
        candidateEdge = None
        suffix = key[elementsFound:]
        for edge in node.edges:
            if self._isPrefix(edge.label, suffix):
                candidateEdge = edge
                break

        # construct our new edge
        newEdge = RadixEdge(suffix)
        if data is not None:
            newEdge.node.data.append(data)

        # Case 2: Need to split an edge in two
        if candidateEdge is not None:
            node.edges.append(newEdge)
            newEdge.node.edges.append(candidateEdge)
            candidateEdge.label = candidateEdge.label[len(suffix):]
            node.edges.remove(candidateEdge)
            self.size += 1
            return
        # Case 3: The key is longer than the current branch. Simple enough, just
        # add an edge with the rest of the key.
        else:
            node.edges.append(newEdge)
            self.size += 1
            return


    def delete(self):
        pass


def testRadixTree():
    rt = RadixTree()
    print(repr(rt))
    rt.insert("+44")
    print(repr(rt))
    rt.insert("+91")
    print(repr(rt))
    rt.insert("+4420")
    print(repr(rt))
    rt.insert("+4")
    print(repr(rt))
    rt.insert("+44")
    print(repr(rt))


if __name__ == '__main__':
    testRadixTree()
        
