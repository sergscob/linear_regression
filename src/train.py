import pandas as pd
import argparse

from plot import plot_scatter, plot_loss
from util import loadCSV, saveTheta

def main():

    X, y = loadCSV("data/data.csv")

    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X_norm = (X - mean) / std

    theta0 = 0.0
    theta1 = 0.0
    lr = 0.07
    epochs = 100

    m = len(X)
    loss_history = []

    # gradient descent
    for i in range(epochs):

        y_pred = theta0 + theta1 *  X_norm

        error = y_pred - y 
        loss = (1 / (2 * m)) * (error ** 2).sum()
        loss_history.append(loss)
        
        # print(f"Epoch {i+1}/{epochs}, Error: {error.sum()}")
        tmp_theta0 = lr * (1/m) * error.sum()
        tmp_theta1 = lr * (1/m) * (error * X_norm).sum()

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1


    real_theta1 = theta1 / std
    real_theta0 = theta0 - (theta1 * mean / std)

    saveTheta(real_theta0, real_theta1, "data/theta.json")
    plot_scatter(X, y, real_theta0, real_theta1)
    plot_loss(loss_history)
    print (f"theta0: {real_theta0:.2f}, theta1: {real_theta1:.2f}")

    y_pred = real_theta0 + real_theta1 * X
    ss_res = ((y - y_pred) ** 2).sum()
    ss_tot = ((y - y.mean()) ** 2).sum()

    r2 = 1 - (ss_res / ss_tot)

    print(f"Presision (R**2): {r2:.2f}")


if __name__ == "__main__":
    main()    



