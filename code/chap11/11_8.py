import numpy as np

def compute_mle_mu(data, IJK):
    
    return np.sum(np.sum(data)) / IJK

def compute_mle_alpha_i(data, i, mle_mu, JK):
    tmp1  = np.sum(np.sum(data[i])) / JK
    return tmp1 - mle_mu

def compute_mle_beta_j(data, j, mle_mu, IK):
    tmp1 = np.sum(np.sum(data[:,j,:])) / IK
    return tmp1 - mle_mu

def compute_mle_gamma_ij(data, i, j, mle_mu, \
        mle_alpha_i, mle_beta_j, K):
    
    tmp = np.sum(data[i][j]) / K
    return tmp - (mle_mu + mle_alpha_i + mle_beta_j)

def compute_s_int_sqr(data, I, J, K):
    
    mle_mu = compute_mle_mu(data, I*J*K)

    tmp = 0
    for i in range(I):
        mle_alpha_i = compute_mle_alpha_i(data, i, mle_mu, J*K)
        for j in range(J):
            mle_beta_j = compute_mle_beta_j(data, j, mle_mu, I*K)
            mle_gamma_ij = compute_mle_gamma_ij(data, i, j, mle_mu, \
                    mle_alpha_i, mle_beta_j, K)
            tmp += mle_gamma_ij**2

    return K*tmp

def compute_s_resid_sqr(data, I, J, K):
    
    tmp = 0

    for i in range(I):
        for j in range(J):
            tmp1 = np.sum(data[i][j]) / K
            for k in range(K):
                
                tmp += (data[i][j][k] - tmp1)**2

    return tmp

def compute_U_A(data, I, J, K):

    s_int_sqr = compute_s_int_sqr(data, I, J, K)
    s_resid_sqr = compute_s_resid_sqr(data, I, J, K)
    s_a_sqr = compute_s_a_sqr(data, I, J, K)

    return (I*J*(K-1)*(s_int_sqr+s_a_sqr)) / ((I-1)*J*s_resid_sqr)

def compute_U_B(data, I, J, K):

    s_int_sqr = compute_s_int_sqr(data, I, J, K)
    s_resid_sqr = compute_s_resid_sqr(data, I, J, K)
    s_b_sqr = compute_s_b_sqr(data, I, J, K)

    return (I*J*(K-1)*(s_int_sqr+s_b_sqr)) / (I*(J-1)*s_resid_sqr)

def compute_U_AB(data, I, J, K):

    s_int_sqr = compute_s_int_sqr(data, I, J, K)
    s_resid_sqr = compute_s_resid_sqr(data, I, J, K)

    return (I*J*(K-1)*s_int_sqr) / ((I-1)*(J-1)*s_resid_sqr)

def compute_U_alpha(data, I, J, K, i, alpha_h):
    
    mle_mu = compute_mle_mu(data, I*J*K)
    mle_alpha_i = compute_mle_alpha_i(data, i, mle_mu, J*K)
    s_resid_sqr = compute_s_resid_sqr(data, I, J, K)

    return (I*J*(K-1)*(mle_alpha_i-alpha_h)) / ((I-1)*J*s_resid_sqr)

def compute_U_beta(data, I, J, K, j, beta_h):

    mle_mu = compute_mle_mu(data, I*J*K)
    mle_beta_j = compute_mle_beta_j(data, j, mle_mu, I*K)
    s_resid_sqr = compute_s_resid_sqr(data, I, J, K)

    return (((I*J*(K-1))**0.5)*(mle_beta_j-beta_h)) / (s_resid_sqr**0.5 * ((I-1)/(I*J*K))**0.5)

def compute_s_a_sqr(data, I, J, K):
    
    mle_mu = compute_mle_mu(data, I*J*K)
    tmp = 0

    for i in range(I):
        mle_alpha_i = compute_mle_alpha_i(data, i, mle_mu, J*K)
        tmp += mle_alpha_i**2

    return J*K*tmp

def compute_s_b_sqr(data, I, J, K):
    
    mle_mu = compute_mle_mu(data, I*J*K)
    tmp = 0

    for j in range(J):
        mle_beta_j = compute_mle_beta_j(data, j, mle_mu, I*K)
        tmp += mle_beta_j**2

    return tmp * I * K

if __name__=="__main__":

    I = 4
    J = 3
    K = 2
    data = [[[11.2, 11.6] ,[12.7, 14.0], [10.1, 9.6]], [[7.4, 8.1],\
    [10.3, 7.9], [5.5, 6.9]], [[7.1, 7.0] ,[8.8, 8.5], [5.0, 7.3]],\
    [[9.6, 7.6], [11.3, 10.8], [6.5, 5.7]]]
    data = np.array(data)
    print(compute_U_beta(data, I, J, K, 1, 1))
