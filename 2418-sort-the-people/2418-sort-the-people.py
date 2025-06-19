class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = {}
        for i in range(len(names)):
            mp[heights[i]] = names[i]
        
        sorted_items = dict(sorted(mp.items(), reverse=True))
        ans = [i for i in sorted_items.values()]
        return ans