getwd()

setwd('/home/seabra/dev/udacity/eda')

getwd()

setwd('/home/seabra/dev/udacity/eda/exemplos')

getwd()

statesInfo <- read.csv('stateData.csv')

subset(statesInfo, state.region == 1)

statesInfo[statesInfo$state.region == 1, ]

taxaHomicidios <- subset(statesInfo, murder >= 10)
head(taxaHomicidios)
