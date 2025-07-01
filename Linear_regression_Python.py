#!/usr/bin/env python
# coding: utf-8

# # Plotting Linear Regression Using Python
# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# In[1]:
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()


# these files are installed through the environment setup, but we need to import in into the notebook to use it


# In[3]:


dataset = pd.read_csv("regression_data.csv")
# after importing pandas we read in the data


# In[4]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
# the data has been read in by pandas, now we use matplotlib to plot and visualize the data


# In[5]:



model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])
# pulling in the LinearRegreesion from the sk_learn, then setting it under the name of model, then making that function with out data set


# In[7]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
# This is to create the plot and include everything we want in the plot, such as the prediction of the linear fit we modeled and overlaying the scatter plot


# In[8]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]]) 


# In[ ]:


# Code to calculate the R squared value from the data set

