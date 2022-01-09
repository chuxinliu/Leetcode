class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        direction = 0
        move_north = 0
        move_west = 0
        
        for i in instructions:
            if i == "L":
                direction+=1
            elif i == "R":
                direction+=3
            else:
                if direction%4==0:
                    move_north+=1
                elif direction%4==1:
                    move_west+=1
                elif direction%4==2:
                    move_north-=1
                else:
                    move_west-=1
        
        return (move_north==0 and move_west==0) or direction%4!=0
      
        
