args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot)
print(plot)

dataset <- read.csv ("regression_data.csv")
# R syntax to read in the data

plot(dataset$YearsExperience, dataset$Salary, col="red")
# plotting data in a scatter plot with R

model <- lm(Salary ~ YearsExperience, data=dataset)
#creating a model of the dataset

ggplot(dataset, aes(x = YearsExperience, y = Salary)) +
  geom_point(colour = 'red') +
  geom_line(aes(y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')
#using an R package called ggplot2 to generate the plot with the best fit line

summary(model)

# calculating the R squared value from the model we created
