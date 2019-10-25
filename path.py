class Node:
  def __init__(self,value):
    self.value=value
    self.left=None
    self.right=None

def find_path(node,n1,path):
    if node is None:
       return False
    path.append(node.value)
    if node.value==n1:
       return True
    if (node.left and find_path(node.left,n1,path)) or (node.right and find_path(node.right,n1,path)):
       return True
    path.pop()
    return False


if __name__=="__main__":
   path=[]
   node=Node(1)
   node.left=Node(2)
   node.right=Node(3)
   node.left.left=Node(4)
   node.left.right=Node(5)
   node.right.left=Node(6)
   node.right.right=Node(7)
   print(find_path(node,7,path))
   print(path)
   