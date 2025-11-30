
size = int(input("Enter the size of the pattern:  "))
       
current_row = 1
while current_row <= size:
    for current_col in range(size):
        print("*", end="")
    print()
    
    current_row += 1