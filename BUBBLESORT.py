arr=[5,2,5,7,8,9,-2,11,9,22]
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
