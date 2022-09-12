class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        # sort the tokens， O(nlogn)
        st = sorted(tokens)
        
        # two pointers approach, O(n)
        max_score = 0
        score = 0
        p1, p2 = 0, len(st)-1
        while p1<=p2:
            # if power largest than the smallest card: play it face up
            if power >= st[p1]:
                power -= st[p1]
                score +=1
                max_score = max(score, max_score)
                p1 += 1
            
            # if power not enough:
            else:
                # if score>=1, play the largest card down
                if score>=1:
                    power+=st[p2]
                    p2-=1
                    score-=1
                
                # if score==0: stop
                else:
                    p1=p2+1
            
        return max_score
        
