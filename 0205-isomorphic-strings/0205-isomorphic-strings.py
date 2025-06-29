class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        The main idea is to create map [element, arr[index]]
        '''
        char_indices = {}
        for index, char in enumerate(s):
            if char in char_indices:
                char_indices[char].append(index)
            else:
                char_indices[char] = [index]
        
        char_indices_2 = {}
        for index, char in enumerate(t):
            if char in char_indices_2:
                char_indices_2[char].append(index)
            else:
                char_indices_2[char] = [index]
        
        return list(char_indices.values()) == list(char_indices_2.values())