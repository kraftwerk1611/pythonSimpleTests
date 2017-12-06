y=0
x=121
n=16
j=n/2-1

while (j==0 or j>0):

    temp=pow((y+pow(2,j)),2)
    if temp<x or temp==x:
        y=y + pow(2,j)
    
    j=j-1

print y
