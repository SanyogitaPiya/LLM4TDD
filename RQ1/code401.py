from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def code404(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Check if the left child is a leaf node
        left_sum = 0
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val

        # Recursively process left and right subtrees
        left_sum += self.code404(root.left)
        left_sum += self.code404(root.right)

        return left_sum

# Additional test case: Tree with left leaves at different depths
def test_tree_left_leaves_different_depths():
    input_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected_output = 24
    solution = Solution()
    result = solution.code404(input_tree)
    assert result == expected_output

