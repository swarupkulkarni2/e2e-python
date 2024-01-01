#author_Swarup
def pallindrom(num):
    reverseNum = 0
    temp = num

    while (temp > 0):
        last = temp%10  #for last digit
        reverseNum = reverseNum*10 + last #to store reverse number
        temp = temp//10 #to get the remaining digits

    if (num == reverseNum):
        print("{0} is a pallindrome number".format(num) )
    else:
        print("{0} is not a pallindrome number".format(num))

#calling a function
pallindrom(int(input("Enter a number : ")))
