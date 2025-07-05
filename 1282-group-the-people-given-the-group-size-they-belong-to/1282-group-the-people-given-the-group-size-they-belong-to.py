class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        groupSize[1] = 3, then person 1 must be in a group of size 3
        [3, 3, 3, 3, 1, 3]
        ans: [[0, 1, 2], [3, 4, 6]. [5]]
        arr = []
        {
            3: [0 , 1, 2]
            check if dict[3].len() == 3, then arr.apend[key] -> clear
        }

        [2, 1, 3, 3, 3, 2]
        {
            2: [0, 5],
            1: [1],
            3: [2, 3, 6]
        }
        '''
        arr = []
        mp = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in mp:
                mp[size] = []
            mp[size].append(i)
            
            if len(mp[size]) == size:
                arr.append(mp[size])
                mp[size] = []
        return arr