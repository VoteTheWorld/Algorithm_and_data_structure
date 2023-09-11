"""
使用两个class,主要是为了快速识别出head,相当于这里有两层内容,一层是node,一层是链
"""

"""
def __init__(self) 表示初始化class的时候,会自动执行的函数,这里的self表示class本身,相当于js中的this
"""

"""
def __repr__(self) 表示当print一个class的时候,会自动执行的函数
"""


class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    # def __lt__(self, other):
    #     return self.data < other.data


class linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """add a new node at the head of the list"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """search for the first node containing data that matches the key"""
        current = self.head

        while current:
            if current.data == key:
                return True
            else:
                current = current.next_node
        return False

    def remove(self, key):
        """remove node that first contains the key"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return "%s was removed" % current.data

    def insert(self, data, index):
        """insert a new node at the given index"""
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = Node.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def delete(self, index):
        """delete node at given index"""
        current = self.head
        prev_node = None

        if index == 0:
            self.head = current.next_node
            return "%s was deleted" % current.data
        else:
            while index > 0:
                prev_node = current
                current = current.next_node
                index -= 1

        prev_node.next_node = current.next_node
        return "%s was deleted" % current.data

    def node_at_index(self, index):
        current = self.head
        position = 0
        while position < index:
            current = current.next_node
            position += 1
        return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head is: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail is: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)


l = linked_list()

l.add(13)
l.add(26)
l.add(48)
l.add(27)
l.add(3)
l.add(548)
l.add(17)
l.add(7)
l.add(5)
l.add(19)

print(l)
