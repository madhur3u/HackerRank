# https://www.hackerrank.com/challenges/taum-and-bday/problem

def cost(b,w,bc,wc,z):
    if bc + z < wc :
        c = b * bc + w * (bc + z)  
    elif wc + z < bc :
        c = b * (wc + z) + w * wc
    else :
        c = b * bc + w * wc
    return c

for _ in range(int(input())):

    b,w = map(int, input().split())
    bc, wc, z = map(int, input().split())

    c = cost(b,w,bc,wc,z)
    print(c)
