bool isValid(struct TreeNode *root, int lmax, int rmin){
    if (!root){
        return true;
    }
    if (root->val >= lmax || root->val <= rmin) {
        return false;
    }
    return isValid(root->left, root->val, rmin) && isValid(root->right, lmax, root->val);
}

bool isValidBST(struct TreeNode* root) {
    
    return isValid(root, INT_MAX, INT_MIN);
}

// intmax 和 intmin的问题,shit