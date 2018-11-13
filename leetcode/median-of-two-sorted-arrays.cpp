/*##############################################################################
# Question:

4. Median of Two Sorted Arrays - Hard


There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
##############################################################################*/


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n=nums2.size();
        int total = m + n;
        int m1 = (total+1)/2;
        int p1 = 0, p2 = 0, counter = 0, cur=-1, pre=-1;
        while (counter <= m1){
            pre = cur;
            if (p1 < m && p2 < n){
                if (nums1[p1] < nums2[p2]){
                    cur=nums1[p1++];
                }else{
                    cur=nums2[p2++];
                }
            }else if(p1 < m){
                cur=nums1[p1++];
            }else if(p2 < n){
                cur=nums2[p2++];
            }     
            counter++;
        }
        if (total % 2 == 0){
            cout<<"Even"<<pre<<" "<<cur;
            return (pre + cur)/2.0;
        }else{
            cout<<"Odd"<<pre<<" "<<cur;
            if (total > 1)return pre;
            else return cur;
        }
    }
};