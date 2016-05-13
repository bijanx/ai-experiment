import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ITERATIONS = 900
ALPHA = 0.03

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
    for iter in range(ITERATIONS):
      theta_0 = theta_update(theta, 0, X, y)
      theta_1 = theta_update(theta, 1, X, y)
      theta = np.array([theta_0, theta_1])
      #print('theta', theta)     
      hypothesis = np.dot(X.T, theta)
      #print('cost:', computeCost(hypothesis, y))
    return theta

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

def plotRealData(X,y):
    plt.plot(X,y, 'ro')
    plt.xlabel('house size')
    plt.ylabel('price')

def plotPredictionLine(theta,X, y):
    # creates an array of data points
    x = np.linspace(np.amax(y),np.amin(X),100)
    y = theta[0] + theta[1] * x 
    plt.plot(x,y)

def main():
    ox, y, length = grabData()
    X = append_bias(ox, length)
    theta = np.array([0.,0.])
    theta = gradientDescent(X, y, theta, length)
    print('final_cost:', computeCost(np.dot(X.T,theta), y))
    plotRealData(ox,y)
    plotPredictionLine(theta,X, y)
    plt.show()
    
main()
