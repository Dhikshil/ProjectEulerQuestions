#If we list all the natural number below 10 that are multiples of 3 and 5, we get 3, 5, 6, 9. 
#Find all the sum of all the multiples of 3 and 5 below 1000.

num1 = 3
num2 = 5
lim = 1000

def MultipleToLim(num1, num2, lim):
    total = 0
    for x in range(0,lim):
        if x % num1 == 0 or x % num2 == 0:
            total += x
    return total

print(MultipleToLim(num1, num2, lim))

