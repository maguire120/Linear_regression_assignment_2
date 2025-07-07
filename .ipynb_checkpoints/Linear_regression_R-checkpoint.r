library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

dataset <- read.csv ("regression_data.csv")
# R syntax to read in the data

# Data
df <- data.frame(
  x = (dataset$YearsExperience),
  y = (dataset$Salary)
)
# data.frame creates the data frome from our inputs using YearsExperience as x and Salaary as Y

# Fit model
model <- lm(y ~ x, data = df)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(df$x, df$y)
pred <- predict(model)
mse <- mean((df$y - pred)^2)

# creating our model to predict Y based on X, the y~x means modeling y as a linear function of x for the predicted best fit
# find the slope and intercept of our predicted y value line
# cor finds the corrleation between x and y (postive or negative)
# predicting y values based on the model, then calculating the mean squared error to see how well the prediction fits
            
# Plot
            
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 1.5, y = max(df$y) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "x", y = "y") +
  theme_minimal()
            
# creating the plot with the modeling we made
            
ggsave("regression_plot_r.png")
            
# creating a png to save of the plot we produced from the modeled data


