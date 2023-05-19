import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":
    

    df = pd.read_csv("hw5.csv")
    n = len(df)
    x = df['year']
    df.plot('year', 'days',legend = False, ylabel = "Number of frozen days",xlabel = "Years")
    plt.xticks(np.linspace(x[0],x[n-1],dtype ='int64',num=3))
    plt.savefig("plot.jpg")

    X = np.append(np.ones((n,1), dtype='int64'),x.to_numpy().reshape(-1,1),axis=1)
    print("Q3a:")
    print(X)

    Y = df['days'].to_numpy()
    print("Q3b:")
    print(Y)

    Z = np.dot(np.transpose(X),X)
    print("Q3c:")
    print(Z)

    I = np.linalg.inv(Z)
    print("Q3d:")
    print(I)

    PI = np.dot(I,np.transpose(X))
    print("Q3e:")
    print(PI)

    hat_beta = np.dot(PI,Y)
    print("Q3f:")
    print(hat_beta)

    y_test = hat_beta[0]+hat_beta[1]*2021
    print("Q4: " + str(y_test))

    if hat_beta[1]>0:
        sign = ">"
        word = "increase"
    elif hat_beta[1]<0:
        sign = "<"
        word = "decrease"
    else:
        sign = "="
        word = "unchanged"

    print("Q5a: " + sign)

    print("Q5b: The sign indicates that number of iced days is expected to " + word + " by "+ str(abs(hat_beta[1])) +" days when year increase by 1.")

    xstar = -hat_beta[0]/hat_beta[1]
    print("Q6a: " + str(xstar))

    print("Q6b: It is a compelling prediction because the overall trend of the number of iced days is downwards as time goes by and the global warming could explain this phenomenon.")