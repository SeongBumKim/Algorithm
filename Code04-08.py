#함수
class Node():
    def __init__(self) :
        self.data = None
        self.link = None


def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while(current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData): #다현, 화사
    global memory, head, current, pre
    if findData == head.data : #첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    #중간노드 삽입    
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    #마지막에 추가하기
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return



#전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']



#메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] : 
    pre = node 
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
insertNode('다현', '화사')
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)