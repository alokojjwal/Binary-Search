def binsearch(n,x):
    first_pos=0
    last_pos=len(n)
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==n[mid]):
            flag=1
            print("The number is found at ",(mid + 1))
            print("The number of iterations "+str(count))
            return
        if(x<n[mid]):
            last_pos=mid-1
        else:            
            first_pos=mid+1
    print("The number is not present")
    
p=int(input("Enter the range of numbers to be searched: "))
q=int(input("Enter the number to be searched: "))
a=[]
for i in range(1,p):
    a.append(i)
binsearch(a,q)