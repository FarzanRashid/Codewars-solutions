import string


def toJadenCase(input_string):
    return string.capwords(input_string, sep = " ")