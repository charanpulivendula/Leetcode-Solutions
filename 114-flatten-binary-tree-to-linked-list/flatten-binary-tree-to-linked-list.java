/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        TreeNode prev = new TreeNode(0);
        prev.left=null;
        prev.right=prev;
        myFunction(root,prev);        
    }
    public void myFunction(TreeNode currentNode,TreeNode prev){
        if (currentNode == null) return;
        System.out.println(currentNode.val+" "+prev.val);
        TreeNode left = currentNode.left;
        TreeNode right = currentNode.right;
        currentNode.left = null;
        prev.right.right = currentNode;
        prev.right=currentNode;
        myFunction(left,prev);
        myFunction(right,prev);
    }
}