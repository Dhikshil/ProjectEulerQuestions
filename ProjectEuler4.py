num1 = 999
num2 = 999

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True

greatest = 0
for x in range(0, num1):
    for i in range(0, num2):
        if is_palindrome(num1*num2):
            if num1 * num2 > greatest:
                greatest = num1 * num2
        else:
            num2 -= 1
    num1 -= 1
    num2 = 999
print(greatest)