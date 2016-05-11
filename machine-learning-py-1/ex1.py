import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ITERATIONS = 15
ALPHA = 0.001

def computeCost(X, y, theta, length):
    i_cost = 0

    # something with the math here is wrong
    # I need to make sure I understand exactly
    # what each matrix is supposed to do and then
    # how the operations look under the hood
    for i in range(length):
        hypothesis = theta[0] + theta[1] * X[i]
        i_cost = i_cost + np.sum(np.square(hypothesis - y[i]))
    final_cost = i_cost * 1 / (2 * length)
    #print(final_cost)

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
    hypothesis = theta[0] + theta[1] * X.transpose()
    costs = [] 

    for iter in range(ITERATIONS):
      hypothesis = np.dot(theta.transpose(), X)
      error = hypothesis - y
      temp_theta_0 = theta[0] - ALPHA * np.sum(np.dot(error ** 2, X[:,1])) / (2 * length)
      temp_theta_1 = theta[1] - ALPHA * np.sum(np.dot(error ** 2, X[:,2])) / (2 * length)
      theta = np.array([temp_theta_0, temp_theta_1])
      print(theta)

def plotData(X,y):
    plt.plot(X,y, 'ro')
    plt.xlabel('house size')
    plt.ylabel('price')
    plt.show()

def main():
    X, y, length = grabData()
    # plotData(X,y)
    X = append_bias(X, length) 
    theta = np.array([0,0])
    theta = gradientDescent(X, y, theta, length)
     

main()
