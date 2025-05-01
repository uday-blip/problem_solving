rows=int(input('enter the no: of rows:'))
for row in range(1,rows+1):
    pattern=""
    for col in range(1,rows+1):
        pattern+=str(row)+' '
    print(pattern)

rows=5
for i in range(1,rows+1):
    pattern=""
    for col in range(1,i+1):
        pattern+=str(i)+' '
    print(pattern)