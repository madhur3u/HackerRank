# FAILED IN LONG RUN

def QUEEN(qy,qx,oy,ox):

    top = 0
    y = qy ; x = qx
    while True :
        if (y == n or (y + 1 == oy and x == ox)) : break 
        y += 1
        top += 1           
    
    bottom = 0
    y = qy ; x = qx
    while True :
        if (y == 1 or (y - 1 == oy and x == ox)) : break 
        y -= 1
        bottom += 1  

    right = 0
    y = qy ; x = qx
    while True :
        if (x == n or (y == oy and x + 1 == ox)) : break 
        x += 1
        right += 1 

    left = 0
    y = qy ; x = qx
    while True :
        if (x == 1 or (y == oy and x - 1 == ox)) : break 
        x -= 1
        left += 1

    topright = 0
    y = qy ; x = qx
    while True :
        if (y == n or x == n) or (y + 1 == oy and x + 1 == ox) : break 
        y += 1 ; x += 1
        topright += 1

    topleft = 0
    y = qy ; x = qx
    while True :
        if (y == n or x == 1) or (y + 1 == oy and x - 1 == ox) : break 
        y += 1 ; x -= 1
        topleft += 1

    bottomright = 0
    y = qy ; x = qx
    while True :
        if (y == 1 or x == n) or (y - 1 == oy and x + 1 == ox) : break 
        y -= 1 ; x += 1
        bottomright += 1

    bottomleft = 0
    y = qy ; x = qx
    while True :
        if (y == 1 or x == 1) or (y - 1 == oy and x - 1 == ox) : break 
        y -= 1 ; x -= 1
        bottomleft += 1

    return (top + bottom + right + left + topright + topleft + bottomleft + bottomright)

n, k = map(int, input().split())
q_y, q_x = map(int, input().split())

# print(f'Sum if no obstacle is {QUEEN(q_y,q_x,0,0)}')
s = QUEEN(q_y, q_x, 0, 0) # sum when no obstacle
so = 0

for _ in range(k):
    # obstacle input
    o_y, o_x = map(int, input().split())
    so = so + (s - QUEEN(q_y, q_x, o_y, o_x))

print(s - so)
