class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        '''
        n = 3 [0, 0]  [0, 1]  [0, 2]
               [1, 0]  [1, 1]  [1, 2]
               [2, 0] [2, 1]  [2, 2]

        [DOWN, RIGHT, UP] -> start (0, 0) -> down -> row + 1
        right -> col + 1 
        up -> row - 1
        left -> col - 1  

        [0, 1, 2]  n = 3    i = 0 j = 0  [0] ->  i = 0 j = 1   [1]   i = 0 j = 2 [2]
        [3, 4, 5]           
        [6, 7, 8]
        '''

        arr = []
        count = 0
        for i in range(n):
            add_arr = []
            for j in range(n):
                add_arr.append(count)
                count += 1
            arr.append(add_arr)
        
        i = 0
        j = 0
        for command in commands:
            if command == "DOWN":
                i += 1
            elif command == "UP":
                i -= 1
            elif command == "RIGHT":
                j += 1
            else:
                j -= 1
        
        return arr[i][j]