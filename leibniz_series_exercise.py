def approximate_pi(n):
    n = 0
    for i in range(n):
        n_series += (((-1)**i)/((2*i) + 1))
    return (4*n_series)
