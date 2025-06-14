class Solution:
    def ans(candi):
        return candi + extraCandies > mx_el
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx_el = max(candies)
        arr = list(map(lambda x: x + extraCandies >= mx_el, candies))
        return arr