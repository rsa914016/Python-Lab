def Ex09a(s1, s2):
    count, i, j = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            count += 1
            if len(s1) > len(s2):
                i += 1
            elif len(s1) == len(s2):
                pass
            else:
                i -= 1
            if count > 1:
                return False
        i += 1
        j += 1
    if count < 2:
        return True


def Ex09b(lst):
    dups = [i for i in lst if lst.count(i) > 1]
    print('Duplicates are :', *set(dups))


def Ex09c(lst):
    print('Unique Values  :', *set(lst))


if __name__ == '__main__':
    print(Ex09a('ajay', 'Ajay'))
    Ex09b([1, 2, 3, 4, 2, 1, 4, 7])
    Ex09c([1, 2, 3, 4, 2, 1, 4, 7])
