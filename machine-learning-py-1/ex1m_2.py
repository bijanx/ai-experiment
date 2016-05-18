import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

ITERATIONS = 1
ALPHA = 0.3

def grabdata():
    print('GRAB DATA==========================================================================')
    data = pd.read_csv('ex1data2.csv').as_matrix()
    print('raw data =', data)
    columns = data.T
    print('data in column form =', columns)
    X_0 = [1] * len(columns[0])
    X = np.array([X_0, columns[0], columns[1]])
    y = columns[2]
    print('x values =', X)
    print('y values =', y)
    return X, y 

def gradientDescent(X, y):
    print('GRADIENT DESCENT===================================================================')
    theta = np.array([0,0,0])
    for iter in range(ITERATIONS):
        for feature in range(len(X)):
            htheta = X.T * theta 
            print('htheta = ', htheta)
            error = htheta.T - y
            print('initial error', error)
            f_error = error * X[feature]
            print('feature error', f_error)
            i_sum = sum(f_error)
            print('initial sum', i_sum)
            a_sum = i_sum / 2 * len(X[feature])
            print('averaged sum', a_sum)
            alpha_sum = a_sum * ALPHA
            print('alpha times sum', alpha_sum)
            new_theta = theta[feature] - 

def regularize(X):
    print('REGULARIZATION===================== = = = = ============ = = = ====================')
    print('X before regularization', X)
    print('length of X', len(X))
    regularized_X = []
    for index in range(len(X)):
        if index > 0:
            average = sum(X[index]) / len(X[index])
            print('average', average)
            variance = np.std(X[index])
            print('variance', variance)
            averaged = X[index] - average
            print('averaged', averaged)
            result = averaged / variance
            #print('result', result)
        else:
            result = X[index]
        regularized_X.insert(index, result)

    print('regularized X is', regularized_X)
    return np.array(regularized_X)
       


def main():
    X, y = grabdata()
    X = regularize(X)
    print('X before descent', X)
    theta = gradientDescent(X, y)
    

main()
