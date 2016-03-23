/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode TreeNode;
int treeHeight(TreeNode* root);
int countNodesWithHeight(TreeNode *root, int height);

int countNodes(TreeNode* root) {
    if (!root){
        return 0;
    }
    int h = treeHeight(root);
    return countNodesWithHeight(root, h);
}


int treeHeight(TreeNode* root){
    TreeNode *node = root;
    int height = 0;
    while (node){
        height++;
        node = node->left;
    }
    return height;
}

int countNodesWithHeight(TreeNode *root, int height){
    if (!root){
        return 0;
    }
    int leftH = height-1;
    int rightH = treeHeight(root->right);
    if (leftH > rightH){
        return 1 + pow(2, rightH)-1 + countNodesWithHeight(root->left, leftH);
    }else{
        return 1 + pow(2, leftH)-1 + countNodesWithHeight(root->right, rightH);
    }
}