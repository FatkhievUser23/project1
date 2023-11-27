def n(chislo):
    if chislo <2:
        return False
    for i in range(2, int(chislo**0.5)+1):
        if chislo%i == 0:
            return False
    return True

ch = 12
res = n(ch)
print(res)