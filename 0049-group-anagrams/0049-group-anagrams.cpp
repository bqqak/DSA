class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       vector<pair<string, string>> v;
       for(string s : strs){
            string l = s;
            sort(l.begin(), l.end());
            v.push_back({l, s});
       }
       sort(v.begin(), v.end());


       vector<vector<string>> res;
       vector<string> temp;
       temp.push_back(v[0].second);

       for(int i = 1; i < v.size(); i++){
            if(v[i].first == v[i - 1].first) temp.push_back(v[i].second);
            else{
                res.push_back(temp);
                temp.clear();
                temp.push_back(v[i].second);
            }
       }
       if(!temp.empty()) res.push_back(temp);
       return res;
    }
};