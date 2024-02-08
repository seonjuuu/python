def selection(ds):
    for a in range(0, len(ds)-1):
        min_ind = a
        for b in range(a+1, len(ds)):
            if ds[b] < ds[min_ind]:
                min_ind = b
        ds[a], ds[min_ind] = ds[min_ind], ds[a]

dataset = [20, 50, 30, 10, 60, 40]
selection(dataset)
print(dataset)
