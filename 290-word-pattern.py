class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        patterns=list(pattern)
        # use zip function, gets zip item, and turn it into a list of tuples
        # shorten it into a set
        s1,s2 = set(list(zip(patterns,words))),set(list(zip(words,patterns)))
        d1,d2 = dict(s1),dict(s2)
        return len(s1)==len(d1) and len(s2)==len(d2) and len(words)==len(patterns)
