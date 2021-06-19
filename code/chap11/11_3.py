import numpy as np

def beta_1_reg(x, y, s_x):
    m_x = np.mean(x)
    m_y = np.mean(y)
    tmp = sum((x-m_x)*(y - m_y))
    tmp1 = sum((x-m_x)**2)

    return tmp / tmp1

def beta_0_reg(mean_x, mean_y, beta_1):
    return mean_y - mean_x * beta_1

def S_sqr(y, x, beta_0, beta_1):
    reg = beta_1 * x + beta_0
    return sum((y-reg)**2)

def sigma_comma(s_sqr, n):
    return (s_sqr/(n-2))**0.5

def U_0(beta_0, beta_0_star, sigma_comma, n, mean_x, s_x):
    return (beta_0 - beta_0_star) / (sigma_comma * (1/n + mean_x**2/s_x**2)**0.5)

def viz(x, y, beta_0, beta_1):
    from matplotlib import pyplot as plt

    plt.plot(x, y, 'o')
    plt.plot(x, beta_0 + beta_1*x)
    plt.show()

def U_01(c_0, n, mean_x, c_1, s_x, beta_0, beta_1, c_star, sigma_star):
    tmp0 = (c_0**2/n + (c_0*mean_x - c_1)**2 / (s_x**2))**-0.5
    tmp1 = ((c_0*beta_0 + c_1*beta_1 - c_star)/sigma_star)

    return tmp0 * tmp1

if __name__=="__main__1":

    x = np.array([0.3, 1.4, 1.0, -0.3, -0.2, 1.0, 2.0, -1.0, -0.7, 0.7])
    y = np.array([0.4, 0.9, 0.4, -0.3, 0.3, 0.8, 0.7, -0.4, -0.2, 0.7])
    n = len(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    s_x = (sum((x-m_x)**2))**0.5
    #s_x = np.std(x)
    beta_1 = beta_1_reg(x, y, s_x)
    beta_0 = beta_0_reg(m_x, m_y, beta_1)
    print("{} {}".format(beta_1, beta_0))
    S = S_sqr(y, x, beta_0, beta_1)
    sigma = sigma_comma(S, n)
    print(S)
    print(sigma)

    beta_0_star = 0.7
    u_0 = U_0(beta_0, beta_0_star, sigma, n, m_x, s_x)
    print("U_0: {}".format(u_0))



if __name__=="__main__2":
      
    x = np.array([0.3, 1.4, 1.0, -0.3, -0.2, 1.0, 2.0, -1.0, -0.7, 0.7])
    y = np.array([0.4, 0.9, 0.4, -0.3, 0.3, 0.8, 0.7, -0.4, -0.2, 0.7])
    n = len(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    s_x = (sum((x-m_x)**2))**0.5
    beta_1 = beta_1_reg(x, y, s_x)
    beta_0 = beta_0_reg(m_x, m_y, beta_1)
    S = S_sqr(y, x, beta_0, beta_1)
    sigma = sigma_comma(S, n)
    c_0 = 5
    c_1 = -1
    c_star = 0 
    u_01 = U_01(c_0, n, m_x, c_1, s_x, beta_0, beta_1, c_star, sigma)
    print(u_01)


if __name__=="__main__":
      
    x = np.array([0.3, 1.4, 1.0, -0.3, -0.2, 1.0, 2.0, -1.0, -0.7, 0.7])
    y = np.array([0.4, 0.9, 0.4, -0.3, 0.3, 0.8, 0.7, -0.4, -0.2, 0.7])
    n = len(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    s_x = (sum((x-m_x)**2))**0.5
    beta_1 = beta_1_reg(x, y, s_x)
    beta_0 = beta_0_reg(m_x, m_y, beta_1)
    S = S_sqr(y, x, beta_0, beta_1)
    sigma = sigma_comma(S, n)
    c_0 = 0
    c_1 = 1
    print(beta_1+beta_0)
    tmp = (c_0**2/n + (c_0*m_x - c_1)**2/s_x**2)**(-0.5)/sigma
    print(tmp)
