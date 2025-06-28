class Solution:
    def sortSentence(self, s: str) -> str:
        list_word = s.split(' ')
        n = len(list_word)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if int(list_word[j][-1]) > int(list_word[j + 1][-1]):
                    list_word[j], list_word[j + 1] = list_word[j + 1], list_word[j]
        
        ans = []
        for i in list_word:
            ans.append(i[:-1])
        return ' '.join(ans)