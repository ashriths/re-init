/*##############################################################################
# Question:

114. Flatten Binary Tree to Linked List - Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
##############################################################################*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        while(root!= null){
            if (root.left==null)
                root = root.right;
            else{
                if (root.left!=null){
                    TreeNode r = root.left;
                    while(r.right!=null){
                        r = r.right;
                    }
                    r.right = root.right;
                }
                root.right = root.left;
                root.left = null;
                root = root.right;
            }
        }
    }
}