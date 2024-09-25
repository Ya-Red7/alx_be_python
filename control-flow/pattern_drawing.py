num = int(input("Enter the size of the pattern:"))
num2 = num
while num:
    for _ in range(num2):
        print('*',end='')
    if num>1:
        print('\n')
    num-=1

