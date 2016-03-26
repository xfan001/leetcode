/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode TreeNode;

TreeNode *subFunc(TreeNode* root){
    if (!root){
        return NULL;
    }
    TreeNode *lchild = root->left;
    TreeNode *rchild = root->right;
    root->left = NULL;
    root->right = flatten(lchild);
    TreeNode *node = root;
    while (node->right){
        node = node->right;
    }
    node->right = flatten(rchild);
    return root;
}


void flatten(struct TreeNode* root) {
    subFunc(root);
}
