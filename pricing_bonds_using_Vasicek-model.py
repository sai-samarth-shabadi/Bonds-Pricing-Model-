import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num_of_interest_rate_simulations = 1000
#num of points in one r(t)
num_of_points = 200


def Vasicek_model(r0, k= 0.9, theta = 0.07, T= 1, sigma = 0.05, n=num_of_points):
    #initiate all the interest rate to 0
    dt = T/float(n)
    t = np.linspace(0,T,n+1)
    r = [r0]
    for _ in range(n):
        dr = k*(theta - r[-1])* dt + sigma*np.random.normal(0, np.sqrt(dt))
        r.append(r[-1] + dr)

    return r

def calculate_price(x0, r0, t):
    data = {}
    dt = t / float(num_of_points)

    for i in range(num_of_interest_rate_simulations):
        data[i] = (Vasicek_model(r0))

    data = pd.DataFrame(data)
    data['mean'] = data.mean(axis=1)

    price = x0 * np.exp(-np.sum(data['mean'] * dt))
    return price

if __name__ == '__main__':

    price = calculate_price(1000, 0.04, 2)
    print('The bond price based on vasicek model using monte carlo simulations: %.2f' %price)