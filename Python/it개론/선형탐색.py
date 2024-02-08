def linear(ds, key):
    for a in range(0, len(ds)):
        if key == ds[a]:
            return a
    return

dataset = [20, 50, 30, 10, 60, 40]
print(linear(dataset, 10))
