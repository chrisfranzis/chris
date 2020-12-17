
F = None

def _get_func(complexity):
    from random import uniform as u
    from math import cos, pi
    A = [u(0.0, 1.0) for _ in range(complexity)]
    f = [u(0.0, 0.1) for _ in range(complexity)]
    o = [u(0.0, 2.0) for _ in range(complexity)]
    O = u(0.0, 2.0)
    return lambda x: sum([A[i] * cos((f[i]*x+o[i])*pi) for i in range(complexity)])+O


def randfun(*args):
    global F
    if not F:
        F = _get_func(5)
    return [F(i) for i in range(*args)]


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.plot(randfun(1000))
    plt.show()