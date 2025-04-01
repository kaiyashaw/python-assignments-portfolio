x=float(input('number:'))
n=0
if 0<=x<=1:
    def error(a, b):
        y = (a ** (2 * (b + 1))) / ((2 * b) + 1)
        return y
    while error(x,n) > 0.0001:
        n+=1
    sum=0
    for i in range(n):
        current=(((-1)**i)*(x**(2*i+1))/(2*i+1))
        sum+=current
    print(sum)
    statement = (sum, n, error(x, n))
    print(statement)

else:
    print ('error')


