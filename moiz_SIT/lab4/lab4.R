#install.packages("tidyverse")
#install.packages("RColorBrewer")

library("tidyverse")
library("RColorBrewer")

setwd("D:/moiz_SIT/lab4")
rm(list=ls())

hd_data <- read.csv("./data/hot-dog-contest-winners.csv",sep = "," ,header=TRUE)


colnames(hd_data)[3] = "eaten"
colnames(hd_data)[5] = "new_rec"

hd_data$new_rec = as.factor(hd_data$new_rec)

hd_obj = ggplot(data=hd_data, aes(x=Year,y=eaten, fill=new_rec))+xlab("year")+ylab("Hot dogs and buns (HDB) eaten")+ggtitle("Nathan's hot dogs eating contest result, 1980-2010") + theme(plot.title = element_text(hjust=0.5))


hd_bar = hd_obj+geom_bar(stat="identity")+scale_fill_manual(values = c("#e5f5f9","#7fcdbb"))+guides(fill = guide_legend(title="New record"))

hd_bar