import numpy as np

def compute_s_betw(array_n_i, array_mean_i):

    p = len(array_n_i)
    n = 0
    s = 0
    for i in range(p):
        s += array_n_i[i] * array_mean_i[i]
        n += array_n_i[i]

    s__ = s / n
    print(s__)
    s_betw = 0
    
    for i in range(p):
        s_betw += array_n_i[i] * (array_mean_i[i] - s__)**2

    return s_betw

def compute_s_resid(array_n_i, array_variance_i):

    s_resid = 0
    for n_i, variance_i in zip(array_n_i, array_variance_i):
        s_resid += (n_i-1) * variance_i

    return s_resid

if __name__=="__main__":
    
    sample_mean = [105.7, 102.0, 93.5, 110.8]
    sample_variance = [30.3, 54.4, 25.0, 36.4]

    n_i = [10 for _ in range(4)]

    s_betw = compute_s_betw(n_i, sample_mean)
    s_resid = compute_s_resid(n_i, sample_variance)

    n = 40
    p = 4
    print("U = ", (s_betw**2/(p-1)) / (s_resid**2/(n-p)))
