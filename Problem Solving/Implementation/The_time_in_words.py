# https://www.hackerrank.com/challenges/the-time-in-words/problem

def num2word(n):
    a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    return(a[n])

hour = int(input())
minutes = int(input())

if minutes == 0:
    print( num2word(hour) + " o' clock")

elif minutes == 15:
    print( "quarter past " + num2word(hour))

elif minutes == 30:
    print( "half past " + num2word(hour))

elif minutes == 45:
    print( "quarter to " + num2word(hour+1))

elif minutes == 1 :
    print( num2word(minutes) + " minute past " + num2word(hour))

elif 1<minutes<30 :
    print( num2word(minutes) + " minutes past " + num2word(hour))

elif minutes == 59 :
    print( num2word(60 - minutes) + " minute to " + num2word(hour+1))

elif 30<minutes<59 :
    print( num2word(60 - minutes) + " minutes to " + num2word(hour+1))
