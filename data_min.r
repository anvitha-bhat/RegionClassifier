rm(list=ls())

data = read.csv("scrape/out.txt",header = TRUE)

#removing irrelavant information
data$rv_park <- NULL
data$plumber <- NULL
data$airport <- NULL
data$aquarium <- NULL
data$accounting <- NULL
data$amusement_park <- NULL
data$bicycle_store <- NULL
data$campground <- NULL
data$bowling_alley <- NULL
data$casino <- NULL
data$car_rental <- NULL
data$car_wash <- NULL
data$cemetery <- NULL
data$car_wash<- NULL
data$courthouse<- NULL
data$convenience_store<- NULL
data$city_hall<- NULL
data$department_store<- NULL
data$electrician<- NULL
data$embassy<- NULL
data$establishment<- NULL
data$finance<- NULL
data$fire_station<- NULL
data$food<- NULL
data$florist<- NULL
data$funeral_home<- NULL
data$general_contractor<- NULL
data$grocery_or_supermarket<- NULL
data$health<- NULL
data$liquor_store<- NULL
data$locksmith<- NULL
data$mosque<- NULL
data$movie_rental<- NULL
data$moving_company<- NULL
data$museum<- NULL
data$painter<- NULL
data$parking<- NULL
data$pet_store<- NULL
data$place_of_worship<- NULL
data$physiotherapist<- NULL
data$roofing_contractor<- NULL
data$stadium<- NULL
data$storage<- NULL
data$subway_station<- NULL
data$synagogue<- NULL
data$taxi_stand<- NULL
data$train_station<- NULL
data$veterinary_care<- NULL
data$zoo<- NULL

#removing place names
data_nameless <- data
data_nameless$name <- NULL
data_nameless <- aggregate(.~place+type,data=data_nameless,FUN=sum)

#summing up the sectors
data_sector_sum <- data_nameless
data_sector_sum$place <- NULL
data_sector_sum <- aggregate(.~type,data=data_nameless,FUN=sum)

#----------------------------------------------------------------------------
#Number of (type) sectors
Ncommercial<-nrow(data_nameless[data_nameless$type=="commercial",])
Nindustrial<-nrow(data_nameless[data_nameless$type=="industry",])
Nresidential<-nrow(data_nameless[data_nameless$type=="residential",])
Nit<-nrow(data_nameless[data_nameless$type=="it",])
Nentertainment<-nrow(data_nameless[data_nameless$type=="entertainment",])

#Finding mean values
Ncolumns <-ncol(data_sector_sum)
COMMERCIAL_MEAN <- data_sector_sum[data_sector_sum$type=="commercial",c(3:Ncolumns)]/Ncommercial
RESIDENTIAL_MEAN <- data_sector_sum[data_sector_sum$type=="residential",c(3:Ncolumns)]/Nresidential
INDUSTRY_MEAN <- data_sector_sum[data_sector_sum$type=="industry",c(3:Ncolumns)]/Nindustrial
ENTERTAINMENT_MEAN <- data_sector_sum[data_sector_sum$type=="entertainment",c(3:Ncolumns)]/Nentertainment
IT_MEAN <- data_sector_sum[data_sector_sum$type=="it",c(3:Ncolumns)]/Nit
#--------------------------------------------------------------------------
# Kmeans 

wssplot <- function(data, nc=15, seed=1234){
  wss <- (nrow(data)-1)*sum(apply(data,2,var))
  for (i in 2:nc){
    set.seed(seed)
    wss[i] <- sum(kmeans(data, centers=i)$withinss)}
  plot(1:nc, wss, type="b", xlab="Number of Clusters",
       ylab="Within groups sum of squares")}

data_nameless$place <- NULL
data_nameless$type <- NULL
#data_nameless_std <- scale(data_nameless[-1])
data_nameless_std <- data_nameless
wssplot(data_nameless)

k.means.fit <- kmeans(data_nameless_std,4)
k.means.fit$centers

library(cluster)
clusplot(data_nameless_std, k.means.fit$cluster, main='2D representation of the Cluster solution',
         color=TRUE, shade=TRUE,
         labels=2, lines=0)





