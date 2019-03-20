#a)read the singpore.csv data in 
library(readr)
dataset <- read_csv("ACST890/singapore.economy.csv")
View(dataset)
#Omitted the NA's
ClearNA<-na.omit(dataset)
ClearNA
#C)plotting grpah
plot(ClearNA$time, ClearNA$gdp,type="l", xlab = "Time", ylab = "GDP (%)", main = "Singapore GDP growth")
#d)mean and standard deviation
Mean<-aggregate(gdp~period,ClearNA,mean)

Std<-aggregate(gdp~period,ClearNA,sd)

stat.table<-data.frame(c(Mean,Std))

names(stat.table)<-c("period","Mean","period","Std")
head(stat.table)
#e)scatterplot

pairs (~gdp + exp + epg + hpr + gdpus + oil + crd + bci,data=ClearNA)
#f)linear regression
Linearregression = lm(gdp~exp, data=dataset)
Linearregression
summary (Linearregression)
#g)multilinear regression

multiregression = lm(gdp~exp+epg+hpr+oil+gdpus+crd, data=ClearNA)
multiregression
summary (multilinearregression)
#h)quantile and state factor and logical regression
qs<-quantile (ClearNA$gdp, probs = 0.05 )

state<-rep(c("normal"),nrow(ClearNA))
state[ClearNA$gdp<qs]<-"crisis"
state<-as.factor(state)
ClearNA<-data.frame(ClearNA,state)


plotdata<-subset(ClearNA,time<2008)
logisticmodel<-glm(state~bci,data=plotdata,family = binomial)
summary(logisticmodel)


