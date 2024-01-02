class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int r=nums.size()-1;
        int l=0;
        
        while(l<r){
            if(nums[l]+nums[r]>target){
                r--;
            }
            else if(nums[l]+nums[r]<target){
                l++;
            }
            else{
                return {l+1,r+1};
            }
        };
        return {};
        
    }
    
};