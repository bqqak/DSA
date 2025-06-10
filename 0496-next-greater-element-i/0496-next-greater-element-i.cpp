class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> greater_el;
        for(int i = 0; i < nums1.size(); i++){
            int mx = nums1[i];
            bool met = false;
            for(int j = 0; j < nums2.size(); j++){
                if(met && nums2[j] > mx){
                    mx = nums2[j];
                    break;
                }
                if(nums1[i] == nums2[j]){
                    met = true;
                }
            }
            greater_el.push_back(mx == nums1[i] ? -1 : mx);
        }
        return greater_el;
    }
};