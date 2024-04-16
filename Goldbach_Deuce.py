#Gabriela Fuller
#1/30/24
#DSC 430
#“I have not given or received any unauthorized assistance on this assignment”
#https://youtu.be/7IPeuFUau14
import random

def find_sum(numbers, target_sum): #finds 2 numbers in a sorted list that sum to a target using binary search and returns a tuple of two integers that meet the target sum
    for i, num in enumerate(numbers):
        complement = target_sum - num
        left, right = i + 1, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < complement:
                left = mid + 1
            elif numbers[mid] > complement:
                right = mid - 1
            else:  # Found the complement
                return i, mid #returns 

    return None

def main():
    length = int(input("Enter the length of the list: "))
    target_sum = int(input("Enter the target sum: "))

    #generate random numbers in a range
    random.seed(0)  # Set a seed for consistency across runs
    numbers = [random.randint(0, 100) for _ in range(length)]

    numbers.sort() #sort the list in 0(n log (n)) using merge sort
    pair_indices = find_sum(numbers, target_sum)
    if pair_indices:
        num1, num2 = numbers[pair_indices[0]], numbers[pair_indices[1]]
        print("Numbers:", num1, num2, "sum to:", target_sum)
    else:
        print("No pair found that sums to:", target_sum)

if __name__ == "__main__":
    main()

