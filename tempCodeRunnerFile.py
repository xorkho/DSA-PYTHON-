tree = BinaryTree(1)

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
