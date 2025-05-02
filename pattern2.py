rows=int(input('enter no: of rows:'))
code=97
for i in range(1,rows+1):
    p=""
    for j in range(1,i+1):
        if j==1 or i==rows or i==j:
            p+=chr(code)+" "
            code+=1
        else:
            p+=" "+" "
            code+=1
    print(p)