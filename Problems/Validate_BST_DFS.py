from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a given binary tree is a valid Binary Search Tree (BST)
        by enforcing strict min and max bounds during a recursive DFS traversal.
        """
        
        # Helper function for recursive validation
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            # 1. Base Case: An empty node/subtree is always a valid BST.
            if not node:
                return True

            # 2. Check Current Node: The node's value must be strictly within its inherited bounds.
            # BST definition: left < node < right
            if not (min_val < node.val < max_val):
                return False

            # 3. Recurse Left Subtree:
            # The maximum allowed value for the left child is the current node's value (node.val).
            # The minimum remains the global min_val.
            is_left_valid = validate(node.left, min_val, node.val)
            
            # 4. Recurse Right Subtree:
            # The minimum allowed value for the right child is the current node's value (node.val).
            # The maximum remains the global max_val.
            is_right_valid = validate(node.right, node.val, max_val)

            # The BST is valid only if BOTH subtrees are valid.
            return is_left_valid and is_right_valid

        # Start the validation from the root, setting the initial bounds to
        # negative infinity and positive infinity to cover the entire integer range.
        return validate(root, float('-inf'), float('inf'))
