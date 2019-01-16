# Fibonacci series Function

def fib2():
    outputval = []
    a, b = 0, 1                  # initialising the varibles
    while b < 1000:              # looping the values till 1000
        outputval.append(b)      # storing in ouptu variable 
        a, b = b, a+b            # re-assigning the varibles for next iteration
    return outputval