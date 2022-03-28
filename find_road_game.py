import sys

class Node:
    def __init__(self, id, x ,y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    # sort()함수는 기본적으로 오름차순인데
    def __lt__(self ,other): # self < other 재정의
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y

def addNode(parent ,child):
    if parent.x < child.x:
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)
    else:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left ,child)

def preorder(arr , node):
    if node == None:
        return

    arr.append(node.id)
    preorder(arr ,node.left)
    preorder(arr ,node.right)

def postorder(arr, node):
    if node == None:
        return

    postorder(arr ,node.left)
    postorder(arr ,node.right)
    arr.append(node.id)


def solution(nodeinfo):
    sys.setrecursionlimit(1500)

    size = len(nodeinfo)
    Nodes = []
    for i in range(size):
        Nodes.append(Node( i +1 ,nodeinfo[i][0] ,nodeinfo[i][1]))

    Nodes.sort()
    root = Nodes[0]

    for i in range(1, size):
        addNode(root, Nodes[i])


    answer = [[] , []]

    preorder(answer[0], root)
    postorder(answer[1], root)


    return answer