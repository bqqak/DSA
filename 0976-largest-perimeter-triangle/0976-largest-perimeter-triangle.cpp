class Solution {
public:
    static bool isExist(int a, int b, int c){
        return a + b > c && b + c > a && c + a > b;
    }
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int p = 0;
        int n = nums.size();
        for(int i = 0; i < n - 2; i++){
            if(isExist(nums[i], nums[i + 1], nums[i + 2])){
                p = max(p, nums[i] + nums[i + 1] + nums[i + 2]);
            }
        }
        return p;
    }
};