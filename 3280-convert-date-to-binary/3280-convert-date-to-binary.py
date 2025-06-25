class Solution:
    def convertDateToBinary(self, date: str) -> str:
        '''
        list(map(lambda x: int(x), ls)) 
        29 / 2 = 14 (1)  14 / 2 = 7 (0)   7 / 2 = 3 (1)    3 / 2 = 1 (1)  1/2 = 1
        '''
        numbers = list(map(lambda x: int(x), date.split("-"))) 
       
        numbers_binary = []
        for num in numbers:
            s = ""
            while num != 0:
                s += str(num % 2)
                num //= 2
            numbers_binary.append(s[::-1])
        return '-'.join(numbers_binary)
            