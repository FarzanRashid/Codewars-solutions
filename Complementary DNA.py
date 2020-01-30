def DNA_strand(dna):
    output =  ""
    for i  in dna:
        if i == "T":
            output += "A"
        elif i == "A":
            output += "T"
        elif i == "G":
            output += "C"
        else:
            output += "G"
    return output