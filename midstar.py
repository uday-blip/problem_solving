#program to print a star in the middle of the pattern
rows=int(input('enter the no:of rows:'))
for r in range(1,rows+1):
    pattern=""
    for c in range(1,rows+1):
        if (r==3 and c==3):
            pattern+="*"+" "  
        elif r==1 or c==1 or r==rows or c==rows:
            pattern+="!"+" "
        else:
            pattern+=" "+" "
    print(pattern)