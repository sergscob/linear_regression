import pandas as pd
import json
import sys

def loadCSV(file_path):
	try:
		df = pd.read_csv(file_path, header=None)
	except:
		print(f"Error: Could not load CSV from {file_path}")
		sys.exit(1)
	df.columns = ["km", "price"]
    # df.columns = df.columns.str.strip()

	df["km"] = pd.to_numeric(df["km"], errors="coerce")
	df["price"] = pd.to_numeric(df["price"], errors="coerce")
	df = df.dropna()

    # print (len(df["price"]))

	X = df["km"].to_numpy()
	y = df["price"].to_numpy()

	return X, y


def saveTheta(theta0, theta1, file_path):
    with open(file_path, "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f)


def loadTheta(file_path):
	try:
		with open(file_path, "r") as read_file:
			data = json.load(read_file)
			return data["theta0"], data["theta1"]
	except:
		print(f"Price: 0")
		print(f"Error: Could not load theta from {file_path}. Run train.py to generate theta file.")
		sys.exit(1)

