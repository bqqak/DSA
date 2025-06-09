class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // Insertion Sort
        vector<int> copy = heights;
        for(int i = 1; i < copy.size(); i++){
            for(int j = i; j > 0; j--){
                if(copy[j] < copy[j - 1]){
                    swap(copy[j], copy[j - 1]);
                } else break;
            }
        }
        int cnt = 0;
        for(int i = 0; i < heights.size(); i++){
            if(heights[i] != copy[i]) cnt++;
        }
        return cnt;
    }
};