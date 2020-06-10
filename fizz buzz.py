for n in range(1, 101):
    response = ''

    if n%3 == 0:
        response += 'Fizz'
    if n%5 == 0:
        response += 'Buzz'

    print(response or n)