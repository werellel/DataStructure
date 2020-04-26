class Node(object):
    nodeNext = ''
    objValue = ''
    binHead = False
    binTail = False
    """docstring for Node"""
    def __init__(self, objValue = '', nodeNext= '', binHead = False, binTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail
        
    def getValue(self):
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue
    def getNext(self):
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def isHead(self):   
        return self.binHead
    def isTail(self):
        return self.binTail

if __name__ == '__main__':
    node1 = Node(objValue = 'a')
    nodeTail = Node(binTail = True)
    nodeHead = Node(binHead = True, nodeNext = node1)
    print(node1.getValue(   ))