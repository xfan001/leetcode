double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int len=nums1Size + nums2Size;
    int new[len];
    int i=0, j=0, k=0;
    double median;
    while(i<nums1Size && j<nums2Size){
        if (nums1[i] <= nums2[j]){
            new[k++] = nums1[i++];
        }
        else if (nums1[i] > nums2[j]){
            new[k++] = nums2[j++];
        }
    }
    while (i<nums1Size){
        new[k++] = nums1[i++];
    }
    while (j<nums2Size){
        new[k++] = nums2[j++];
    }
    if (len % 2 == 1){
        median = new[(len-1)/2];
    }
    else{
        median = (new[len/2-1] + new[len/2])*1.0/2.0;
    }
    return median;
}