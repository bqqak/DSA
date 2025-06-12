class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> v;
        
        unordered_map<string, vector<int>> pos;

        int n =strs.size();
        for(int i = 0; i < n; i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            pos[s].push_back(i);
        }
        for(auto [word, positions] : pos){
            vector<string> values;
            for(int i : positions){
                values.push_back(strs[i]);
            }
            v.push_back(values);
        }
        return v;
    }
};