def quick(ds):
    if len(ds) < 2:
        return ds
    else:
        key = ds[0]
        left = [data for data in ds[1:] if data <= key]
        right = [data for data in ds[1:] if data > key]
        return quick(left) + [key] + quick(right)

dataset = [40,50,25]
print(quick(dataset))
