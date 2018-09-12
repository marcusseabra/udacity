setwd('/home/seabra/dev/udacity/eda/exemplos')

entrevistasInfo <- read.csv('reddit.csv')
table(entrevistasInfo$employment.status)
summary(entrevistasInfo)

str(entrevistasInfo)
levels(entrevistasInfo$age.range)

library(ggplot2)

qplot(data = entrevistasInfo, x = age.range)
qplot(data = entrevistasInfo, x = income.range)

# Order the factor levels in the age.range variable in order to create
# a graph with a natural order. Look up the documentation for
# the factor function or read through the example in the Instructor Notes.

# Once you're ready, try to write the code to order the levels of
# the age.range variable.

# Be sure you modify the variable in the data frame. That is modify reddit$age.range.
# Don't create a new variable.

# The levels of age.range should take on these values...

#    "Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"

# This exercise is ungraded. You can check your own work by using the Test Run
# button. Your plot will appear there.

# ENTER YOUR CODE BELOW THE LINE.
# ================================================================================


# Variáveis fatoriais
set.seed(124)

exemplo <- sample(0:1, 20, replace = TRUE)

is.factor(exemplo)

is.numeric(exemplo)

exemplo.f <- factor(exemplo, labels = c("private", "public"))
exemplo.f

levels(exemplo.f)

is.factor(exemplo.f)

statusSocial <- c("low", "middle", "low", "low", "low", "low", "middle", "low", "middle",
                  "middle", "middle", "middle", "middle", "high", "high", "low", "middle",
                  "middle", "low", "high")
is.factor(statusSocial)

is.character(statusSocial)

statusSocial.niveis <- factor(statusSocial, levels= c("low", "middle", "high"))

levels(statusSocial.niveis)

statusSocial.ordenado <- ordered(statusSocial, levels= c("low", "middle", "high"))
statusSocial.ordenado

is.factor(statusSocial.ordenado)

statusSocial.ordenado <- ordered(statusSocial, levels= c(levels(statusSocial.ordenado) , "very.high"))
statusSocial.ordenado[21] <- "very.high"
statusSocial.ordenado
