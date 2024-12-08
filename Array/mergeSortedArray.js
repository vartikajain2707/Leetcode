var merge = function(nums1, m, nums2, n) {
    let i=m-1
    let j=n-1
    let k=m+n-1
    while(k>=0 && j>=0 && i>=0){
        if(nums1[i]<=nums2[j]){
            nums1[k]=nums2[j]
            j--
            k--
        }
        else{
            nums1[k]=nums1[i]
            k--
            i--
        } 
    }
    while(k>=0 && j>=0){
        nums1[k]=nums2[j]
        k--
        j--
    }
};
