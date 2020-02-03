def remove_duplicate_words(s):
    alist = s.split()
    string = ""
    for i in alist:
        if i not in string:
            string += " "
            string += i
    return string[1:]

print(remove_duplicate_words("my cat is fat my cat"))






