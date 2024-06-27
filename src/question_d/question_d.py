#write functions here, don't add input('') statements here!


def menu():
    choice = 'n'
    while choice != 'y' and choice != 'Y':
        num = int(input("Type a number to see if it is prime: "))
        print(is_prime(num))
        choice = input("Would you like to quit (y = yes, n = no)?")




def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True