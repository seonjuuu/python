def bubble(ds):
    for a in range(0, len(ds)-1):
        for b in range(0, len(ds)-1-a):
            if ds[b] > ds[b+1]:
                ds[b], ds[b+1] = ds[b+1], ds[b]
            print("a")

dataset = [20, 50, 30, 10, 60, 40]
bubble(dataset)
print(dataset)
