# author: CJP (AMDG) 12/2/2021

total = 0
while True:
    num = input("Enter a number: ")
    if num == "-1":
        break
    else:
        total += int(num)

print("The sum of all the numbers entered is {0}".format(total))
