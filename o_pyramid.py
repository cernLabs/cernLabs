# prompt user to input number of rows for the pyramid
print("enter the number of rows: ")
r = int(input())

# build pyramid
for i in range(r+1):
 for j in range(i+1):
  print('o', end=' ')
 print('')
