class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [chr(i) for i in range(97, 123)]
        for i in alphabet:
            if sentence.find(i) == -1:
                return False
        return True