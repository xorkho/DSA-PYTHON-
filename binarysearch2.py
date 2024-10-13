def BinarySearch(arr,query):
    low=0
    high=len(arr)-1
    count=0
    while low<=high:
        count+=1
        mid=(low+high)//2
        if arr[mid]==query:
            print(count)
            return mid
        elif arr[mid]<query:
            low=mid+1
        else:
            high=mid-1
    print(count)
    return "not found"
BinarySearch([11,23,25,37,41,46,58,63,75],1000)