#The prime factors of 13195 are 5, 7, 13 and 29
#What is the largest prime factor of the number 600851475143

num = 600851475143
x = 2

gtreatest_factor = 0
while x*x < num:
    while num % x == 0:
        num = num//x
    x += 1

print(num)
