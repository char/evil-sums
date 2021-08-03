from math import floor, sqrt
from typing import Generator

# https://oeis.org/A096858 :
# b[n_] := b[n] = If[n < 2, n, 2*b[n-1] - b[n-1-Floor[1/2 + Sqrt[2*n-2]]]];
# t[n_] := Table[b[n] - b[n-i], {i, 1, n}]; Table[t[n], {n, 1, 15}]


def _conway():
    seq = [0, 1, 2]
    yield from seq
    while True:
        n = len(seq)
        x = seq[-1] * 2 - seq[n - 1 - floor(0.5 + sqrt(2 * n - 2))]
        yield x
        seq.append(x)


def generate_options(size: int) -> Generator[int, None, None]:
    c = _conway()
    c = [next(c) for _ in range(size + 1)]
    for i in range(1, size + 1):
        yield c[size] - c[size - i]
