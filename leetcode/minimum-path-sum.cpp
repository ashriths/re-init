/*##############################################################################
# Question:

64. Minimum Path Sum - Medium


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
##############################################################################*/


class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> cost;
        int m = grid.size();
        int n = 0;
        if (m > 0) n = grid[0].size();
        //cout<<m<<" "<<n<<endl;
        for(int i=0; i < grid.size(); i++){
            vector<int> c;
            for(int j=0; j < grid[i].size(); j++){
                if (i==0 && j==0){
                    c.push_back(grid[i][j]);
                    continue;
                }else{
                    if (i==0){
                        c.push_back(grid[i][j] + c[j-1]);
                    }else if (j==0){
                        c.push_back(grid[i][j] + cost[i-1][j]);
                    }else{
                        int top = grid[i][j] + cost[i-1][j];
                        int left = grid[i][j] + c[j-1];
                        c.push_back(min(top, left));        
                    }    
                } 
                //cout<<grid[i][j]<<"->"<<c[j]<<endl;
            }
            cost.push_back(c);
        }
        return cost[m-1][n-1];
    }
};