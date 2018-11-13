/*##############################################################################
Question:

78. Subsets - Medium


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
##############################################################################*/


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        ArrayList<List<Integer>> results = new ArrayList<List<Integer>>();
        results.add(new ArrayList<Integer>());
        for (int i=0; i < nums.length ; i ++ ){
            //System.out.println(i);
            ArrayList<List<Integer>> newResults = new ArrayList<List<Integer>>();
            for (List<Integer> l : results){
                //
                List<Integer> m = new ArrayList<Integer>();
                m.addAll(l);
                m.add(nums[i]);
                //System.out.println(m);
                newResults.add(m);
            }
            results.addAll(newResults);
        }
        return results;
    }
}