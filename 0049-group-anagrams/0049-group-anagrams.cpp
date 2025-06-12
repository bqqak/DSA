class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> v;
        vector<string> copy_strs = strs;
        for(string &s : strs){
            sort(s.begin(), s.end());
        }
        int n =strs.size();
        unordered_map<string, vector<int>> pos;
        for(int i = 0; i < n; i++) pos[strs[i]].push_back(i);
        for(auto [word, positions] : pos){
            vector<string> values;
            for(int i : positions){
                values.push_back(copy_strs[i]);
            }
            v.push_back(values);
        }
        return v;
    }
};