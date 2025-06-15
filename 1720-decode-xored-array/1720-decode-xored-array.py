class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        # encoded[i] = arr[i] ^ arr[i + 1] -> need to know arr[i + 1]
        # arr[i+1] = encoded[i] ⊕ arr[i]
        n = len(encoded)
        for i in range(n):
            arr.append(encoded[i] ^ arr[i])
        return arr
        
