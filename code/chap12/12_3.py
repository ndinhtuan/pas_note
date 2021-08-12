import numpy as np

def get_prob_glivenko_cantelli(t, n):

    a = 0
    for i in range(1, n+1):
        a += (-1)**(i-1)*np.e**(-2*(i**2)*(t**2))

    return 1 - 2*a

if __name__=="__main__1":
    
    t = 0.0082/(60000**-0.5)
    print(get_prob_glivenko_cantelli(t, 20000)**3)

import matplotlib.pyplot as plt
import numpy as np

def generate_uniform(num, gamma=1):

    results = []

    for i in range(num):
        gu = np.random.uniform(0, 1)
        ge = -np.log(1-gu)/gamma
        results.append(ge)

    return results

def compute_mse(num, theta=np.log(2)):
    
    results = 0

    for i in range(num):
        r_ = generate_uniform(2000)
        results += (sorted(r_)[1001]-theta)**2

    return results / num

def exer1(viz=False):
    
    ges = compute_mse(100)
    print(ges)
    
    if viz:
        plt.scatter(x=range(2000), y=ges)
        plt.show()

if __name__=="__main__":
    exer1()
