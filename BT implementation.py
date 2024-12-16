from binarytree import BinaryTree

def buildTree(val):    #Time Complexity: O(n). Space Complexity: O(n).
    if len(val)==0 or val[0] is None:
        return None
    root=BinaryTree(val[0])
    nodes=[root]
    i=1 #For tracking of item in val
    n=0 #For tracking of item in nodes
    while i < len(val):
        parent = nodes[n]
        if i < len(val) and val[i] is not None:
            parent.addlc(val[i])
            nodes.append(parent.lc)
        i += 1
        if i < len(val) and val[i] is not None:
            parent.addrc(val[i])
            nodes.append(parent.rc)
        i += 1
        n += 1
    return root

def search(node,target):    #Time Complexity: O(n). Space Complexity: O(n).
    if node is None:
        return [None,0]
    if node.item==target:
        return [node,1]
    if node.lc is not None and node.lc.item==target:
        return [node,2]
    if node.rc is not None and node.rc.item==target:
        return [node,3]
    x=search(node.lc,target)
    if x[0] is not None:
        return x
    return search(node.rc,target)
            

values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', None, 'H', None, None, 'I']
root = buildTree(values)
print("Breadth-First Traversal:")
root.TraverseBreadthFirst()
print("Tree constructed successfully!")

target = "B"
result = search(root, target)
if result[0] is not None:
    if result[1] == 1:
        print(f"\nTarget {target} found at the root.")
    elif result[1] == 2:
        print(f"\nTarget {target} found as the left child of node {result[0].item}.")
    elif result[1] == 3:
        print(f"\nTarget {target} found as the right child of node {result[0].item}.")
else:
        print(f"\nTarget {target} not found in the tree.")



# Draw a BT of height 4 in which onlyone node (the rightmost node in the
# last level) is absent. Run the code for this tree.

# Step 1: Create the root node (Level 0)
# tree = BinaryTree(1)

# # Step 2: Build Level 1
# tree.addlc(2)
# tree.addrc(3)

# # Step 3: Build Level 2
# tree.lc.addlc(4)
# tree.lc.addrc(5)
# tree.rc.addlc(6)
# tree.rc.addrc(7)

# # Step 4: Build Level 3 (Fill left to right, leave the rightmost node missing)
# tree.lc.lc.addlc(8)
# tree.lc.lc.addrc(9)
# tree.lc.rc.addlc(10)
# tree.lc.rc.addrc(11)
# tree.rc.lc.addlc(12)
# tree.rc.lc.addrc(13)
# tree.rc.rc.addlc(14)  # The rightmost node (15) is not added intentionally.

# # Step 5: Check the tree properties
# print("Height of the tree:", tree.height())              # Should return 4
# print("Total nodes in the tree:", tree.nodecount())      # Should return 14
# print("Total leaf nodes in the tree:", tree.leafcount()) # Should return 7
# print("Is the tree strictly binary?", tree.isStrictlyBinary())  # Should return True
# print("Is the tree perfect?", tree.isPerfect())          # Should return False
# print("Is the tree an ACBT?", tree.isACBT())             # Should return True


# # Draw a BT of height 4 in which the first three levels are completely filled and only three nodes (the leftmost
# # nodes) are present m the last level.
# # Run the code for this tree.

# # Assuming the BinaryTree class is already defined

# # Step 1: Create the root node (Level 0)
# tree = BinaryTree(1)

# # Step 2: Build Level 1
# tree.addlc(2)
# tree.addrc(3)

# # Step 3: Build Level 2
# tree.lc.addlc(4)
# tree.lc.addrc(5)
# tree.rc.addlc(6)
# tree.rc.addrc(7)

# # Step 4: Build Level 3 (Add only the leftmost three nodes)
# tree.lc.lc.addlc(8)
# tree.lc.lc.addrc(9)
# tree.lc.rc.addlc(10)  # Stop here; other nodes are absent.

# # Step 5: Check the tree properties
# print("Height of the tree:", tree.height())              # Should return 4
# print("Total nodes in the tree:", tree.nodecount())      # Should return 10
# print("Total leaf nodes in the tree:", tree.leafcount()) # Should return 3
# print("Is the tree strictly binary?", tree.isStrictlyBinary())  # Should return False
# print("Is the tree perfect?", tree.isPerfect())          # Should return False
# print("Is the tree an ACBT?", tree.isACBT())             # Should return False
