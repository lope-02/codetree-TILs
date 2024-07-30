a=list(input())
b=list(input())


'''
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

def decimal_to_ternary(decimal_number):
    if decimal_number == 0:
        return "0"
    ternary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 3
        ternary_number = str(remainder) + ternary_number
        decimal_number = decimal_number // 3
    return ternary_number
'''

def binary_to_decimal(binary_str):
    decimal = 0
    binary_str = binary_str[::-1]  # 뒤집어서 처리 (오른쪽에서 왼쪽으로)
    for i in range(len(binary_str)):
        decimal += int(binary_str[i]) * (2 ** i)
    return decimal

def ternary_to_decimal(ternary_str):
    decimal = 0
    ternary_str = ternary_str[::-1]  # 뒤집어서 처리 (오른쪽에서 왼쪽으로)
    for i in range(len(ternary_str)):
        decimal += int(ternary_str[i]) * (3 ** i)
    return decimal  

a_arr=[]
b_arr=[]

tmp_a=a
tmp_b=b

if a[0]=='0': a[0]='1'
    
else: 
    for i in range(1,len(a)):
        if a[i]=='0': tmp_a[i]='1'
        else: tmp_a[i]='0'
        print(tmp_a)
        a_arr.append(tmp_a)
      
        tmp_a=a
print(a_arr)
if b[0]=='0': b[0]='1'
    
else: 
    for i in range(1,len(b)):
        if a[i]=='0': tmp_b[i]='1'
        else: tmp_b[i]='0'
        b_arr.append(tmp_b)
       
        tmp_b=b
print(b_arr)

for i in range(len(a_arr)):
    a_arr[i]=binary_to_decimal(a_arr[i])

for i in range(len(b_arr)):
    b_arr[i]=ternary_to_decimal(b_arr[i])

print(a_arr)
print(b_arr)


for i in range(len(a_arr)):
    for j in range(len(b_arr)):
        if a_arr[i]==b_arr[j]: print(a_arr[[i]])