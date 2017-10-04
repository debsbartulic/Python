def numero_perfeito(num):
    res = 0
    total = 0
    aux = num
    while (res != 1):
        if (aux % 2 == 0):
            res = aux / 2
            total = total + res
        else:
            res = aux / 2 + 1
            total = total + res
        aux = aux / 2
    if (total == num):
        return True
    else:
        return False