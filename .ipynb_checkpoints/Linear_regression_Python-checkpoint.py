#!/usr/bin/env python
# coding: utf-8

# # Plotting Linear Regression Using Python
# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# In[57]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.stats import linregress
import sys
# these files are installed through the environment setup, but we need to import in into the notebook to use it
# pulling in more packages to help with more detailed analysis and numpy can help make the script usable for any generic data set

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

# In[58]:


dataset = pd.read_csv("regression_data.csv")
# after importing pandas we read in the data


# ## Git and Improvements to Assignment 2
# This is an improvement to the linear regression model that we ran above

# In[59]:


print(dataset.columns)


# In[60]:


def load_data(df, x_col, y_col):
    x = np.array(df[x_col])
    y = np.array(df[y_col])
    return x, y
# we are loading in the dataframe with the df which is from pandas, and then taking the name of the x and y columns with x_col or y_col
# after getting the finding the x and y column names, we use numpy to put the values belonging to those columns into an array


# In[61]:


x_col = "YearsExperience"
y_col = "Salary"
x, y = load_data(dataset, x_col, y_col)
# making new variables to rename the x and y columns from the dataset to x_col and y_col
# making variables x and y that are the values of the columns from the dataset


# In[62]:


from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print ("slope =", slope, "intercept =", intercept, "r_value =", r_value, "p_value =", p_value, "std_err =", std_err)
# importing linregress from scipy.stats to calculate each of the measures listed, then printing them for visualization


# In[63]:


from sklearn.metrics import mean_squared_error
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)
print ("mse =", mse)
# now we import mean_squared_error to see how close our model is to predicting the actual data


# In[64]:


plt.plot(x, y_pred, 'r-', label='Fitted Line')
# adds a line that is red in color (r-) named Fitted line (label=) and the line is based off of the acutal x values and the predictedy values that was defined during the mse calculation
plt.scatter(x, y)
# actual data from the data set plotted into a scatter blot
plt.text(1.5, max(y) - 1,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
# test added into the plot at certain coordinates (1.5, max) and prints the y=mx+b formula with values as well as MSE onto the plot
plt.xlabel(x_col)
plt.ylabel(y_col)
# adds labels for the x and y axis, using the previously defined variables x_col and y_col
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
# saves png copy of the plot
plt.show()


# In[ ]:




