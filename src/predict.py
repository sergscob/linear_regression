import pandas as pd
from plot import plot_scatter
from util import loadTheta

def main():

    theta0, theta1 = loadTheta("data/theta.json")
    # print(f"theta0: {theta0}, theta1: {theta1}")

    km_max = - theta0 / theta1 

    s = input("Mileage of your car ? ")
    if not s or not s.isdigit():
        print('\nPlease enter a number')
        exit(1)

    km = float(s)
    if km < 0 or km >= km_max:
        print("Please enter a number between 0 and " + str(int(km_max)))
        exit(1)

    price = theta0 + km * theta1
    print("\nYour estimated price: " + str(int(price)))


if __name__ == '__main__' :
	main()
