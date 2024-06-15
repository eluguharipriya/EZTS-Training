#You are given an integer array of size N, representing jars of chocolates. Three students A, B,and C respectively, will pick chocolates one
#by one from each chocolate jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task is to fine and return an
#integer value representing the total number of chocolates that student A will have, after all the chocolates have been picked from all the jars.
#Note: Once a jar is done A will start taking the chocolates from the new jar. 
chocolate=list(map(int,input('Enter the number of Chocolates in each jar').split()))
N=len(chocolate)
count=0
for i in chocolate:
    if i==0:
        continue
    if i<=3:
        count+=1
    else:
        if i%3==0:
            count=count+(i//3)
        else:
            count=count+(i//3)+1
print(count)
