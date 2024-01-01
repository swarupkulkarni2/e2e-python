#Author_Swarup
num = int(input("Enter a number : "))
i = 2
isPrime = True

while (i <= num//2):
    print(i)
    if (num % i == 0):
        isPrime = False
        break
    i+=1

if (isPrime == True):
    print("{0} is a prime number : ".format(num))
else:
    print("{0} is not a prime number".format(num))


