## Purpose of Assignment_3
For assignment_2 the goal was to read in a set of data, plotting it in a scatter plot using both python and R, and modeling a linear regression to the data and adding it to the visualized plot.
Assignment_3 built upon what we made with assignment_2 to make improved plots, and gain more experience with improving scripts and code

## Packages used for the completion of Assignment_2
##### pandas
##### matplotlib
##### scikit-learn
##### scipy
##### ggplot2
##### sys
##### numpy

## Files found in Assignment_3
### regression_data.csv 
CSV file that contains 2 columns of data titled YearsExperience and Salary
### Linear_regression_python.ipynb
Jupyter lab notebook that provides the framework for constructing a linear regression from the data found in regression_data.csv using python. The variables used in this notebook are as follows:
#### dataset
regression_data.csv data read in with pandas
#### x_col
YearsExperience string
#### y_col
Salary string
#### x, y
Values of the columns found in the data set, YearsExperience and Salary
##### 
The basic flow of the notebook is the required packages are imported in, the data is read in using pandas, then numpy is used to create arrays of the values found in each of the columns. After creating the variables, the slope, intercept, r_value, p_value and linear regression from the variable x, y is created using the scipy linregress.Then sklearn is used to import the mean_squared_error function to create the new variable:
#### y_pred
prediction of the y values using y=mx+b
#####
After creating all of the values, we use matplotlib to construct a plot of the data and linear regression with the values printed on the graph
### Linear_regression_python.html
html file of the code from the Linear_regression_python.ipynb file described above
### Linear_regression_Python.py
script written in Python based on the code from the Linear_regression_python.ipynb. In order to make this script able to run a linear regression and create a plot similar to the way it was done for regression_data.csv, additional code was needed. It is required to import sys, then create variables that are the arguments to input. The argument variables are as follows:
#### filename
sys.argv[1] - name of the data set you are pulling data from
#### x_col
sys.argv[2] - name of the column of data that will be plotted along the x axis
#### y_col
sys.argv[3] - name of the column of data that will be plotted along the y axis
#####
The remainder of the script runs similar to the code in the notebook, with a png image of the plot created being saved and shown.
### regression_plot_python.png
image file of the data plot generated from running the script written in python to plot linear regression
### Linear_regression_R.ipynb 
Jupyter lab notebook that provides the framework for constructing a linear regression from the data found in regression_data.csv using R. The variables used in this notebook are as follows:
#### dataset
regression_data.csv read in data
#### df
pulls in the values for x (YearsExperience) and y (Salary) from the dataset variable
#### model
making a model of the linear regression from the values of x using the data set from the df variable
#### slope
slope from the linear regression model variable
#### intercept
y intercept from the linear regression model variable
#### r
r_value from the linear regression model variable
#### pred
using the model to predict the y values in the model
#### mse
mean squared error measured from the pred variable
##### 
The basic flow of the notebook is ggplot2 is imported, the dataset regression_data.csv is loaded in then the variables described above are created. From the created variables, we use ggplot2 to create a plot of the data with the linear regression and values printing onto the plot
### Linear_regression_R.html
html file of the code from the Linear_regression_R.ipynb file described above
### Linear_regression_R.r
script written in R based on the code from the Linear_regression_R.ipynb. In order to make this script able to run a linear regression and create a plot similar to the way it was done for regression_data.csv, additional code was needed. It is required to import sys, then create variables that are the arguments to input. The argument variables are as follows:
#### filename
sys.args[1] - name of the data set you are pulling data from
#### x_col
sys.args[2] - name of the column of data that will be plotted along the x axis
#### y_col
sys.args[3] - name of the column of data that will be plotted along the y axis
#####
The remainder of the script runs similar to the code in the notebook, with a png image of the plot created being saved.
### regression_plot_r.png 
image file of the data plot generated from running the script written in R to plot linear regression
 
## Additional purpose to Assignment_3

As a part of Assignment_3 the idea of github branches and commit to branch to maintain a previous version of a working file
When the branch has been finished and validated to work, is accurate, and has been reviewed the branch can be merged into the main branch while maintaining a version history
    