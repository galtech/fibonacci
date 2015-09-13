series = [0,1]

n = raw_input('Please enter series length: ')
try:
    n = int(n)
except:
    print 'Please enter an integer only'
    quit()


def fib(n):

    for num in range(0,n):
        if num in [0,1]:
            continue
        elif num > 1:
            series.append(series[num-2] + series[num-1])
    return series                   

fibSeries = fib(n)
print 'nth fibonacci number: ', fibSeries[len(fib(n))-1]
