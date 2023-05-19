import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    input_file = sys.argv[1]
    data = pd.read_csv(input_file)

    plt.plot(data["year"], data["days"])
    plt.xlabel("Year")
    plt.ylabel("Number of ice days")
    plt.savefig("plot.jpg")


    ones_column = np.ones((len(data), 1), dtype="int64")
    X = np.hstack((ones_column, data[["year"]].to_numpy()))
    Y = data["days"].to_numpy()
    X_T=np.transpose(X)
    Z = np.dot(X_T, X)
    I = np.linalg.inv(Z)
    PI = np.dot(I, X_T)

    hat_beta = np.dot(PI, Y)

    x_test = np.array([1, 2022])
    y_test = np.dot(x_test, hat_beta)

    x_power = (-hat_beta[0])/hat_beta[1]

    print("Q3a:")
    print(X)

    print("Q3b:")
    print(Y)

    print("Q3c:")
    print(Z)

    print("Q3d:")
    print(I)

    print("Q3e:")
    print(PI)

    print("Q3f:")
    print(hat_beta)

    print("Q4: " + str(y_test))

    if (hat_beta[1] > 0):
        print("Q5a: >")
        print("Q5b: A positive value indicates that the number of ice days is increasing as time passes.")
    elif (hat_beta[1] < 0):
        print("Q5a: <")
        print("Q5b: A negative indicates that the number of ice days is decreasing as time passes.")
    else:
        print("Q5a: =")
        print("Q5b: A value of equal to zero indicates that there is no linear trend in the number of ice days as time passes.")


    print("Q6a:" + str(x_power))
    print("Q6b: When we look at the graph, the trend seems to be negation. This means less ice days as time passes on. So, the above prediction sure is compelling.")


    
if __name__=="__main__":
    main()
