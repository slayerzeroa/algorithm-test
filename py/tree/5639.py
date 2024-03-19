# # 백준 5639

# class Node:
#     def __init__(self, value):
#         # linked list
#         self.value = value
#         self.left = None
#         self.right = None


# class NodeMgmt:
#     def __init__(self, head):
#         self.head = head

#     def insert(self, value):
#         self. current_node = self.head
#         while True:
#             if value < self.current_node.value:
#                 if self.current_node.left != None:
#                     self.current_node = self.current_node.left
#                 else:
#                     self.current_node.left = Node(value)
#                     break
#             else:
#                 if self.current_node.right != None:
#                     self.current_node = self.current_node.right
#                 else:
#                     self.current_node.right = Node(value)
#                     break

#     def postorder(self, n):
#         if n!= None:
#             if n.left:
#                 self.postorder(n.left)
#             if n.right:
#                 self.postorder(n.right)
#             print(n.value, '', end='')

# head = Node(int(input()))
# BST = NodeMgmt(head)
# while True:
#     try:
#         BST.insert(int(input()))
#     except:
#         break

# BST.postorder(head)


def dic_insert(curr, num):
    global root
    if len(binary_tree) == 0:
        root = num
        binary_tree[root]=['*', '*']
    else:
        if num<curr:
            if binary_tree[curr][0] == '*':
                binary_tree[curr][0] = num
                binary_tree[num] = ['*', '*']
            else:
                dic_insert(binary_tree[curr][0], num)
        else:
            if binary_tree[curr][1] == '*':
                binary_tree[curr][1]=num
                binary_tree[num]=['*', '*']
            else:
                dic_insert(binary_tree[curr][1], num)

def postorder(root):
    if binary_tree[root][0]!="*":
        postorder(binary_tree[root][0])
    if binary_tree[root][1]!="*":
        postorder(binary_tree[root][1])
    print(root,end=" ")

binary_tree={}
root=None
while True:
    try:
        dic_insert(root,int(input()))
    except:
        break

postorder(root)
