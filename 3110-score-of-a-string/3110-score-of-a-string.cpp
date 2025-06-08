class Solution {
public:
    int scoreOfString(string s) {
        // s.length <= 100, thus we can solve it in O(n^3)
        int cnt = 0;
        for(int i = 0; i < s.size() - 1; i++){
            cnt += abs(int(s[i]) - int(s[i + 1]));
        }
        return cnt;
    }
};