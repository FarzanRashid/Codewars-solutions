def sort_array(source_array):
    odd = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            odd.append(source_array[i])
            source_array[i] = "n"
    odd.sort()
    index = 0
    for v in range(len(source_array)):
        if source_array[v] == "n":
           source_array[v] = odd[index]
           index += 1
    return source_array