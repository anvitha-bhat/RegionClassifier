rm(list=ls())
library(plyr)
library(ggplot2)

data = read.csv("merged.csv",header = TRUE)

ct_map <- ddply(data, .(type, cluster), summarize, freq=length(type))

ct_map$cluster <- as.factor(ct_map$cluster)

#comm <- ct_map[ct_map$type=="commercial",c(2,3)]
#residential <- ct_map[ct_map$type=="residential",c(2,3)]
#it <- ct_map[ct_map$type=="it",c(2,3)]
#entertainment <- ct_map[ct_map$type=="commercial",c(2,3)]