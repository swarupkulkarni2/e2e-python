#Author Swarup
def numberPattern(num):

    i, j = 1,1
    while i <= num:
        for j in range (1, i+1):
            print(j, end=' ')
        print()
        i+=1
    i = num - 1
    while i >= 1:
        for j in range(1, i+1):
            print(j, end=' ')
        print()
        i-=1

numberPattern(int(input("Enter a num : ")))
