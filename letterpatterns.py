# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3 
# 2 2 
# 1   
rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(i,0,-1):
        res+=str(i)+" "
    print(res)
    
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
rows=5
for i in range(rows,0,-1):
    res=""
    for sp in range(rows-i):
        res+=" "
    for j in range(1,i+1):
            res+="*"+" "
    print(res)

# *       *
# *       *
# * * * * *
# *       *
# *       *
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==3 or (j==1 or j==5):
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)