## Linear_regression_assignment_2 updated to assignment_3
    

### Purpose of Assignment_3
For assignment_2 the goal was to read in a set of data, plotting it in a scatter plot using both python and R, and modeling a linear regression to the data and adding it to the visualized plot.
Assignment_3 built upon what we made with assignment_2 to make improved plots, and gain more experience with improving scripts and code

### Packages used for the completion of Assignment_2
pandas
matplotlib
scikit-learn
scipy
ggplot2
numpy

## Files found in Assignment_3
The following headings are the files found in this repo and a description of them

### regression_data.csv
CSV file containing the data. The data is entered into two columns title YearsExperience and Salary. There are 10 data points for both YearsExperience and Salary
### Linear_regression_python.ipynb
Jupyter lab notebook providing the code to perform a linear regression of the data in the regression_data.csv file. In order to run the code found in this notebook, user will need pandas, matplotlib, scikitlearn, numpy, and scipy.
Variables in this file are are defined as:
##### x_col= YearsExperience 
##### y_col= Salary 
##### x, y= values of the data in the .csv file
##### y_pred= estimate of y as a fucntion of x, being y=mx+b
The general flow of the notebook is as follows:
##### read in the data set, with python, using numpy to set the values in the columns as arrays, using scipy to create a linear regression to determine the slope, intercept, r value, p value, and the std error. Then we use scikit learn to calculate the mean squared error. MSE is cacluated from y_pred with the slope and intercept gathered before. Finally all the data we collected is plotted using matplot.lib including the linear regression line and the scatter plot.
### Linear_regression_python.html 
html file of the code used to plot the data set and linear regression model using Python. The work flow of this file is similar to the Linear_regression_python.ipynb.
### Linear_regression_Python.py
script written in Python that can run a linear regression of any data set containing 2 columns with the inputs of the input of the data file name, and both column title names. The work flow of this script follows the description of Linear_regression_python.ipynb. To run this script the following import is needed:
##### sys
sys will allow us to set arguments to be entered to set and provide direction for the data file being read, and the column names. The code is set to accept only 4 arguments. The first arugment is the script. Additional arguments are entered under new variables named as followed:
##### filename= sys.argv[1]
##### x_col= sys.argv[2]
##### y_col= sys.argv[3]

### regression_plot_python.png
image file of the data plot generated from running the script written in python to plot linear regression
### Linear_regression_R.ipynb
Jupyter lab notebook providing the code to perform a linear regression of the data in the regression_data.csv file. In order to run the code found in this notebook, user will need ggplot2.
Variables in this file are are defined as:
##### dataset= read of the regression_data.csv file
##### df= data frame of the .csv file columns YearsExperience and Salary 
##### model= modeling linear regression from the x and y column values
##### slope= slope line generated in model
##### intercept= y intercept generated in model
##### r= r value generated in model
##### pred= predtion of the y values based on the x values and values defined above 
##### mse= mean squared error generated from pred
The general flow of the notebook is as follows:
##### read in the data set, with R, using R we calcuate the values of the variables mentioned above. Finally all the data we collected is plotted using ggplot2 including the linear regression line and the scatter plot.
### Linear_regression_R.html
html file of the code used to plot the data set and linear regression model using R. The work flow of this file is similar to the Linear_regression_R.ipynb.
### Linear_regression_R.r
script written in R that can run a linear regression of any data set containing 2 columns with the inputs of the input of the data file name, and both column title names. The work flow of this script follows the description of Linear_regression_R.ipynb. The code is set to accept only 3 arguments. Arguments are entered under new variables named as followed:
##### filename= sys.args[1]
##### x_col= sys.args[2]
##### y_col= sys.args[3]
### regression_plot_r.png
image file of the data plot generated from running the script written in R to plot linear regression
    
## Additional purpose to Assignment_3

As a part of Assignment_3 the idea of github branches and commit to branch to maintain a previous version of a working file
When the branch has been finished and validated to work, is accurate, and has been reviewed the branch can be merged into the main branch while maintaining a version history