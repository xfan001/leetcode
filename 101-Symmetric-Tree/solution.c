bool isMirror(struct TreeNode *tree1, struct TreeNode *tree2){
    if (!tree1 && !tree2){
        return true;
    }
    else if (tree1 && tree2){
        return (tree1->val == tree2->val && 
        isMirror(tree1->left, tree2->right) && 
        isMirror(tree1->right, tree2->left));
    }
    else{
        return false;
    }
}

bool isSymmetric(struct TreeNode* root) {
    return isMirror(root, root);
}
