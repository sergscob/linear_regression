import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(X, y, theta0, theta1):

    plt.figure(figsize=(10, 6))

    X_line = np.linspace(X.min(), X.max(), 2)
    y_line = theta0 + theta1 * X_line

    plt.scatter(X, y, label="Data points")
    plt.plot(X_line, y_line, color="red", label="Regression line")

    plt.title("Car Price")
    plt.xlabel("km")
    plt.ylabel("price")
    plt.grid(True)

    plt.savefig("charts/scatter.png")


def plot_loss(loss_history):

    plt.figure(figsize=(10, 6))

    plt.plot(loss_history)

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss Curve")
    plt.ticklabel_format(style='plain', axis='y')

    plt.grid(True)

    plt.savefig("charts/loss.png")
