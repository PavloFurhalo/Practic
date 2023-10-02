class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


def insert_element(self, data):
        """
        Вставляє новий вузол з даними `data` до початку списку.
        """
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

def find_element(self, data):
        """
        Перевіряє, чи присутній вузол з даними `data` у списку.
        Повертає True, якщо такий вузол існує, і False в іншому випадку.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

def select_element(self, index):
        """
        Повертає елемент на позиції `index` (індексація з нуля).
        Якщо такої позиції немає, повертає None.
        """
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current is not None else None

def get_previous_element(self, data):
        """
        Повертає дані попереднього вузла перед вузлом з даними `data`.
        Якщо такий вузол не існує, повертає None.
        """
        if self.head is None or self.head.data == data:
            return None

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            return current.data

