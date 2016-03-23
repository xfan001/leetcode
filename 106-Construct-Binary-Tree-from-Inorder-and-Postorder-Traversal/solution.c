/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* buildTreeFunc(int *inorder, int in_start, int in_end,
                               int *postorder, int post_start, int post_end){
    if (in_start > in_end){
        return NULL;
    }
    int i;
    for (i=in_start; i<=in_end; i++){
        if (inorder[i] == postorder[post_end]){
            break;
        }
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = inorder[i];
    root->left = buildTreeFunc(inorder, in_start, i-1, postorder, post_start, post_start+i-1-in_start);
    root->right = buildTreeFunc(inorder, i+1, in_end, postorder, post_end-1-(in_end-i-1), post_end-1);
    return root;
}


struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    return buildTreeFunc(inorder, 0, inorderSize-1, postorder, 0, postorderSize-1);
}
