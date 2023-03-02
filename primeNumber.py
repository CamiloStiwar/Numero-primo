
def isPrimeNumber(number):
    if number == 1:
        return False

    isPrime = True
    for divisor in range(2,number):
         if number % divisor == 0:
            isPrime = False
            return isPrime
    return isPrime

contPrimeNumbers = 0
sumPrimeNumbers = 0
numberToEvaluate = 1

while contPrimeNumbers < 20:
    if isPrimeNumber(numberToEvaluate):
        contPrimeNumbers = contPrimeNumbers + 1
        sumPrimeNumbers = sumPrimeNumbers + numberToEvaluate
        print(numberToEvaluate, sumPrimeNumbers, isPrimeNumber(sumPrimeNumbers))

    numberToEvaluate = numberToEvaluate + 1