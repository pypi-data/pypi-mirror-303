from __future__ import annotations
import time
import pyconcord as pc

import numpy as np


n_values = [0, 1, 2, 17]

def test_robust_concord():
    x = np.random.randn(13, 9)

    n, p = x.shape
    s = time.time()
    lam = pc.RobustSelection(x, alpha=0.95, B=200, with_diag=False)
    e = time.time()
    print(f"Time to finish robust selection: {e - s:.2f}")
    s = time.time()
    omega = pc.concord(x, lambda1=lam)
    e = time.time()
    print(f"Time to finish concord: {e - s:.2f}")
    
    cov = np.round(omega.todense(), 2)
    assert ~np.isinf(cov[0,0])
    assert cov[0, 1] == cov[1, 0]

def test_basic_concord():
    x = np.random.randn(13, 9)

    n, p = x.shape
    
    print(pc.concord.__doc__)
    omega = pc.concord(x, lambda1=0.3)
    
    cov = np.round(omega.todense(), 2)
    assert ~np.isinf(cov[0,0])
    assert cov[0, 1] == cov[1, 0]

def test_concord_w_guess():
    from scipy.sparse import identity

    x = np.random.randn(13, 9)

    n, p = x.shape
    
    x0 = identity(p).tocoo()
    
    omega = pc.concord(x, x0=x0, lambda1=0.3)
    cov = np.round(omega.todense(), 2)
    assert ~np.isinf(cov[0,0])
    assert cov[0, 1] == cov[1, 0]

def test_speed():
    # Smaller lambda takes longer time
    lambdas = np.exp(np.linspace(np.log(5e-2), np.log(5e-1), 10))

    data_large = np.random.randn(200, 200)
    import time
    for lam in lambdas:
        start = time.time()
        sparse_arr = pc.concord(data_large, lambda1=lam)
        np.asarray(sparse_arr.todense())
        end = time.time()
        print(f"Elapsed for concord at lambda {lam:.3f} NZ={sparse_arr.nnz / (sparse_arr.shape[0]*(sparse_arr.shape[0]-1))*100:.2f}% time= {(end - start):.3f}s")

