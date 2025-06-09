class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        //using maths (Combinations) -> n(n - 1) / 2
        unordered_map<int, int> mp;
        for(int i : nums) mp[i]++;
        int cnt = 0;
        for(auto [key, value]: mp){
            cnt += (value * (value - 1) / 2);
        }
        return cnt;
    }
};