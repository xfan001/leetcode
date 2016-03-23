/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* buildTreeFunc(int *inorder, int in_start, int in_end,
                               int *preorder, int pre_start, int pre_end){
    if (in_start > in_end){
        return NULL;
    }
    int i;
    for (i=in_start; i<=in_end; i++){
        if (inorder[i] == preorder[pre_start]){
            break;
        }
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    root->val = inorder[i];
    root->left = buildTreeFunc(inorder, in_start, i-1, preorder, pre_start+1, pre_start+1+(i-1-in_start));
    root->right = buildTreeFunc(inorder, i+1, in_end, preorder, pre_end-(in_end-i-1), pre_end);
    return root;
}


struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    return buildTreeFunc(inorder, 0, inorderSize-1, preorder, 0, preorderSize-1);
}