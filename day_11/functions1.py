def main ():
    num = int (input ('enter number: '))
    name = input ('What is you name? ')

    print ('The numbers of evens and odd upto this number are ', evens_and_odds (num), ' respectively')
    greet (name)

def evens_and_odds (n):
    evens = 0
    odds = 0
    for i in range (n + 1):
        if i % 2 == 0 :
            evens += 1
        else:
            odds += 1
    return evens, odds

def greet (g = 'guest'):
    print (f'Hello, {g}')

    

main ()

            