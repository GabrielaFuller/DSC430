#Gabriela Fuller
#1/15/24
#DSC 430
#https://youtu.be/yj_HZKPWzsQ
#“I have not given or received any unauthorized assistance on this assignment”

# A function finds gcd
def find_gcd(a, b):
    while b:  # While b is not zero
        a, b = b, a % b  # Update a and b
    return a  # Return GCD

# Checks if two numbers are coprime
def coprime(a, b):
    if find_gcd(a, b) == 1:  # If the GCD is 1, they are coprime
        return True
    else:  # They are not coprime if the GCD is not 1
        return False

# Runs the coprimality loop
def coprime_test_loop():
    while True:  # Keep asking for input indefinitely, relies on the user to enter integers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Checking if they are coprime
        result = coprime(num1, num2)
        
        # print result
        if result:
            print(f"{num1} and {num2} are coprime.")
        else:
            print(f"{num1} and {num2} are not coprime.")
        
        # Asking if you want to continue
        continue_choice = input("Do you want to test another pair? (yes/no): ")
        if continue_choice.lower() == 'no':  # If the user wants to exit
            break  # Exit the loop

# Execute the coprime test
if __name__ == "__main__":  # Corrected this line
    coprime_test_loop()