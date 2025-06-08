class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        // words.length <= 50, consequently we can solve it in O(n ^ 3)
        int n = words.size();
        vector<int> res;
        for(int i = 0; i < n; i++){
            if(find(words[i].begin(), words[i].end(), x) != words[i].end()) res.push_back(i);
        }
        return res;
    }
};