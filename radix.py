#!python

class RadixNode(object):
    """docstring for RadixNode"""
    def __init__(self, label):
        self.label = label
        self.data = []
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0

 
class RadixTree(object):
    """docstring for RadixTree"""
    def __init__(self, items=None):
        self.root = RadixNode('__ROOT__')
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

    def _search(self, key):
        # start at root, keep track of the number of characters matched / elements found
        # make sure we only go as far as the key length
        node = self.root
        elementsFound = 0
        keyLength = len(key)
        # traverse through the tree. find edge, find next edge, rinse, repeat
        while node.isLeaf() == False and elementsFound < keyLength:
            nextNode = None
            # match only the relevant parts of the key
            suffix = key[elementsFound:]
            # look through all the node's edges for a prefix match
            for child in node.children:
                if self._isPrefix(suffix, child.label):
                    nextNode = child 
                    break
            if nextNode is None:
                break 
            else:
                node = nextNode
                elementsFound += len(nextNode.label)
        return (node, elementsFound)

    # TODO: Make this pretty printed, like the "tree" program
    def diagram(self):
        items = []
        if not self.empty():
            self._traversePreOrder(self.root, items.append)
        return items

    def empty(self):
        return self.size == 0

    def contains(self, key):
        node, elementsFound = self._search(key)
        return elementsFound == len(key)

    # return the data from the node with the closest match to the key
    def lookup(self, key):
        node, elementsFound = self._search(key)
        if node is self.root:
            raise KeyError('No mapping found for {}'.format(key))
        return node.data

    def insert(self, key, data=None):
        node, elementsFound = self._search(key)
        # Case 1: We hit an exact node!
        if elementsFound == len(key):
            if data is not None:
                node.data.append(data)
            return
        # look for a candidate edge/node
        candidateEdge = None
        suffix = key[elementsFound:]
        depth = 0
        for child in node.children:
            childMatchDepth = self._matchDepth(suffix, child.label)
            if childMatchDepth > 0:
                candidateEdge = child
                depth = childMatchDepth
                break
        # construct our new node
        newNode = RadixNode(suffix)
        if data is not None:
            newNode.data.append(data)
        # Case 2: Need to split an edge in two
        if candidateEdge is not None:
            # trim the old edge to just the unique part:
            candidateEdge.label = candidateEdge.label[depth:]
            # Case 2a: The new suffix is entirely contained within the edge
            # e.g. adding "test" to "tester"
            if depth == len(suffix):
                # connect the new edge to the node we stopped at
                node.children.append(newNode)
                # connect the old edge to our new node
                newNode.children.append(candidateEdge)
                # disconnect the old edge from the old parent
                node.children.remove(candidateEdge)
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
                newStem = RadixNode(suffix[:depth])
                # trim the new suffix
                newNode.label = newNode.label[depth:]
                # now connect it all together...
                node.children.append(newStem)
                newStem.children.extend([newNode, candidateEdge])
                node.children.remove(candidateEdge)
                self.size += 2
                return
        # Case 3: The key is longer than the current branch. Simple enough, just
        # add an edge with the rest of the key.
        # e.g. adding "slower" to "slow"
        else:
            node.children.append(newNode)
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

    print(rt.diagram())


if __name__ == '__main__':
    testRadixTree()
        
