pattern = int(input("Enter the size of the pattern: "))

row = 0
while row < pattern:
    col = 0
    while col < pattern:
      print("*", end="")
      col += 1
    print()  # Move to the next line after each row
    row += 1
