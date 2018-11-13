/*##############################################################################
# Question:

# 18. 4Sum


# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
################################################################################
# Solution Note:

# Two ways again:

# Solve using 2 two sums
#     O(n^3) solution
#     1. Sort it
#     2. First and second loop to fix a and b
#     3. Last loop to converge to middle from both ends to get c and d
##############################################################################*/

class Solution {
public:
    
    // void printVector(const vector<int>& nums){
    //     cout<<"[";
    //     for(int i=0; i<nums.size(); ++i ){
    //         cout<<nums[i]<<",";
    //     }
    //     cout<<"]"<<endl;
    // }
    // void printVectorVector(const set<vector<int>>& nums){
    //     cout<<"[";
    //     for(int i=0; i<nums.size(); ++i ){
    //         printVector(nums[i]);
    //     }
    //     cout<<"]"<<endl;
    // }
    
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        set<vector<int>> results;
        sort(nums.begin(), nums.end());
        vector<int> cur;
        nSumInner(nums, 4 ,0 ,nums.size()-1 , target, cur, results);
        vector<vector<int>> resultsVector(results.begin(), results.end());
        return resultsVector;
    }
    
    void nSumInner(const vector<int>& nums, int n, int left, int right, int target, 
                   vector<int>& cur, set<vector<int>>& results){
        // cout<<"nSumInner(n="<<n<<",target="<<target<<",left="<<left<<endl;
        // printVector(cur);
        // printVectorVector(results);
        if (n==2){
            while (left < right){
                int s = nums[left] + nums[right];
                if (s == target){
                    vector<int> _cur = cur;
                    _cur.push_back(nums[left]);
                    _cur.push_back(nums[right]);
                    results.insert(_cur);
                    left++;
                }else if(s < target){
                    left++;
                }else{
                    right--;
                }
            }
        }else{
            for (int i=left; i<=right; i++){
                int e = nums[i];
                cur.push_back(e);
                nSumInner(nums, n-1, i+1, right, target-e, cur, results);
                cur.pop_back();
            }
            return;
        }
    }
};
            
        