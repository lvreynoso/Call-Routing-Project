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

    def _isPrefix(self, first, second):
        isPrefix = True 
        for index, character in enumerate(second):
            if index >= len(first):
                isPrefix = False
                break
            if character != first[index]:
                isPrefix = False
                break
        return isPrefix

    def _sharesStem(self, suffix, edgeLabel):
        return suffix[0] == edgeLabel[0]

    def _matchDepth(self, suffix, edgeLabel):
        depth = 0
        for index, character in enumerate(suffix):
            if index >= len(edgeLabel):
                break
            elif character != edgeLabel[index]:
                break
            else:
                depth += 1
        return depth


    def _traversePreOrder(self, node, visit):
        for edge in node.edges:
            visit(edge.label)
            self._traversePreOrder(edge.node, visit)

    def diagram(self):
        items = []
        if not self.empty():
            self._traversePreOrder(self.root, items.append)
        print(items)

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
            if self._sharesStem(edge.label, suffix):
                candidateEdge = edge
                break

        # Case 2: Need to split an edge in two
        if candidateEdge is not None:
            depth = self._matchDepth(suffix, candidateEdge.label)
            # Case 2a: The new suffix is entirely contained within the edge
            # e.g. adding "test" to "tester"
            if depth == len(suffix):
                # construct our new edge
                newEdge = RadixEdge(suffix)
                if data is not None:
                    newEdge.node.data.append(data)
                node.edges.append(newEdge)
                newEdge.node.edges.append(candidateEdge)
                candidateEdge.label = candidateEdge.label[len(suffix):]
                node.edges.remove(candidateEdge)
                self.size += 1
                return
            # Case 2b: The new suffix only contains a partial match to the 
            # candidate edge. This means we need to create *two* new edges.
            # One for the shared stem and one for the new suffix. We need to
            # trim the label for the old edge to just the unique part.
            # Finally, we need to connect the old suffix and the new suffix
            # to the new shared stem.
            # e.g. adding "team" to "test"
            elif depth < len(suffix):
                # create shared stem:
                newStem = RadixEdge(suffix[:depth])
                # trim the new suffix and create an edge for it
                newEdge = RadixEdge(suffix[depth:])
                if data is not None:
                    newEdge.node.data.append(data)
                # trim the old edge to just the unique part:
                candidateEdge.label = candidateEdge.label[depth:]
                # now connect it all together...
                node.edges.append(newStem)
                newStem.node.edges.extend([newEdge, candidateEdge])
                node.edges.remove(candidateEdge)
                self.size += 2
                return

        # Case 3: The key is longer than the current branch. Simple enough, just
        # add an edge with the rest of the key.
        # e.g. adding "slower" to "slow"
        else:
            newEdge = RadixEdge(suffix)
            if data is not None:
                newEdge.node.data.append(data)
            node.edges.append(newEdge)
            self.size += 1
            return


    def delete(self):
        pass


def testRadixTree():
    rt = RadixTree()
    print(repr(rt))

    fullNumbers = ['+15552998210', '+44201']
    items = ['+44', '+91', '+4420', '+4', '+44', '+9185']
    for item in items:
        print('Inserting {}'.format(item))
        rt.insert(item)
        print(repr(rt))

    for item in items:
        result = rt.contains(item)
        print("Tree contains {}: {}".format(item, result))

    for item in fullNumbers:
        result = rt.contains(item)
        print("Tree contains {}: {}".format(item, result))

    rt.diagram()


if __name__ == '__main__':
    testRadixTree()
        
