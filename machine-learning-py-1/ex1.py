import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ITERATIONS = 200
ALPHA = 0.001

def computeCost(hypothesis,y):
    first_thing = (1. / (2. * len(y)))
    cost = np.sum(np.square(hypothesis - y))
    return first_thing * cost

def append_bias(X, length):
    bias = np.array([1] * length)
    return  np.array([bias, X])

def grabData():
    data = pd.read_csv('ex1data1.csv').as_matrix()
    X = data[:,0]
    y = data[:,1]
    return X, y, len(y)

def gradientDescent(X, y, theta, length):
    costs = []

    for iter in range(ITERATIONS):
      theta_0 = theta_update(theta, 0, X, y)
      theta_1 = theta_update(theta, 1, X, y)
      
      theta = np.array([theta_0, theta_1])
      #print('theta', theta)     
      hypothesis = np.dot(X.T, theta)
      print('cost:',computeCost(hypothesis, y))


def theta_update(theta, index, X, y):
    hypothesis = np.dot(X.T, theta)
    #print(hypothesis)
    error = hypothesis - y
    #print(error)
    s_error = error * X.T[:,index]
    #print('s_error', s_error)
    s_sum = sum(s_error)
    #print('s_sum',s_sum)
    alpha_error = ALPHA * s_sum
    #print('a', alpha_error)
    averaged = alpha_error / (2 * len(y)) 
    #print('averaged', averaged)
    return_value = theta[index] - averaged
    #print('return_value', return_value)
    return return_value

def plotData(X,y):
    plt.plot(X,y, 'ro')
    plt.xlabel('house size')
    plt.ylabel('price')
    plt.show()

def main():
    X, y, length = grabData()
    # plotData(X,y)
    X = append_bias(X, length)
    theta = np.array([0.,0.])
    # error = computeCost(hypothesis,y)
    # print(error)
    theta = gradientDescent(X, y, theta, length)

main()
