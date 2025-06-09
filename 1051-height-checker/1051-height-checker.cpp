class Solution {
public:
    int heightChecker(vector<int>& heights) {
        //  Counting Sort
        int mx = 0;
        for(int i : heights) mx = max(mx, i);
        
        vector<int> v(mx + 1, 0);
        for(int i : heights) v[i]++;

        for(int i = 1; i <= mx; i++) v[i] += v[i - 1];

        int n = heights.size();
        vector<int>ans(n);
        for(int i = n - 1; i >= 0; i--){
            int x = heights[i];
            int pos = --v[x];
            ans[pos] = x;
        }
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(heights[i] != ans[i]) cnt++;
        }
        return cnt;
    }
};