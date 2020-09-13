from binarytree import build 
class Solution(object):
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None

        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left

        return parent

n=int(input())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes) 
val=Solution()
print(val.upsideDownBinaryTree(binary_tree))
