def automorphic(n):
    squared = str(n ** 2)
    if squared.endswith(str(n)):
        return "Automorphic"
    return "Not!!"
