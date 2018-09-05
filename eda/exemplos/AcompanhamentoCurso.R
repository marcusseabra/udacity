setwd('/home/seabra/dev/udacity/eda/exemplos')

entrevistasInfo <- read.csv('reddit.csv')
table(entrevistasInfo$employment.status)
summary(entrevistasInfo)

str(entrevistasInfo)
levels(entrevistasInfo$age.range)

qplot(data = entrevistasInfo, x = age.range)
qplot(data = entrevistasInfo, x = income.range)
