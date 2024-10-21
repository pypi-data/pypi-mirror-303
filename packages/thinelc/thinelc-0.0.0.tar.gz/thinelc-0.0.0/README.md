# Thin wrapper for ELC
Thin Python wrapper for a modified version of the Higher-Order Clique Reduction without Auxiliary Variables (ELC) algorithm by Vladimir Kolmogorov. The original source code by Vladimir Kolmogorov availbable at http://pub.ist.ac.at/~vnk/software.html.

## Installation
Install package using `pip install thinelc` or clone this repository (including. Building the package requires Cython.

## Tiny example
```python
from thinelc import PyPBF


def reduce(pbf, qpbf, mode, newvar):
    assert mode in (0, 1, 2)
    assert isinstance(newvar, int)
    
    if mode==0:
        pbf_tmp = pbf.copy()
        pbf_tmp.reduce_higher()
        pbf_tmp.to_quadratic(qpbf, newvar)
        
    elif mode==1:
        pbf_tmp = pbf.copy()
        pbf_tmp.reduce_higher_approx()
        pbf_tmp.to_quadratic(qpbf, newvar)
    else:
        pbf_tmp = pbf.copy()
        pbf.to_quadratic(qpbf, newvar)

# Create graph object.
pbf = PyPBF()

# Add edges.
pbf.add_unary_term(0, 0, 1)  # E(x)
pbf.add_unary_term(1, 0, 4)  # 4y
pbf.add_unary_term(2, 0, -1) # -z
pbf.add_pairwise_term(1, 3, 0, 2, 0, 0)  # -2(y-1)w

vars3 = [0, 1, 2]
vals3 = [0, 0, 0, 0, 0, 0, 1, 2]  # xy(z+1)
pbf.add_higher_term(3, vars3, vals3)

vars4 = [0, 1, 2, 3]
vals4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -2, 0, -2, 0, -4]  # -xw(y+1)(z+1)
pbf.add_higher_term(4, vars4, vals4)

print("Higher-order Function: ")
pbf.shrink()
pbf.print()
print("\n")

mode = 0
qpbf = PyPBF()
reduce(pbf, qpbf, mode, 4)

print("Quadratic Function (mode 0 - ELC+HOCR): ")
qpbf.shrink()
qpbf.print()
print("\n")
```

## License
As the ELC implementation is distributed under the GPLv3 license, so is this package.