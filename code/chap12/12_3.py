import numpy as np

def get_prob_glivenko_cantelli(t, n):

    a = 0
    for i in range(1, n+1):
        a += (-1)**(i-1)*np.e**(-2*(i**2)*(t**2))

    return 1 - 2*a

if __name__=="__main__":
    
    t = 0.0082/(60000**-0.5)
    print(get_prob_glivenko_cantelli(t, 20000)**3)
