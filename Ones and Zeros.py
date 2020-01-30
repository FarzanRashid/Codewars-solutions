def binary_array_to_number(arr):
    out = ""
    for i in arr:
        var = str(i)
        out+= var
    return int(out, 2)