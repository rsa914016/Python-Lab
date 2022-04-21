def isEven(even):
    if even % 2 == 0:
        return True
    return False


def isOdd(odd):
    if odd % 2 == 1:
        return True
    return False


def reverseString(string):
    if type(string) is not str:
        raise TypeError('This Function Only Used To Reverse The Strings')
    return string[::-1]
