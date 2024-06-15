# 백준 1991

N = int(input())


tree = [None] * (2**(N-1))

for _ in range(N):
    root, left, right = input().split()
    if root == 'A':
        tree[0] = root
    root_index = tree.index(root)
    if left != '.':
        tree[root_index * 2 + 1] = left
    if right != '.':
        tree[root_index * 2 + 2] = right

def preorder(tree, i=0):
    if i < len(tree):
        print(tree[i], end = "")
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            preorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            preorder(tree, right)

def inorder(tree, i=0):
    if i < len(tree) or tree[i] is not None:
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            inorder(tree, left)
        print(tree[i], end="")
        if right < len(tree) and tree[right] is not None:
            inorder(tree, right)

def postorder(tree, i=0):
    if i < len(tree) or tree[i] is not None:
        left = 2 * i + 1
        right = left + 1
        if left < len(tree) and tree[left] is not None:
            postorder(tree, left)
        if right < len(tree) and tree[right] is not None:
            postorder(tree, right)
        print(tree[i], end="")


preorder(tree)
print("")
inorder(tree)
print("")
postorder(tree)