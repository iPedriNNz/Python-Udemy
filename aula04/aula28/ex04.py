def fizzbuzz(n1):
    if n1 % 3 == 0:
        return 'Fizz'
    elif n1 % 5 == 0:
        return 'Buzz'
    elif n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'
    else:
        return n1

print(fizzbuzz(7))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(22))
