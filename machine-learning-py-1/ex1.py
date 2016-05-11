import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ITERATIONS = 5
ALPHA = 0.001

def computeCost(hypothesis,y):
    first_thing = (1. / (2. * len(y)))
    print('hypothesis', hypothesis)
    print('error', hypothesis - y)
    print('error sqaured', np.dot(hypothesis, hypothesis))
    cost = np.sum(np.square(hypothesis - y))
    print('cost', cost)
    final_cost = first_thing * cost

    return final_cost

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
      error = computeCost(X,y,theta,length)
      x1 = ALPHA / 2 * length
      sum_of_errors_squared = np.sum(np.dot(error**2, X.T)) * ALPHA
      # print('sum', sum_of_errors_squared)
      theta_0 = theta[0] - sum_of_errors_squared / length * 2
      theta_1 = theta[1] - sum_of_errors_squared / length * 2
      # print(theta_0,theta_1)
      print("theta when starting", theta)
      theta = np.array([theta_0, theta_1])
      print("theta when done", theta)

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
    hypothesis = np.dot(X.T, theta)
    error = computeCost(hypothesis,y)
    print(error)
    # theta = gradientDescent(X, y, theta, length)

main()
