def binary_search(start,end,a,k):
    if (start>=end):
        for _ in a:
            mid=(start+end)//2
            if a[mid]==k:
                return mid
            elif a[mid]>k:
                return binary_search(start,mid,a,k)
            else:
                return binary_search(mid+1,end,a,k)
    else:
        return -1
n=int(input('enter a number of element:'))
a=[]
for i in range(n):
    a.append(int(input('enter a items:')))
a.sort()
print('the sorted list is :',a)
k=int(input('enter a search item:'))
r=binary_search(0,n-1,a,k)
if (r==-1):
    print("element not found")
    exit()
else:
    print(f"found at index {r}")
    exit()
