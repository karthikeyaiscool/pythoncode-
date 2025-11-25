def arraysum(a):
    sum=0
    for i in a:

        sum = sum + 1

    return(sum)
a = [12,3,4,15]
arraysum(a)
def summ(n):
    if(n<=0):
       return
    return n+ summ(n-1)