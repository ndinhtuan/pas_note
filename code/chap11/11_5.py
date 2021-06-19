import numpy as np

def hat_beta_1d(x, y):
    return x @ y / np.sum(x**2)

def mle_vector_beta(z, y):
    tmp = np.linalg.inv(z@z.T) 
    tmp1 = tmp @ z
    y = np.expand_dims(y, 1)
    return tmp1 @ y

def determine_r_sqr(x, y, beta):
    
    print(beta.shape, x.shape)
    y_pred = beta.T @ x
    print(y_pred, y)
    y_avg = np.mean(y)
    e1 = (y_pred[0] - y)**2
    e2 = (y - y_avg)**2
    
    return 1 - np.sum(e1)/np.sum(e2)

if __name__=="__main__":
    
    # Data for exercise 5
    x = np.array([0.6, 1.0, 1.7, 1.7, 2.2, 2.2, 2.8, 3.5, 3.5, 4.2])
    y = np.array([8, 3, 5, 11, 10, 19, 9, 14, 22, 22])
    
    #print(hat_beta_1d(x, y))
    # data in 11.1 table
    x_1 = np.array([1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 4.6, 1.6, 5.5, 3.4])
    y_1 = np.array([0.7, -1.0, -0.2, -1.2, -0.1, 3.4, 0.0, 0.8, 3.7, 2.0])

    tmp = np.array([1 for i in range(len(x_1))])
    
    z = np.array([tmp, x_1, x_1**2])
    #print(z.shape)
    #print(mle_vector_beta(z, y_1))
    beta_hat = mle_vector_beta(z, y_1)
    print(determine_r_sqr(z, y_1,beta_hat))
