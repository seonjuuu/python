def insertion(ds):
    for a in range(1, len(ds)):
        key = ds[a]
        b = a-1
        while b>=0 and ds[b]>key:
            ds[b+1] = ds[b]
            print("a")
            b = b-1
        ds[b+1] = key

dataset = [11,9,3,8]
insertion(dataset)
print(dataset)
