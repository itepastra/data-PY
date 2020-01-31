import sympy


def partial(function, var):
    return sympy.diff(f, x)


def diffmethode(function, uncertainties, vars_=None):
    if vars_ is None:
        vars_ = function.free_symbols
    return sqrt(
        sum(
            [
                (partial(function, var) * sig) ** 2
                for var, sig in zip(vars_, uncertainties)
            ]
        )
    )
