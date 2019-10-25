class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


def diameter(node):
   node_left,node_right,dia_left,dia_right=0,0,0,0
   if node is None:
      return 0
   else:
      if node.left:
         node_left = height(node.left)
      if node.right:
         node_right = height(node.right)
      if node.left:
         dia_left = diameter(node.left)
      if node.right:
         dia_right = diameter(node.right)
      return max(node_left + node_right, max(dia_left, dia_right))

def inorder(node):
  if node:
    if node.left:
       inorder(node.left)
    print(node.value)
    if node.right:
       inorder(node.right)


def height(node):
   queue = []
   len_queue = 0
   count = 0
   if node:
      queue.append(node)
   else:
      return 0
   while queue:
      len_queue = len(queue)
      if not len_queue:
         return count
      else:
         count = count + 1
      while len_queue:
         s = queue.pop(0)
         if s.left:
            queue.append(s.left)
         if s.right:
            queue.append(s.right)
         len_queue = len_queue - 1
   return count


if __name__ == "__main__":
   node = Node(1)
   node.left = Node(2)
   node.right = Node(3)
   node.left.left = Node(4)
   node.left.right = Node(5)
   print("The inorder traversal of the tree is")
   inorder(node)
   print("The diameter of the tree is")
   print(diameter(node))
   print("The height of the tree")
   print(height(node))

   
