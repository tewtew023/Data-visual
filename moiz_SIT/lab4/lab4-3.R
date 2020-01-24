#install.packages("tidyverse")
#install.packages("RColorBrewer")

library("tidyverse")
library("RColorBrewer")

setwd("D:/moiz_SIT/lab4")
rm(list=ls())

scb_data <- read.csv("./data/flowingdata_subscribers.csv",sep = "," ,header=TRUE)



scb_obj = ggplot(data=scb_data, aes(x=Date,y=Subscribers))+xlab("Date")+ylab("subscriber")+ggtitle("Subscirber Rising")+ theme(axis.text.x = element_text(angle = 270, hjust = 1))


scb_point = scb_obj+geom_point(stat="identity")+scale_fill_manual(values = c("#e5f5f9"))+guides(fill = guide_legend(title="Number of subscriber"))

scb_point

