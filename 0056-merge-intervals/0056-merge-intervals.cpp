class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        // [[0 1] [1 4]]
        // start = 0 end = 1
        // 1 >= 1   end = 4 
        // start = 0 end = 4
        int start = intervals[0].front();
        int end = intervals[0].back();
        int n = intervals.size();
        
        vector<vector<int>> v;
        for(int i = 1; i < n; i++){
            if(end >= intervals[i].front()){
                end = max(end, intervals[i].back());
            } else{
                v.push_back({start, end});
                start = intervals[i].front();
                end = intervals[i].back();
            }
        }
        v.push_back({start, end});
        return v;
    }
};