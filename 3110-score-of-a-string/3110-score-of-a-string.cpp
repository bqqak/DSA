class Solution {
public:
    int scoreOfString(string s) {
        
        int cnt = 0;
        for(int i = 0; i < s.size() - 1; i++){
            cnt += abs(int(s[i]) - int(s[i + 1]));
        }
        return cnt;
    }
};
