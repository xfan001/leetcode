/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int isSame = 0;
    int start=-1, end=0;
    for (int i=0; i<numsSize; i++){
        if (!isSame && nums[i]==target){
            isSame = 1;
            start = i;
        }
        if (isSame && nums[i]!=target){
            isSame = 0;
            end = i;
            break;
        }
    }
    returnSize = (int *)malloc(2 * sizeof(int));
    *returnSize = start;
    *(returnSize+1) = end-1;
    return returnSize;
}