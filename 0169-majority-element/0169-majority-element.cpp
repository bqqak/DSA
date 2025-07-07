class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int votes = 0;
        for(auto it : nums){
            if(votes == 0) candidate = it;
            if(candidate != it) votes--;
            else votes++;
        }
        return candidate;
    }
};