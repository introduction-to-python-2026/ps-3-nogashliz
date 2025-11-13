def approximate_pi(n_terms):
    n_series = 0
    for i in range(n_terms):
        n_series += (((-1)**i)/((2*i) + 1))
    return 4 * n_series
