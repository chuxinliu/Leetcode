class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        # a list for letters
        letters = list(s)
        
        # a list for spaces
        leng = len(letters)
        list_spaces = [""]*leng
        for i in range(0, len(spaces)):
            list_spaces[(spaces[i])] = " "

        # combine two lists!
        output = ""
        for i in range(0, leng):
            output+=list_spaces[i]
            output+=letters[i]
        return output
