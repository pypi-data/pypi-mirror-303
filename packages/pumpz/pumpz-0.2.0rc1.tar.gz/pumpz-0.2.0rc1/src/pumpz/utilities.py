import sympy

def decompose_dict(dict: dict) -> list:
    r = []
    for key in dict:
        for i in range(dict[key]):
            r.append(key)
    return r

def factor_check(initial_factor, attempt=0) -> tuple:

    if isinstance(initial_factor, int):
        initial_factor = decompose_dict(sympy.factorint(initial_factor))

    if not isinstance(initial_factor, list):
        raise Exception("initial_factor should be int or list")

    if any(x > 99 for x in initial_factor):
        return (0, 0)
    factor = initial_factor.copy()
    a = 0
    b = 0
    i = 0
    if len(factor) == 1:
        return (0, 0)
    while i < len(factor):
        if factor[i] * factor[i + 1] < 99:
            factor[i + 1] = factor[i] * factor[i + 1]
            factor[i] = 1
            i += 1
        else:
            a = factor[i]
            factor[i] = 1
            i = len(factor)
    b = sympy.prod(factor)
    if b <= 99:
        return (a, b)
    else:
        return (a, factor_check(decompose_dict(sympy.factorint(b))))