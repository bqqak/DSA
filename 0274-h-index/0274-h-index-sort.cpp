class Solution {
public:
    int hIndex(vector<int>& citations) {
        // [3 0 6 1 5]
        // [0 1 3 5 6] or [6 5 3 1 0]
        sort(citations.begin(), citations.end(), greater<int>());
        int mx = INT_MIN;
        int n = citations.size();
        for(int i = 0; i < n; i++){
            int citation = citations[i]; // 3
            int cnt_paper = i + 1; // 2
            if(mx < min(citation, cnt_paper)) mx = min(citation, cnt_paper); // mx = 3
        }
        return mx;
    }
};