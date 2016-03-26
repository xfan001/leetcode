/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode TreeNode; 

TreeNode* convert(int *nums, int start, int end)
{
    if (start>end){
        return NULL;
    }
    int mid = (start+end)/2;
    TreeNode *node = malloc(sizeof(TreeNode));
    node->val = nums[mid];
    node->left = convert(nums, start, mid-1);
    node->right = convert(nums, mid+1, end);
    return node;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return convert(nums, 0, numsSize-1);
}