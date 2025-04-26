#program to print the sum of the digits in a number
dig=567
total=0
while dig>0:
    last=dig%10
    dig=dig//10
    total+=last
print(total)

#program to print a number in reverse order
dig=567
rev_dig=0
while dig>0:
    last=dig%10
    dig=dig//10
    rev_dig=rev_dig*10+last
print(rev_dig)

#program to find the factorial of the given number
num=7
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#program to print the middle characters in a given string
name='udayasree'
length=len(name)
if length%2==0:
    mid=name[length//2-1:length//2+1]
else:
    mid=name[length//2]
print(mid)

#program to print the middle value of the given number
num=9696
str_num=str(num)
length=len(str_num)
if length%2==0:
    mid_val=str_num[length//2-1:length//2+1]
else:
    mid_val=str_num[length//2]
print(mid_val)

#program to print True if the sum of 1st and last digits equals to the sum of middle digits 
num=765
str_num=str(num)
first_dig=int(str_num[0])
last_dig=int(str_num[-1])
first_final_sum=first_dig+last_dig
print(first_final_sum)
middle_sum=0
for i in range(1,len(str_num)-1):
    middle_sum=middle_sum+int(str_num[i])
print(middle_sum)
if middle_sum==first_final_sum:
    print('equals')
else:
    print('not equals')
    
#program to print that 1st and last digits are less than the remaining
num=2952
str_num=str(num)
first=int(str_num[0])
last=int(str_num[-1])
for i in range(1,len(str_num)-1):
     digit=int(str_num[i])
     if first<digit and last<digit:
         print('True')
     else:
         print('False')
         
#program to print to the vowels in a string in a reverse order
name='sannykumarbol'
vowels=['a','e','o','i','u']
vowels_found=[]
rev_vowels=[]
for i in name:
    if i in vowels:
        vowels_found.append(i)
print(vowels_found)
rev_vowels=vowels_found[::-1]
print(rev_vowels)

#Program to print the unique vowels in the string
hero='jacksparrow'
vowels=['a','e','i','o','u']
vowels_are=[]
unique_vowels=[]
v_c=0
for i in hero:
    if i in vowels:
        vowels_are.append(i)
print(vowels_are)
for j in vowels_are:
     if j not in unique_vowels:
         unique_vowels.append(j)
print(unique_vowels)

# Program to print the letters after removing the duplicates
text='racecar'
char_count={}
for char in text:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print(char_count)
for char, count in char_count.items():
    if count==1:
        print(char)

#Program to change upper case to lowercase and vice versa
car='AudIr8'
swapped=[]
for word in car:
    if 'A'<=word<='Z':
        swapped.append(chr(ord(word)+32))
    elif'a'<=word<='z':
        swapped.append(chr(ord(word)-32))
    else:
        swapped.append(word)
print(''.join(swapped))

#Program to print the 1st and last uppercase letters in reverse
example='NumberOne'
upper=[]
rev_upper=[]
lower=[]
final=[]
for i in example:
    if 65<=ord(i)<=90:
        upper.append(i)
    elif 97<=ord(i)<=122:
        lower.append(i)
    else:
        final.append(i)
rev_upper=upper[::-1]
final=rev_upper+lower
print(''.join(final))
numbers=[3, 1, 4, 1, 5, 9]
big=numbers[0]
for dig in numbers:
    if dig>big:
        big=dig
print(dig)

#Program to print the 1st big and 2nd big in a list
num=[1,26,56,43,10,8,21]
big=float("-inf")   #lowest
sec_big=float("-inf")
for current in num:
    if current>big:
        sec_big=big
        big=current
    elif current!=big and current>sec_big:
        sec_big=current
print(big,sec_big)

#Program to print the sum of all elements in a array
from functools import reduce
kii=[1,2,3,4,5]
sum=reduce(lambda u,v:u+v,kii)
print(sum)
#
plus=0
for i in range(len(kii)):
      plus+=kii[i]
print(plus)

#Program to remove the duplicate from the list of numbers
input= [1,2,2,3,4,4,5] 
unique=[]
for i in range(len(input)):
    if input[i] not in unique:
        unique.append(input[i])
print(unique)

#program to print true if the list is sorted in ascending order 
u=[1,2,3,4,5] 
new_u=sorted(u)
print(new_u)
if u==new_u:
    print('True')
else:
     print('False')

#program to reverse an list
input=[10,40,55,73,21] 
rev_list=[]
for i in range(len(input)-1,-1,-1):
    rev_list.append(input[i])
print(rev_list)

#program to remove the falsey values from a list
input=[1,0,'false',2,"",3]
truth=[element for element in input if isinstance(element,(int,float)) and element!=0]
print(truth)

#Program to print the unique items of a list
uday=[1,2,2,3,4,4,5]
unique=[]
not_unique=[]
for i in uday:
    if uday.count(i)==1:
        unique.append(i)
    elif uday.count(i)>1:
        not_unique.append(i)
    else:
        print('can not be determined')
print(uday)
print(unique)
print(not_unique)

#Program to print the sum of even digits in a list
list=[1,2,3,4,5] 
even_sum=0
for i in list:
     if i%2==0:
         even_sum+=i
print(even_sum)

#Program to print a string in reverse order
car='volkswagenpolo'
reverse=[]
for i in  range(len(car)-1,-1,-1):
     reverse.append(car[i])
print(''.join(reverse))  

#program to check whether it is a palindrome or not
mine='madam'
you=mine[::-1]
if mine==you:
    print('palindrome')
else:
    print('not palindrome')

#program to print count of vowels
text='helloworld'
vowels=['a','e','i','o','u']
v_c=0
for i in text:
    if i in vowels:
       v_c+=1
print(v_c)

#program to remove the vowels from a string
word='saibabu'
vowels='aeiouAEIOU'
no_vowel=[]
for char in word:
    if char not in vowels and char!=" ":
        no_vowel.append(char)
print("".join(no_vowel))

#Program to title the string
greet='hello world'
capital=greet.title()
print(capital)

#Program to convert a string into a number
string='123'
changed=[]
for char in string:
    number=ord(char)-ord('0')
    changed.append(number)
print(changed)
print(type(changed[2]))

#program to check whether all the items are numbers are not
pin='1564'
is_pin=pin.isdigit()
print(is_pin)

#program to find the no:of occurences of a character
name='udaybabu'
occur_of_u=name.count('u')
print(occur_of_u)

#program to  convert a list into a dictionary
him=[['name','uday'],['age','21']]
converted=dict(him) 
print(converted)   

#program to merge two dictionaries
dict_1={'name':'uday'}
dict_2={'age':'21'}
dict_1.update(dict_2)
print(dict_1)

#program to count the objects,get keys and get values in a dictionary
dict_1={'a':1,'b':2,'c':3}
req=dict_1.items()
key=dict_1.keys()
val=dict_1.values()
print(req)
print(key)
print(val)
print(len(req))

#program to check that whether a dictionary is empty or not 
details={}
size=len(details)
if size==0:
    print('True (this dictionary is empty)')
else:
    print('False')
