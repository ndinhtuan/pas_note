import numpy as np

def trimmed_means(k, arr):
    
    sorted_arr = sorted(arr)
    trimmed_mean = sorted_arr[k:len(arr)-k]
    return np.mean(trimmed_mean)

def sample_median(arr):
    sorted_arr = sorted(arr)
    len_ = len(sorted_arr)
    pivot = len_//2
    if len_ % 2:
        return (sorted_arr[pivot] + sorted_arr[pivot-1])/2
    else:
        return sorted_arr[pivot]

def sample_median_absolute_deviation(arr):
    sample_median_ = sample_median(arr)
    sample_absolute_deviation = [abs(i-sample_median_) for i in arr]
    return sample_median(sample_absolute_deviation)

def M_estimator(arr, k, sigma=None):
    
    if sigma is None:
        sigma = sample_median_absolute_deviation(arr)/0.6745
    
    def psi_k(y, k):
        if y < -k: return -k
        if -k <= y and y <= k: return y
        if y > k: return k
    
    def weight_x(x, theta, k, sigma):
        if x == theta:
            return 1
        else:
            return psi_k((x-theta)/sigma, k)/(x-theta)

    NUM_ITER = 10
    hist_theta = []
    
    theta = sample_median(arr)

    for i in range(NUM_ITER):
        ws = []
        for x in arr:
            ws.append(weight_x(x, theta, k, sigma))

        theta = sum(np.array(ws)*np.array(arr)) / sum(ws)
        hist_theta.append(theta)
        print("Step {}: {}".format(i, theta))
    print(hist_theta)

if __name__=="__main__":
    arr = [23, 21.5, 63.0, 22.5, 2.1, 22.1, 22.4, 2.2, 21.7, 21.7, 22.2, 22.9, 21.3, 21.8, 22.1]
    print(trimmed_means(3, arr))
    print(sample_median(arr))
    M_estimator(arr, k=1.5)   
