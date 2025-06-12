class Solution {
public:
    string largestNumber(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n - i - 1; j++){
                string a = to_string(nums[j]);
                string b = to_string(nums[j + 1]);
                if(a + b < b + a){
                    swap(nums[j], nums[j + 1]);
                }
            }
        }
        string res = "";
        for(int i = 0; i < n; i++){
            res += to_string(nums[i]);
        }
        if(res[0] == '0') return "0";
        return res;
    }
};