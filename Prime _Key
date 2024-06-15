def check_prime(m):
    flag=0
    if m<0:
        flag=1
    elif m==0:
        flag=0
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=1
                break
    if flag==0:
        return 1
    else:
        return 0
#Finding smallest prime number larger than a given integer N        
result=[]        
N=int(input())     
flag=0
k=N+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
#calculating the sum of all prime numbers between N and smallest prime number larger than N       
sum=0
for i in range(N+1,k):
    sum+=i
result.append(sum)

p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1  
#determining if the product of the smallest prime number larger than N and next immediate prime number is also a prime number        
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)

Prime_key=tuple(result) #output is like if u given an input as 7 then next prime number.will be 11 and the in between 7 and 11 their is 8+9+10=27,
#their should be 27 and next to 11 prime number is 13.Then multipy the 11*13 then the output should not be prime number then it is false
print(Prime_key)
    
