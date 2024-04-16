#Gabriela Fuller
#I have not given or received any authorized assistance on this assignment
#DSC 430
#https://youtu.be/hzKvRGKdLmg

def greet():
    print("I generate stem-and-leaf plots.") #printing user greeting

def get_user_input(): #user prompt to enter a number
    return input("Enter 1, 2, or 3 to choose a datafile, or 0 to exit: ")

def read_datafile(user_input): #read respective file from the file directory
    file_paths = {
        '1': r"C:\Users\Gabi Fuller\DSC430\StemAndLeaf1.txt",
        '2': r"C:\Users\Gabi Fuller\DSC430\StemAndLeaf2.txt",
        '3': r"C:\Users\Gabi Fuller\DSC430\StemAndLeaf3.txt"
    }

    if user_input in file_paths: #checks user input if its valid, retrieves the open file and reads the data if it's valid
        file_path = file_paths[user_input]
        with open(file_path, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    else:
        print("Invalid input. Please enter 1, 2, 3, or 0.")
        return []

#defines stem and leaf plot 
def display_stem_and_leaf(data):
    print("Stem-and-leaf plot:")
    if len(data) == 0:
        print("No data to display.")
        return
    
    #stem and leaf calculation and sorting

    stems = set(x // 10 for x in data)
    for stem in sorted(stems):
        leafs = [x % 10 for x in data if x // 10 == stem]
        leafs_str = " ".join(map(str, sorted(leafs))) #leaf extraction and formatting
        print(f"{stem}| {leafs_str}") #plot output

def main(): #defines main functin, greeting, main loop, and user input and exit condition
    greet()
    while True:
        user_input = get_user_input()
        if user_input == '0':
            print("Exiting the program. Goodbye!")
            break
        elif user_input in ['1', '2', '3']: #data handling and handles valid or invalid input
            data = read_datafile(user_input)
            display_stem_and_leaf(data)
        else:
            print("Invalid input. Please enter 1, 2, 3, or 0.")

if __name__ == "__main__": #execution check
    main()