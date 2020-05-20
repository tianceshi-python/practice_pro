# encoding:utf-8
class Node(object):
    '''创建一个点 '''
    def __init__(self,item):
        self.item = item
        self.next = None

def findloop(head):

    slow = head
    fast = head
    #创建一个标记
    loopExist = False
    #如果头节点为空，直接返回
    if head == None:
        return False
    print('findloop head is:', head)
    #只要2个游标不为空就一直循环
    #2个游标一快一慢，终会相遇
    while fast.next != None and fast.next.next != None:
        #快游标
        fast = fast.next.next

        #慢游标
        slow = slow.next
        if slow == fast:
            #游标相遇，返回True,并跳出循环
            loopExist = True
            break
    if loopExist == True:
        #如果相遇，说明有环
        slow = head
        #将慢游标从头节点重新开始
        while slow != fast:
            slow = slow.next
            fast = fast.next

        #相等以后返回环的头节点
        return slow.item

    return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1


if findloop(node1):
    print('存在环')
    print('findloop(node1) is :',findloop(node1))

else:
    print('不存在环结构')