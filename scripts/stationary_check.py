from statsmodels.tsa.stattools import adfuller
import numpy as np
import matplotlib.pyplot as plt

# using variance and mean to check stationarity

def check_stationary_mv(df, title):
    print()
    print(title)
    print()
    X = df[0:].values
    split = round(len(X) / 3) # Splitting the data into three equal parts
    X1, X2 , X3 = X[0:split], X[split:2*split] , X[2*split:] # Spliting the dataset to check mean and std stationarity across a period of time
    mean1, mean2 , mean3 = X1.mean(), X2.mean() , X3.mean()
    var1, var2, var3 = X1.var(), X2.var() , X3.var()
    print('mean1= %f, mean2= %f, mean3= %f' % (mean1, mean2,mean3))
    print('variance1= %f, variance2= %f, variance3=%f' % (var1, var2,var3))

# using The Augmented Dickey-Fuller test to check stationarity

def check_stationary_adf(df, col, title):
    print()
    print(title )
    print()
    adfResult = adfuller(df[col].values, autolag='AIC')
    print(f'ADF Statistic: {adfResult[0]}')
    print(f'p-value: {adfResult[1]}')
    return adfResult

# Creating a correlation graph 

def corrPlots(array: np.array, prefix: str):
    plt.figure(figsize=(30, 5))
    plt.title(f"{prefix}  Autocorrelations of Sales")
    plt.bar(range(len(array)), array)
    plt.grid(True)
    plt.show()
    plt.savefig('../charts/'+str(prefix)+'.jpg')