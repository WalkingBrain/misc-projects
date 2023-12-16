import math

def is_even(number):
    """
    Determines if a number is even or not.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

def is_integer(number):
    """
    Checks if the given number is an integer.
    
    Parameters:
        number (int or str): The number to be checked.
        
    Returns:
        bool: True if the number is an integer, False otherwise.
    """
    try:
        int(number)
        return True
    except ValueError:
        return False
    
def is_float(number):
    """
    Check if a given number is a valid float.

    Parameters:
    - number (str or int or float): The number to be checked.

    Returns:
    - bool: True if the number is a valid float, False otherwise.
    """
    try:
        float(number)
        return True
    except ValueError:
        return False

def is_prime(number):
    """
    Checks if a given number is prime.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_perfect_square(number):
    """
    Check if a number is a perfect square.

    Parameters:
    - number: an integer or float number to be checked.

    Returns:
    - True if the number is a perfect square.
    - False otherwise.
    """
    return is_integer(number ** (1/2))

def is_perfect_cube(number):
    """
    Check if a number is a perfect cube.

    Parameters:
    - number: an integer or float number to be checked.

    Returns:
    - True if the number is a perfect cube.
    - False otherwise.
    """
    return is_integer(number ** (1/3))
    
def is_power_of_two(number):
    """
    Check if a number is a power of two.

    Parameters:
    - number: an integer or float number to be checked.

    Returns:
    - True if the number is a power of two.
    - False otherwise.
    """
    return is_integer(math.log2(number))
    
def is_power_of_three(number):
    """
    Check if a number is a power of three.

    Parameters:
    - number: an integer or float number to be checked.

    Returns:
    - True if the number is a power of three.
    - False otherwise.
    """
    return is_integer(math.log3(number))
    
def is_positive(number):
    return number > 0
    
def is_negative(number):
    return number < 0
    
def is_zero(number):
    return number == 0

def check_perfect(a):
    divisors_sum = sum(i for i in range(1, a) if a % i == 0)
    return divisors_sum == a

def lcm(a, b):
    return a * b // math.gcd(a, b)

def fibonnaci_sequence(iterations):
    a, b = 0, 1
    for i in range(iterations):
        print(a, end=" ")
        a, b = b, a + b
    
def digital_root(number):
    return (number - 1) % 9 + 1

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def pythagorean_triples_two(a, b):
    not_found = True
    for c in range(max(a, b)**2):
        if c**2 == a**2 + b**2:
            print(f"triple found for {a}^2 + {b}^2 = {c}^2")
            not_found = False
            break
    if not_found:
        print("No triple found")

def sum_of_range_int(a, b):
    return b*(b+1)//2 - a*(a-1)//2

def pythagorean_triangle_side_and_hypotenuse(c, b):
    return (c**2 - b**2)**0.5

def avg_of_range_int(a, b):
    return (a + b) / 2

def solve_quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

def find_factors(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors

def find_pythagorean_triples_one(a):
    found = False
    for b in range(1, a ** 2):
        if 2 * b - 1 > a ** 2:
            break
        for c in range(1, a ** 2):
            if 2 * c - 1 > a ** 2:
                break
            elif a ** 2 + b ** 2 == c ** 2:
                print(f"triple found for {a}^2 + {b}^2 = {c}^2")
                print(f"{a**2} + {b**2} = {c**2}")
                found = True
    if not found:
        print("No triple found")
    
def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def is_in_pythagorean_triple(c):
    for b in range(1, c):
        for a in range(1, c):
            if is_pythagorean_triple(a, b, c):
                return True
    return False
    
    
def decimal_to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def binary_addition(a, b):
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    result = ''
    carry = 0
    for i in range(len(a)-1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result

def binary_subtraction(a, b):
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    result = ''
    borrow = 0
    for i in range(len(a)-1, -1, -1):
        r = int(a[i]) - int(b[i]) - borrow
        if r < 0:
            r += 2
            borrow = 1
        else:
            borrow = 0
        result = str(r) + result
    return result.lstrip('0')

def nth_root(n, number):
    return number ** (1 / n)

def percentage_in(sample_size, numbers, value):
    return 100  / sample_size * numbers.count(value)

def encrypt(message, key):
    shift = math.floor(key ** 0.5 * 2)
    return ''.join(chr(ord(char) + shift) for char in message)

def decrypt(message, key):
    shift = math.floor(key ** 0.5 * 2)
    return ''.join(chr(ord(char) - shift) for char in message)

