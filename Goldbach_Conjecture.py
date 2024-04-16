#Gabriela Fuller
#1/30/24
#DSC 430
#https://youtu.be/21M1UG-bqxg

#“I have not given or received any unauthorized assistance on this assignment”

def is_prime(n): #Check and define if a number is prime. returns true if the number is prime, false otherwise
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(limit): # tests for integers less than the given limit."""
    for even_num in range(4, limit, 2): #iterates over even numbers
        found = False
        for i in range(2, even_num // 2 + 1):
            if is_prime(i) and is_prime(even_num - i):
                print(f"{even_num} = {i} + {even_num - i}")
                found = True
                break
        if not found:
            print(f"No prime pair found for {even_num}")

# Test for integers less than 100
goldbach_conjecture(100)

