import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

ITERATIONS = 100
ALPHA = 0.3

def computeCost(hypothesis,y):
    first_thing = (1. / (2. * len(y)))
    cost = np.sum((hypothesis - y).T * (hypothesis - y))
    return first_thing * cost

def grabData():
    data = pd.read_csv('ex1data2.csv').as_matrix()
    X = np.array([np.array([1] * len(data[:,0])),data[:,0], data[:,1]])
    y = data[:,2]
    return X, y, len(y)

def gradientDescent(X, y, theta, length):
    for iter in range(ITERATIONS):
        theta_output = []
        for feature in range(len(X)):
            theta_output.append(theta_update(theta, feature, X, y))
        print('theta output', theta_output)
        theta = theta_output
    return theta

def theta_update(theta, index, X, y):
    hypothesis = np.dot(X.T, theta) 
    error = hypothesis - y
    s_error = error * X[index]
    s_sum = sum(s_error)
    alpha_error = ALPHA * s_sum
    averaged = alpha_error / (2 * len(y)) 
    return_value = theta[index] - averaged
    return return_value

def plotRealData(X,y):
    plt.plot(X,y, 'ro')
    plt.xlabel('house size')
    plt.ylabel('price')

def plotPredictionLine(theta,X, y):
    x = np.linspace(np.amax(y),np.amin(X),100)
    y = theta[0] + theta[1] * x 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

def predict(size, rooms, theta):
    print('predict theta', np.array(theta))
    print('np.array([size,rooms])', np.array([[size],[rooms]]))
    return np.sum(theta[0] + (theta[1] * size) + (theta[2] * rooms))

def regularize(X):
    r_X = []
    for feature in range(len(X)):
        if feature > 0:
            examples = X[feature]
            average = float(sum(examples)) / len(examples)
            variance = np.std(examples)
            r_X.insert(feature, (examples - average) / variance) 
        else:
            r_X.insert(0, X[0])
    return np.array(r_X)

def main():
    X, y, length = grabData()
    X = regularize(X)
    theta = np.array([0.,0.,0.])
    theta = gradientDescent(X, y, theta, length)
    print('final_cost:', computeCost(np.dot(X.T,theta), y))
    print('predicted value for 3 rooms, 2104', predict(2104, 3, theta))

main()
