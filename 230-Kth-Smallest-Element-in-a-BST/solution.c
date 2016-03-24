/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode TreeNode;

int calTreeNodeCount(TreeNode* root){
    if (!root){
        return 0;
    }
    return 1 + calTreeNodeCount(root->left) + calTreeNodeCount(root->right);
}

int kthSmallest(struct TreeNode* root, int k) {
    int lcount = calTreeNodeCount(root->left);
    if (lcount < k-1){
        return kthSmallest(root->right, k-lcount-1);
    }else if (lcount > k-1){
        return kthSmallest(root->left, k);
    }else{
        return root->val;
    }
}