class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        if not self.head:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next

    def update(self, target, new_data):
        current = self.head
        while current:
            if current.data == target:
                current.data = new_data
                return
            current = current.next


# 创建一个链表
my_list = LinkedList()

# 增加数据
my_list.append(1)
my_list.append(2)
my_list.append(3)

# 显示链表
my_list.display()

# 查询数据
print("查找 2:", my_list.search(2))

# 删除数据
my_list.delete(2)
my_list.display()

# 修改数据
my_list.update(3, 4)
my_list.display()

# 查询数据
print("查找 2:", my_list.search(2))

# 删除数据
my_list.delete(2)
my_list.display()

# 修改数据
my_list.update(3, 4)
my_list.display()
