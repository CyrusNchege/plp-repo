def fizz_buzz(number):
    """ The function prints fizz, buzz and fizzbuzz based on divisibility of 
    3, 5 or both respectivly 

    Args: number(int): takes one parameter

    Returns:
            fizz, buzz or fizzbuzz 
    """
    
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number
# for reusability of the fuction create an object that does specific task
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))

print("......")
print("......")

for i in range(1,20):
    print(fizz_buzz(i))
