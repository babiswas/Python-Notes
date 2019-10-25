class Node:
   def __init__(self,value):
       self.value=value
       self.right=None
       self.left=None

def lca(node,n1,n2):
   if node is None:
     return None
   else:
     if node.value==n1 and node.value==n2:
        return node
     else:
        node_left=lca(node.left,n1,n2)
        node_right=lca(node.right,n1,n2)
        if node_left and node_right:
           return node
        return node_left if node_left else node_right

def find(node,n1):
   if not node:
     return False
   else:
     if node.value==n1:
        return True
     else:
        return (find(node.left,n1) or find(node.right,n1))

if __name__=="__main__":
   node=Node(1)
   node.left=Node(2)
   node.right=Node(3)
   node.left.left=Node(4)
   node.left.right=Node(5)
   node.right.left=Node(6)
   node.right.right=Node(7)
   print(find(node,4))
   print(find(node,6))
   print(lca(node,4,6))


   
   



