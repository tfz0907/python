def mysort(arr):
    alen=len(arr)
    gap=alen//2
    while gap>=1:
        for j in range(gap,alen):
            i=j
            while (i-gap)>= 0:
                if arr[i]<arr[i-gap]:
                    arr[i],arr[i-gap]=arr[i-gap],arr[i]
                    i-=gap
                else:
                    break
        gap//=2
arr=[2,1,45,8,7,9,5]
mysort(arr)
print(arr)
