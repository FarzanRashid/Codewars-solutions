def unique_in_order(iterable):
    output = []
    for i in iterable:
        if i not in output:
            output.append(i)
        elif  i != output[-1]:
            output.append(i)
    return output