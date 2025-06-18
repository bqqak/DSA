class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')
        for part in path_list:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)