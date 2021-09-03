# t is no of 50 digit nos
# add all 50 digit numbers
# print 1st 10 digits of it

t = int(input())
s = 0
for a0 in range(t) :
    n = int(input())
    s = s + n

a = len(str(s))
a = a-10
b = pow(10,a)
print(s//b)
