class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def is_full(tree):
#Перевіряє чи є дерево повним
  if tree is None:
    return True
  return (tree.left is not None and tree.right is not None) and \
    is_full(tree.left) and is_full(tree.right)

def is_perfect(tree):
#Перевіряє чи є дерево ідеальним
  if tree is None:
    return True
  return (tree.left is None or is_perfect(tree.left)) and \
    (tree.right is None or is_perfect(tree.right)) and \
    (tree.left is not None and tree.right is not None) and \
    (tree.left.data == (tree.data - 1) // 2) and \
    (tree.right.data == (tree.data - 1) // 2 + 1)

def is_complete(tree):
#Перевіряє чи є дерево повним
  if tree is None:
    return True
  return (tree.left is None or is_complete(tree.left)) and \
    (tree.right is None or is_complete(tree.right)) and \
    (tree.left is None or (tree.right is not None and tree.left.data < tree.right.data))

def is_balanced(tree):
#Перевіряє чи є дерево збалансованим
  if tree is None:
    return True
  return (abs(height(tree.left) - height(tree.right)) <= 1) and \
    is_balanced(tree.left) and is_balanced(tree.right)

def height(tree):
#Визначає висоту дерева
  if tree is None:
    return 0
  return 1 + max(height(tree.left), height(tree.right))

def main():
  tree = Node(1)
  tree.left = Node(2)
  tree.right = Node(3)
  tree.left.left = Node(4)
  tree.left.right = Node(5)

  print("Чи є дерево повним:", is_full(tree))
  print("Чи є дерево ідеальним:", is_perfect(tree))
  print("Чи є дерево повним:", is_complete(tree))
  print("Чи є дерево збалансованим:", is_balanced(tree))

if __name__ == "__main__":
  main()




