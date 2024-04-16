#Gabriela Fuller
#2/8/24
#https://youtu.be/i6sHm98OoNk
#DSC 430
#“I have not given or received any unauthorized assistance on this assignment”

def humanpyramid(row, column): #calculates total weight on persons back in pyramid 
    if row == 0:
        return 0 #row of person on 0-based index
    if column == 0 or column == row: 
        return 128  #column of person on 0-based index, returns total weight based on each person's shoulders divded by 2
    left = humanpyramid(row - 1, column - 1)
    right = humanpyramid(row - 1, column)
    return left + right + 128
total_weight_on_l = humanpyramid(4, 2)  # Person L
print(f"Total weight on L's back: {total_weight_on_l} pounds")