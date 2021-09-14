##### https://www.hackerrank.com/challenges/queens-attack-2/problem

n, k = map(int, input().split())
y, x  = map(int, input().split())

top         = n - y         # all moves in each direction of queen when no obstacle
bottom      = y - 1
right       = n - x
left        = x - 1
topright    = min(n-y, n-x)
topleft     = min(n-y, x-1)
bottomright = min(y-1, n-x)
bottomleft  = min(y-1, x-1)

for _ in range(k):
    # obstacle input
    oy, ox  = map(int, input().split())

    if ox == x:  # when obstacle is in y axis it can be in top or bottom
        if oy > y:
            top = min(top, oy - y - 1) # top

            # so if in top queen can only move oy - y - 1, we take min here as 
            # we can find some other obstacle above this one so we will take minimum
            # same reason is for all below cases for taking minimum

        else :
            bottom = min(bottom, y - oy - 1) # bottom

    if oy == y: # when obstacle is in x axis it will be in left or right
      
        if ox > x:
            right = min(right, ox - x - 1) # right
        else :
            left = min(left, x - ox - 1) # left
    
    if oy - ox == y - x : # this means the obstacle is in topright or bottom left i.e. 1st or 3rd quadrant
      
        if ox > x and oy > y : 
            topright = min(topright, min(oy - y - 1, ox - x - 1)) # topright
            
        elif ox < x and oy < y :
            bottomleft = min(bottomleft, min(y - oy - 1, x - ox - 1)) # bottomleft

    if oy + ox == y + x : # this means the obstacle is in topleft or bottomright i.e. 2nd or 4th quadrant
      
        if ox < x and oy > y : 
            topleft = min(topleft, min(oy - y - 1, x - ox - 1)) # top left
            
        elif ox > x and oy < y :
            bottomright = min(bottomright, min(y - oy - 1, ox - x - 1)) # bottom right

print(top + topleft + topright + left + right + bottom + bottomleft + bottomright)
