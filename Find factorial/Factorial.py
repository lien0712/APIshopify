# caculate the factorial of a given number
# find the number of trailing zeros

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

def factorialTrailingZeros(number):
    count=0
    while(number%10==0):
        count+=1
        number=number/10
    return count

if __name__ == '__main__':
    number= int(input("The number is: "))
    fac=factorial(number)
    print(f"Factorial is: {fac}")
    print(factorialTrailingZeros(fac))
