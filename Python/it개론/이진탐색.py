def binary(ds, key):
    low = 0
    high = len(ds)-1
    while low <= high:
        mid = (low+high)//2
        print("pdp",mid)
        if key == ds[mid]:
            return mid
        elif key < ds[mid]:
            high = mid-1
        else:
            low = mid+1
    return

dataset = [1,5,9,14,20,22,30]
print(binary(dataset, 9))
