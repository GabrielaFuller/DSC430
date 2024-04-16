#Gabriela Fuller
#1/30/24
#DSC 430
#https://youtu.be/-nloRaLEeGw

#“I have not given or received any unauthorized assistance on this assignment”

def happynum(num):
    seen = set()
    while num != 1 and num not in seen: #while loop iterates until number reaches 1
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1, list(seen) #returns after the loop

def main():
    results = {}

    while True:
        try:
            user_input = input('Enter a positive number or type "end" to finish: ') #prompts user to enter a number or end
            if user_input.lower() == 'end':
                break
            num = int(user_input) #converts input to integer
            if num <= 0:
                print('Enter a positive number')
                continue
            ishappy, sequence = happynum(num)

            result_str = 'happy -u-' if ishappy else 'sad ;n; ' #response depending on iterations

            results[num] = (result_str, sequence) #stored in results dictionary

            print(f'{num} is a {result_str} number: {sequence}\n')
        except ValueError:
            print('Invalid entry, enter a positive number')

    print('\nSumming result')
    print(results)

if __name__ == '__main__':
    main()