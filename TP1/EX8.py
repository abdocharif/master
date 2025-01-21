def somme_varargs(*args):
    return sum(args)
print(somme_varargs(1, 2, 3))
print(somme_varargs(10, 20, 30, 40))
print(somme_varargs())