import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ITERATIONS = 2
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
      hypothesis = np.dot(X.T, theta)
      cost = computeCost(hypothesis, y)
      error = hypothesis - y
      print('cost', cost)
      print('error', error)
      print('error times x1', np.dot(error, X.T[:,0]))
      # print('sum', sum_of_errors_squared)
      theta_0 = theta[0] - np.dot(error, X.T[:,0]) / length * 2
      theta_1 = theta[1] - np.dot(error, X.T[:,1]) / length * 2
      # print(theta_0,theta_1)
      # print("theta when starting", theta)
      theta = np.array([theta_0, theta_1])
      # print("theta when done", theta)

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
