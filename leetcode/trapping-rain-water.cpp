/*##############################################################################
# Question:

42. Trapping Rain Water
Hard
2371
47


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

##############################################################################*/

class Solution {
public:
    int trap(vector<int>& height) {
        int left =  0;
        int right = height.size()-1;
        int maximumHeight = 0;
        int total = 0;
        while (left < right){
            int h = min(height[left], height[right]);
            if (h < maximumHeight){
                total += (maximumHeight-h);
            } 
            maximumHeight = max(h, maximumHeight);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return total;
    }
};