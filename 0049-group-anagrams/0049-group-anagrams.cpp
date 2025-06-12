class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> v;
        unordered_map<string, vector<string>> mp;
        for(string s : strs){
            string l = s;
            sort(l.begin(), l.end());
            mp[l].push_back(s);
        }
        for(auto values: mp){
            v.push_back(values.second);
        }
        return v;
    }
};