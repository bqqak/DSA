class Solution {
public:
    static bool compare(int a, int b){
        return to_string(a) + to_string(b) > to_string(b) + to_string(a);
    }
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), compare);
        string res = "";
        for(int i : nums) res += to_string(i);
        
        return (res[0] == '0' ? "0" : res);
    }
};